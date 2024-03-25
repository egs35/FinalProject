Providing a list and explanation of what exists in the code
1 points for each.
Maximum 5 points.
Each item should be a paragraph that reflects on the learning process and knowledge gained.
Awareness of data types and type checking.
Understanding of class and object-oriented programming principles.
Use of property decorators for data encapsulation and validation.
Use the list below to help you explore concepts you can discuss in the report reflection.md

Sqlite3
The “Sqlite3” command is seen in the first lines of code. This line of code is responsible for connecting the python code with a SQLite database. The SQLite database makes it easier to make tables, store data, and make a file with all the information in your database. One of the main attributes that make sqlite3 a useful tool for python programs is that it enables multiple database files to connect to one single database. Use of sqlite3 teaches us how to navigate databases and organize user input/
 
Initialize database   
	The command “def initialize_database():” uses the sqlite3 to connect and store all the input data in a table. After the database is initialized the names of the columns, and the type of input from users is used to create a table. All user input is put into the interactable database. This makes the data we acquire easy to organize and access. Furthermore, this allows use to utilize the learned skill of serialization,which converts the python objects created from user input to readable,organized, accessible data.

Take user input 
We defined a class add_restaurant with the following attributes: name, rating, review, price, and location. Within the class class diagram, each attribute type is specified as with an input function. Doing so, with each instance the user is asked to input each attribute value. 

Connect user input to database 
Through lines 28-35, we call the functions sqlite3.connect(), which calls the restaurant database. Through cursor.execute(), we specify the attributes within the add_restaurant class that will be columns within the database and each object will become a new row defined throughout the columns by the values the user imputed during instantiation. This is followed by commit() and close() which updates the database with each instance. 
  
Print all restaurants 
Lastly, we call a for loop used to iterate through each restaurant object within the restaurants database. With each object, the program prints the name and corresponding attributes. 

