from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import UserProfileInfo, Author, Book, Genre
from django.contrib.auth.models import User as dUser
from core.forms import UserForm
from neomodel import db as neodb
import random



def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def message(request, message):
    return render(request,'core/message.html',{'message':message})



# -------------------------------------- Login Info --------------------------------------
# 1. Login
# 2. Logout
# 3. Register

# Login
def user_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                print("successful")
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("someone tried to login and failed")
            print("Username:{} and password {}".format(username,password))
            return message(request, "Invalid Login Details")
    else:
        return render(request,'login.html')

# Logout
@login_required
def user_logout(request):
    logout(request)
    return message(request, 'Logout successful')

# Register
def user_register(request):
    if request.method=='POST':
        userform = UserForm(data=request.POST)
        genresList = request.POST.getlist('genres')
        #print(genresList)
        if userform.is_valid():
            newUser = userform.save(commit=False)
            newUser.latitude = request.POST.get('latitude')
            newUser.longitude = request.POST.get('longitude')
            print(type(newUser))
            newUser.save()

            user = dUser.objects.create_user(username=request.POST.get("username"),
                                         password=request.POST.get("password"),
                                         is_superuser=False,
                                         ).save()

            for g in genresList:
                #print(g)
                newUser.favGenres.connect(Genre.nodes.get(name=g))
            
            return message(request,'Registered successfully! You can login to proceed.')
        else:
            print(userform.errors)
            return message(request,'Error in registering. Please try again.')

    else:
        user = request.user
        if user.is_authenticated:
            return message(request, 'You are already logged in.')
        else:
            userform = UserForm()
            genreNodes = Genre.nodes
            return render(request,'register.html',{'userform':userform,'genreNodes':genreNodes})




# -------------------------------------- Searching Book --------------------------------------
# 1. Search Book by Name
# 2. Search Book by Genre
# 3. Search Book by Author
# 4. Book-details


# Search Book by Name
def search_by_name(request):
    
    if request.method == 'POST':
        book_name = request.POST.get('searched_book')
        
        bookNode = Book.nodes.get_or_none(Title=book_name)
    
        if(bookNode):
            bookInfo = []
            bookInfo.append(bookNode.Title)
            bookInfo.append(bookNode.wrote.all())
            bookInfo.append(bookNode.img_url)
            bookInfo.append(bookNode.genre.all())

            return render(request, 'core/search_by_name.html', {"book":bookInfo})
        else:
            return message(request, 'The searched book is not available in the Database. Please try a with different name')
            
    return render(request, 'core/search_by_name.html')


# Search Book by Genre
def search_by_author(request):
    if request.method == 'POST':
        author_name = request.POST.get('searched_author')
        
        authorNode = Author.nodes.get_or_none(name=author_name)
        

        if(authorNode):
            books = []
            booksList = authorNode.wrote.all()
            
            random_items = random.sample(booksList, min(len(booksList), 21) )
            for b in random_items:
                books.append([b.Title, b.wrote.all(), b.img_url, b.genre.all()])

            return render(request, 'core/search_author_result.html', {"books":books, "author":authorNode})
        else:
            return message(request, 'The searched author is not available in the Database. Please try a with different name')
            
    return render(request, 'core/search_by_author.html')


# Search Book by Author
def search_by_genre(request):
    allGenres = Genre.nodes

    if request.method == 'POST':
        genresSelected = request.POST.getlist('genres')
        booksToBePassed = {}

        # Selecting random 50 books for each genre
        for g in genresSelected:
            genreNode = Genre.nodes.get(name=g)
            books = []
            booksList = genreNode.bookGenre.all()
            #print(booksList)
            random_items = random.sample(booksList, 21)
            for b in random_items:
                books.append([b.Title, b.wrote.all(), b.img_url, b.genre.all()])
            booksToBePassed[str(genreNode.name)] = books

        return render(request, 'core/search_genre_result.html', {'books': booksToBePassed})

    return render(request, 'core/search_by_genre.html', {'genreNodes': allGenres})


