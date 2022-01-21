# Book Recommendation and Sharing  


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Features](#features)
  * [Tech Stack](#tech-stack)
  * [File Structure](#file-structure)
* [Getting Started](#getting-started)
* [Results and Demo](#results-and-demo)
* [Future Work](#future-work)
* [Contributors](#contributors)
* [Acknowledgements and Resources](#acknowledgements-and-resources)


<!-- ABOUT THE PROJECT -->
## About The Project
Our aim is to create a web portal for recommending books based on collaborative filtering. Also, providing user option to search book price online (using web scraping) and offline exchange of books using location of the seller (using spatial analysis).
Refer this [documentation](https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Project%20Report.pdf).

### Features
* *Registration for Users :*    
  Users can register on our platform to explore all the features .

* *Search :*    
In this feature users can look for the book as per their interest.
  * Search by name
  * Search by author
  * Search by Genre

* *Get Recommendation:*   
   In this feature, we recommend books to users based on what other similar users have read and chosen as favorite book.
    
* *Online Price:*   
   You can check the online price of books from different sites and navigate to that site to buy the books online

* *Connect:*    
  You can connect with other users and exchange the book you want from them. For this purpose we have used the spatial queries and attributes.
  This has options like finding the users within 1km, 5km, 10km, 15km

* *Save:*   
  Here users can save their favorite genre and favorite books

* *Exchange Books:*     
  Option to fill form to exchange book you have wherein lat, long, book name and book info are taken and stored in the database, so that when someone wants to   exchange that book, he can do the same with you.

* *Registration For NGOs:*    
  This feature is added to help NGOs so that they can get donated books from our users.

* *Donate:*     
  One can donate books to Schools and NGOs to help others to gain maximum knowledge.
  In this feature users are allowed to find the Schools and NGOs nearby their locations. For this purpose we have used the spatial queries and attributes.
  This has options like finding the ngos and schools within 1km, 5km, 10km, 15km
  
<br>

### Tech Stack
Software used for this project :  
* Backend :     
  * Python3       
  * Django  

* Frontend:       
  * HTML  
  * CSS     
  * JS            

* Database:
  * PostGIS 
  * Pgadmin 
  * neo4j 


1 . Django
    Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. Built by experienced developers, Django takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.

2 . Python3
    Python3 is a high-level, interpreted, interactive and object-oriented scripting language. Python is designed to be highly readable. It uses English keywords frequently where as other languages use punctuation, and it has fewer syntactical constructions than other languages.
    
3 . HTML
    HTML (Hypertext Markup Language) is the code that is used to structure a web page and its content. For example, content could be structured within a set of paragraphs, a list of bulleted points, or using images and data tables. 
    
4 . CSS
    Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup 
    language such as HTML. CSS is a cornerstone technology of the World Wide Web, alongside HTML and JavaScript. 

5 . JS
    JavaScript (JS) is a lightweight, interpreted, or just-in-time compiled programming language with first-class functions. While it is most well-known as the scripting language for Web pages, many non-browser environments also use it, such as Node.js, Apache CouchDB and Adobe Acrobat. JavaScript is a prototype-based, multi-paradigm, single-threaded, dynamic language, supporting object-oriented, imperative, and declarative (e.g. functional programming) styles. 

6 . Postgres
    PostgreSQL is used as the primary data store or data warehouse for many web, mobile, geospatial, and analytics applications. The latest major version is PostgreSQL 12.

7 . Postgis
    PostGIS is a spatial database. Oracle Spatial and SQL Server (2008 and later) are also spatial databases. 
    
8 . Pgadmin
    PgAdmin is a web-based GUI tool used to interact with the Postgres database sessions, both locally and remote servers as well. You can use PGAdmin to perform any sort of database administration required for a Postgres database

9 . Neo4j
    Neo4j facilitates personal data storage and management: it allows you to track where private information is stored and which systems, applications, and users access it. The graph data model helps visualize personal data and allows for data analysis and pattern detection


<br>


### File Structure
    .
    ├── Documentation                   # Documentation files       
    │   ├── Project Report.pdf          # Project report
    │   ├── Project Execution Steps.pdf   
    │   └── Results                     # Folder containing screenshots of results
    ├── book_ex                         # Source code for feature - "exchange of books"
    ├── core                            # Source code for core features of webapp
    ├── datasets                        # Datasets required for project
    ├── donation                        # Source code for feature - "donations of books and NGO registration" 
    ├── project                         # Source code for django project with all imports and database connections
    ├── static                          # Contains all CSS, JS, vendors and image files
    ├── templates                       # Contains all HTML pages
    ├── web_scrape                      # Source code for feature - "web scrapping prices of books online in diff sites"
    ├── README.md 
    ├── manage.py                       # File used to run server                     
    └── requirements.txt                # Contains all imports required to run the project              
<br>

### Database Models
<!--Explanation -->
* **Graph Database Model**
  * *Node Properties*
    Node             |Properties  |
    | :------------  | --------: |
    Genre            | name, genre_id|
    Book             |Title, img_url|
    UserProfileInfo  |first_name, last_name, email, username, address, pincode, latitude, longitude, phone|
    Author           |name |


  * *Graph Relationships*
    | Relations     | RelationFrom      | RelationTo  |
    | :------------ |   :---:       | --------: |
    | FAVOURITEGENRE |    UserProfileInfo     |  Genre |
    |    FAVOURITEBOOK   |   UserProfileInfo    | Book  |
    |    GENRE | Genre      | Book  |
    |   WROTE |  Author     | Book  |

<br>        

* **Spatial Database Tables**
     
    * Table : *donation_ngo*     
        |Name of column  | Data Type |              
        | :------------  | --------: |              
        |id  | Integer|              
        |name | Character |            
        |location |geometry(Point) |             
        |address | Character|                
        |city | Character|              

    * Table : *book_ex*
        |Name of column |Data Type Of Column|
        | :------------  | --------: |
        |id|integer|
        |name|character|
        |location|geometry(Point)|
        |address|character|
        |city|character|
        |book|character|
        |author|character|
        |email|character|
        |contact|character|
        |genre|character|

<br>

<!-- GETTING STARTED -->
## Getting Started

### Installation
Clone the repo
```sh
git clone https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing.git
```

### Prerequisites
See [this](https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Project%20Execution%20Steps.pdf) for installation steps, setting up databases and running the project.

<br>

<!-- RESULTS AND DEMO -->
## Results and Demo
* **Home Page**             
    Image 1  | Image 2| 
    | :------------  |  --------: |
    | <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/home1.png">   |   <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/home2.png">    |    
    
    Image 3  | Image 4| 
    | :------------  |  --------: |
    | <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/home3.png">   |   <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/home4.png">    |  
<br>

* **About-Us Page**
    Image 1  | Image 2| 
    | :------------  |  --------: |
    | <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/about-us1.png">   |   <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/about-us2.png">    |  
<br>

* **Register Page**
    Image 1  | Image 2| 
    | :------------  |  --------: |
    | <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/register1.png">   |   <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/register2.png">    |    
    
    Image 3  | Image 4| 
    | :------------  |  --------: |
    | <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/register3.png">   |   <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/register4.png">    |  
<br>

* **Login Page**
    Image 1  | Image 2| 
    | :------------  |  --------: |
    | <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/login1.png">   |   <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/login2.png">   |  
<br>

* **Search Book**
    * **By name**
        Image 1  | Image 2| 
        | :------------  |  --------: |
        | <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/search_book_byname_1.png">   |   <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/search_book_byname_2.png">   |  

        Image 3  | Image 4| 
        | :------------  |  --------: |
        | <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/search_book_byname_3.png">   |   <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/search_book_byname_4.png">    |  
    <br>

    * **By Genre**
        Image 1  | Image 2| 
        | :------------  |  --------: |
        | <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/search_book_bygenre1.png">   |   <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/search_book_bygenre2.png">   |
    <br>

    * **By Author**
        Image 1  | Image 2| Image 3|
        | :------------  | :-------: | --------: |
        | <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/search_book_byauthor1.png">   |   <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/search_book_byauthor2.png">   | <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/search_book_byauthor3.png"> |
    <br>

* **Online Price Page**
    Image 1  | Image 2| 
    | :------------  |  --------: |
    | <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/online_price.png">   |   <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/online_price_redirect.png">   |  
<br>

* **Add to Favorites Page**
    Image 1  |
    | :------------  |
    | <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/add_favorites.png">   |     
<br>

* **Book Exchange Page**
    Image 1  | Image 2| 
    | :------------  |  --------: |
    | <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/book_ex.png">   |   <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/book_ex_result.png">   |  
<br>

* **Book Exchange Form Page**
    Image 1  | Image 2| 
    | :------------  |  --------: |
    | <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/book_ex_form1.png">   |   <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/book_ex_form2.png">   |  
<br>

* **Get Recommendations Page**
    Image 1  |
    | :------------  |
    | <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/get_recommendation.png">   |     
<br>

* **Donate Page**
    Image 1  | Image 2| 
    | :------------  |  --------: |
    | <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/donate.png">   |   <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/donate_results.png">   |  
<br>

* **Register NGOs Page**
    Image 1  | 
    | :------------  |  
    | <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/register_NGO.png">   |  
<br>

* **Profile Page**
    Image 1  | Image 2| 
    | :------------  |  --------: |
    | <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/profile1.png">   |   <img width="600" height="300" src="https://github.com/Bhumika-Kothwal/Book-Recommendation-and-Sharing/blob/master/Documentation/Results/profile2.png">   |  
<br>



<!-- FUTURE WORK -->
## Future Work

<br>

<!-- CONTRIBUTORS -->
## Contributors

* MEMBERS
  1. [Ms. Bhumika Kothwal](https://github.com/Bhumika-Kothwal) : kothwalbhumika@gmail.com
  2. [Ms. Neha Shinde](https://github.com/nbshinde) : nehashinde3399@gmail.com
  3. [Ms. Nishtha Sainger](https://github.com/Bhumika-Kothwal) : kothwalbhumika@gmail.com

<!-- ACKNOWLEDGEMENTS AND REFERENCES -->
## Acknowledgements and Resources
* [Books Dataset](https://github.com/akshaybhatia10/Book-Genre-Classification/tree/master/data)
* Neomodel :
    * [Neomodel Documentation](https://neomodel.readthedocs.io/en/latest/)
    * [Getting Started With Neomodel](https://thobalose.co.za/2016/neomodel/#)