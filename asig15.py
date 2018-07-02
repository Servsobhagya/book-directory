
# Q1- Create a database. Create the following tables:
# 1. Book
# 2. Titles
# 3. Publishers
# 4. Zipcodes
# 5. AuthorsTitles
# 6. Authors
# Refer to the diagram below

import pymysql as py

db=py.connect("localhost","root","**","library")

book='create table book(book_id char(40),title_id char(40),location char(40),grene char(40))'
titles='create table titles(title_id int,title char(40),ISBN char(40),publisher_id int,publication_year int)'
publishers='create table publishers(publishers_id int,name char(40),street_address char(40),suite_number int,zip_code_id int)'
zip_codes='create table zip_codes(zip_codes_id int,city char(40),zip_codes int)'
authors_titles='create table authors_titles(authors_titles char(40),author_titles_id int,title_id int)'
authors='create table authors(authors_id int,first_name char(40),middle_name char(40),last_name char(40))'

cursor=db.cursor()

cursor.execute("drop table book")
cursor.execute("drop table zip_codes")
cursor.execute("drop table authors_titles")
cursor.execute("drop table authors")
cursor.execute("drop table publishers")
cursor.execute("drop table titles")
print(cursor.execute("show tables"))

cursor.execute(book)
cursor.execute(titles)
cursor.execute(publishers)
cursor.execute(zip_codes)
cursor.execute(authors_titles)
cursor.execute(authors)

print(cursor.execute("show tables"))

db.close()


#Q2- Insert values in the tables.

import pymysql as py

db=py.connect("localhost","root","**","library")
cursor=db.cursor()
cursor.execute("insert into book values(001,'searching for mountain','j&k','jammu')")
cursor.execute("insert into titles values(002,'looking for hill','1005',201,2005)")
cursor.execute("insert into publishers values(203214,'nepoleon','india',201,2010)")
cursor.execute("insert into zip_codes values(20465,'ladakh',5042135)")
cursor.execute("insert into authors_titles values('201',10654,454215)")
cursor.execute("insert into authors values(6315425,'sham','null','pandey')")
cursor.execute("select * from book")
print(cursor.fetchall())
db.commit()
db.close()


#Q3- Update any values in any of the tables. Print the original and updated values.

import pymysql as py

db=py.connect("localhost","root","**","library")

cursor=db.cursor()
cursor.execute("select * from book")
show=cursor.fetchall()
print(show)
cursor.execute("update book set grene='helpful' where book_id=001 ")
cursor.execute("select * from book")
show=cursor.fetchall()
print(show)
db.commit()
db.close()
