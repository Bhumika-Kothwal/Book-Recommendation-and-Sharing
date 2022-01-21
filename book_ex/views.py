from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from core.models import UserProfileInfo, Book, Author, Genre
from .models import Book_ex
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
import folium
from core.views import message


# CREATING NEW BOOK NODE
def createBookNode(Title, img_url, genre, author):
    bookNode = Book(Title=Title, img_url=img_url, rating=0).save()

    if not Author.nodes.get_or_none(name=author):
        Author(name=author).save()
    authorNode = Author.nodes.get(name=author)

    genreNode = Genre.nodes.get(name=genre)

    authorNode.wrote.connect(bookNode)
    genreNode.bookGenre.connect(bookNode)


# BOOK EXCHANGE FORM
def bookex_form(request):
    name=""
    address=""
    city=""
    lat=0.0
    long=0.0
    book=""
    img_url=""
    author=""
    email=""
    contact=""
    details=False

    if request.method == 'POST' and details==False:
        details=True
        name = request.POST.get('name')
        address= request.POST.get('address')
        city= request.POST.get('city')
        lat=request.POST.get('lat')
        long=request.POST.get('long')
        book= request.POST.get('book')
        img_url=request.POST.get('img_url')
        author=request.POST.get('author')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        genre=request.POST.get('genre')

        location = fromstr(f'POINT({long} {lat})', srid=4326)

        bookNode = Book.nodes.get_or_none(Title=book)
        if not bookNode:
            createBookNode(Title=book, img_url=img_url, genre=genre, author=author)

        s=Book_ex(name=name, location=location, address=address, city=city, book=book,author=author, email=email, contact=contact, genre=genre)
        #print(type(s))
        s.save()
        return message(request,'Thank you for submitting your details!')

    genreNodes = Genre.nodes.all()
    return render(request,'book_ex/bookex_form.html', {"genres":genreNodes})


# finding the nearby users with book req by curr user
def near_book(request):
    if request.POST.get('exchange'):
        bookTitle = request.POST.get('exchange')
        return render(request, 'book_ex/near_book.html', {"book":bookTitle})

    else:
        lat=0.0
        long=0.0
        dist=""
        near=[]
        dirn=[]

        lat=request.POST.get('lat')
        long=request.POST.get('long')
        location = fromstr(f'POINT({long} {lat})', srid=4326)

        dist=request.POST.get('dist')
        print(location)
        book=request.POST.get('book')
        bookTitle=request.POST.get('book')
        print(book)
        if dist=="lt1":
            near = Book_ex.objects.annotate(distance=Distance("location", location)/1000).filter(distance__lte=1, book=book).order_by("distance")
        elif dist=="lt5":
            near = Book_ex.objects.annotate(distance=Distance("location", location)/1000).filter(distance__lte=5, book=book).order_by("distance")
        elif dist=="lt10":
            near= Book_ex.objects.annotate(distance=Distance("location", location)/1000).filter(distance__lte=10, book=book).order_by("distance")
        else:
            near= Book_ex.objects.annotate(distance=Distance("location", location)/1000).filter(distance__lte=15, book=book).order_by("distance")
        
        print(near)
        
        m=folium.Map(location=[lat,long],zoom_start=12)

        folium.Marker(
            [lat,long],
            popup='',
            tooltip='Your Location!',
            icon=folium.Icon(color='red')
        ).add_to(m),

        if len(near)>0:
            for book in near:
                org_address=book.address.replace(' ','+')
                link="https://www.google.com/maps/dir/?api=1&destination=" + org_address
                dirn.append(link)
                tooltip="Name:"+book.name+" , Email:"+book.email+" , Contact:"+book.contact
                folium.Marker(
                    [book.location.y,book.location.x],
                    popup='<a href="' + link + '">GetDirection</a>',
                    tooltip=tooltip
                ).add_to(m)

                m.save('templates/book_ex/map_near_book.html')

        return render(request,'book_ex/near_book.html',{'near':near, 'dirn':dirn,'zip':zip(near,dirn),'book':bookTitle, 'submitted':True})
    

# Showing the user and result on map
def map_near_book(request):
    return render(request,'book_ex/map_near_book.html')