# Book-details 
def book_details(request):
    user = request.user
    book = []
    if request.POST.get('book-details'):
        bookTitle = request.POST.get('book-details')
        bookNode = Book.nodes.get(Title=bookTitle)
        book.append([bookNode.Title, bookNode.img_url, bookNode.wrote.all(), bookNode.genre.all()])

        buttonName = "Add to Favorites"
        if user.is_authenticated:
            userNode = UserProfileInfo.nodes.get(username=user.username)
            if userNode.favBooks.relationship(bookNode):
                buttonName = "Remove from Favorites"
        
        return render(request, 'core/book_details.html', {"book":book, "buttonName":buttonName})
    
    elif request.POST.get('favorite') and user.is_authenticated:
        bookTitle = request.POST.get('favorite')
        bookNode = Book.nodes.get(Title=bookTitle)
        book.append([bookNode.Title, bookNode.img_url, bookNode.wrote.all(), bookNode.genre.all()])

        userNode = UserProfileInfo.nodes.get(username=user.username)

        buttonName = ""
        #added = None
        if userNode.favBooks.relationship(bookNode):
            neodb.cypher_query("MATCH (user:UserProfileInfo {username:$username})-[rel:FAVORITEBOOK]->(:Book{Title:$Title}) DELETE rel", {"username": userNode.username,"Title":bookTitle})
            buttonName = "Add to Favorites"

        else:
            userNode.favBooks.connect(bookNode)
            buttonName = "Remove from Favorites"

        return render(request, 'core/book_details.html', {"book":book, "buttonName":buttonName})

    elif not user.is_authenticated:
        return message(request, "Please Register/Login to use this feature")



# -------------------------------------- Get Book Recommendation--------------------------------------

# Recommend by Similar User's Choice
def search_by_similarUser(request):
    booksToBePassed=[]
    user = request.user

    if user.is_authenticated:
        # Using Favorite Book to find the Similar Users
        userNode = UserProfileInfo.nodes.get(username=user.username)
        userFavBooks = userNode.favBooks.all()
        #print("Fav books = " , userFavBooks)
        if(len(userFavBooks) == 0):
            return message(request, "Please add your favorite books to 'Favorites' by using service 'Add to favorites'")

        otherUsers = []
        for b in userFavBooks:
            for u in b.user.all():
                if u is not userNode and u not in otherUsers:
                    otherUsers.append(u)
        #print("Other users = " , otherUsers)
        

        for u in otherUsers:
            for b in u.favBooks.all():
                if b not in userFavBooks:
                    booksToBePassed.append([b.Title, b.wrote.all(), b.img_url, b.genre.all()])
        #print("Books to be passed = " , booksToBePassed)

        if(len(booksToBePassed) == 0):
            return message(request, "No other user has chosen same Favorite Book as yours")
        return render(request, 'core/search_by_similarUser.html', {'books': booksToBePassed})

    else:
        return message(request, "Please Register/Login to use this feature")




# -------------------------------------- Profile Info --------------------------------------
# 1. Profile

def profile(request):
    if request.user.is_authenticated:
        userNode = UserProfileInfo.nodes.get(username=request.user.username)
        print(request)
        if request.POST.get("removeFav"):
            bookTitle = request.POST.get("removeFav")
            neodb.cypher_query("MATCH (user:UserProfileInfo {username:$username})-[rel:FAVORITEBOOK]->(:Book{Title:$Title}) DELETE rel", {"username": userNode.username,"Title":bookTitle})
        
        elif request.POST.get("removeGenre"):
            genreName = request.POST.get("removeGenre")
            neodb.cypher_query("MATCH (user:UserProfileInfo {username:$username})-[rel:FAVORITEGENRE]->(:Genre{name:$name}) DELETE rel", {"username": userNode.username,"name":genreName})

        elif request.POST.get("addGenre"):
            genre = request.POST.get("addGenre")
            genreNode = Genre.nodes.get(name=genre)
            print(genreNode)
            userNode.favGenres.connect(genreNode)

        booksToBePassed = []
        for b in userNode.favBooks.all():
            booksToBePassed.append([b.Title, b.wrote.all(), b.genre.all()])
        userGenres = userNode.favGenres.all()
        otherGenres = []
        for g in Genre.nodes.all():
            if g not in userGenres:
                otherGenres.append(g)
        

        return render(request,'profile.html',{'userNode':userNode, 'favBooks':booksToBePassed,'userGenres':userGenres,'otherGenres':otherGenres})
        

    else:
        return message(request, "Please Register/Login to use this feature")
