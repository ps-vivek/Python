'''
This program does the following:
    1) Reads "watchlist.csv" file and generates suggestions for viewing 5 random movies
    2) Converts the contents of "watchlist.csv" into a unicode format and written those contents it into sqlite database
    3) Displays all the movies whose rating is greater than 8.5
    4) Displays the content of entire movie database
    5) Displays the movies released before 2000
    6) Displays the movies whos runtime is less than 100 minutes

"watchlist.csv" contains movie details extracted from my imdb favorite list
'''
import sqlite3,csv,random
con=sqlite3.connect("Test.db")  #creating a database
cur=con.cursor() # creating the cursor for the database
cur.execute('''DROP TABLE movie_list''') # deleting any previously created database of name movie_list

cur.execute("CREATE TABLE movie_list (Title TEXT, IMDbRating REAL, Runtime INTEGER, Year INTEGER);") #creates a table with 4 columns
filename="watchlist.csv"
f2=open(filename,'r')
movie_data=csv.reader(f2) #Return a reader object which will iterate over lines in the given csvfile.
movie_data_processed=list(movie_data) # converts the csv file contents into a list

#Randomly picks 5 movies from the movie list
new_list=random.sample(movie_data_processed,5)
print("<<<Below are 5 movies that you might like to watch>>>")
for movie in new_list:
   print movie[0]
print

movie_data_uni=[]
for movies in movie_data_processed: #converts ascii to unicode format
   uni_list=[unicode(movies[0],"utf8"),unicode(movies[1],"utf8"),unicode(movies[2],"utf8"),unicode(movies[3],"utf8")]
   movie_data_uni.append(uni_list)     #append all the csv file contents to a new list

# inserting data into movie_list table from the given list whose contents are in unicode format
cur.executemany("INSERT INTO movie_list (Title, IMDbRating, Runtime, Year) VALUES (?,?,?,?);",movie_data_uni)

#Display all the movies whose rating is greater than 8.5
cur.execute("SELECT Title,IMDbRating FROM movie_list WHERE IMDbRating > '8.5';")
print ("<<<<Printing the movie name whose imdbrating is greater than 8.5>>>")
for quality_movies in cur:
   print (quality_movies)
   print
print

#Display the collection of all movies
'''
print ("<<<Displaying contents of the entire table>>>>>")
cur.execute("SELECT * FROM movie_list;")
for all_movies in cur:
   print (all_movies)
print
'''

#Display the movies released before 2000
print ("<<<Displaying the titles that were released before 2000>>>>>")
cur.execute("SELECT Title,Year FROM movie_list WHERE Year < 2000;") # displays all the contents of the table
for movies_before_2000 in cur:
   print (movies_before_2000)
print

#Display the contents of  movies whose runtime is < than 100 minutes
print ("<<<Displaying the titles that have running time less than 100 mins>>>>>")
cur.execute("SELECT Title,Runtime FROM movie_list WHERE Runtime < 100;") # displays all the contents of the table
for movie_with_0To100_minutes in cur:
   print (movie_with_0To100_minutes)
print

con.commit() #saving the database
con.close() #closing the database
