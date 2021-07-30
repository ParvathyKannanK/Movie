import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Qwerty@007", database = "MovieRecord")

mycursor = mydb.cursor()

#mycursor.execute("INSERT INTO moviedata (MovieName, Actor, Actress, Yr, Director) VALUES('Maze Runner','Dylan OBrien','Kaya Scodelario', 2014,'Wes Bell')")
#mycursor.execute("INSERT INTO moviedata (MovieName , Actor, Actress, Yr, Director) VALUES('The Ghazi Attack','Rana Daggubati','Taapsee Pannu', 2017,'Sankalp Reddy')")
#mycursor.execute("INSERT INTO moviedata (MovieName , Actor, Actress, Yr, Director) VALUES('Anegan','Dhanush','Amyra Dastur', 2015,'K. V. Anand')")
#mydb.commit()

#mycursor.execute("SELECT * FROM moviedata")

mycursor.execute("SELECT * FROM moviedata WHERE Actor='Dhanush'")



for i in mycursor:
  print(i)

