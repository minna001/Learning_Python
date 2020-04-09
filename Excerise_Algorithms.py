# Create a first.txt file that reads the contents of the first 90 chars of bear.txt then writes them to new file

with open("bear.txt","r") as myfile:
    content = myfile.read()
    
with open("first.txt","w") as file:
    file.write(content[:90])
    
"""    
 You can read an existing file with Python:

with open("file.txt") as file:
    content = file.read()
You can create a new file with Python and write some text on it:

with open("file.txt", "w") as file:
    content = file.write("Sample text")
You can append text to an existing file without overwriting it:

with open("file.txt", "a") as file:
    content = file.write("More sample text")
You can both append and read a file with:

with open("file.txt", "a+") as file:
    content = file.write("Even more sample text")
    file.seek(0)
    content = file.read()
    
"""
"""   
Builtin objects are all objects that are written inside the Python interpreter in C language.

Builtin modules contain builtins objects.

Some builtin objects are not immediately available in the global namespace. They are parts of a builtin module. To use those objects the module needs to be imported first. E.g.:

import time
time.sleep(5)
A list of all builtin modules can be printed out with:

import sys
sys.builtin_module_names
Standard libraries is a jargon that includes both builtin modules written in C and also modules written in Python.

Standard libraries written in Python reside in the Python installation directory as .py files. You can find their directory path with sys.prefix.

Packages are a collection of .py modules.

Third-party libraries are packages or modules written by third-party persons (not the Python core development team).

Third-party libraries can be installed from the terminal/command line:

Windows:

pip install pandas

Mac and Linux:

pip3 install pandas
"""
"""
In the example you just saw we used the following SQL statement in our Python code:

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = 'rain'")
That statement retrieved all the rows of the Dictionary table where the value of the column Expression was rain. The string inside cursor.execute() is SQL code that Python sends to the database. That kind of language is understood by the database.

Here are some more examples of SQL queries that you can try out from within your Python script just like we did previously:

Get all rows where the value of the column Expression starts with r:

"SELECT * FROM Dictionary WHERE Expression  LIKE 'r%'"
Get all rows where the value of the column Expression starts with rain:

"SELECT * FROM Dictionary WHERE Expression  LIKE 'rain%'"
All rows where the length of the value of the column Expression is less than four characters:

"SELECT * FROM Dictionary WHERE length(Expression) < 4"
All rows where the length of the value of the column Expression is four characters:

"SELECT * FROM Dictionary WHERE length(Expression) = 4"
All rows where the length of the value of the column Expression is greater than 1 but less than 4 characters:

"SELECT * FROM Dictionary WHERE length(Expression) > 1 AND length(Expression) < 4"
All rows of column Definition where the value of the column Expression starts with r:

"SELECT Definition FROM Dictionary WHERE Expression  LIKE 'r%'"
"""
"""
from geopy.geocoders import Nominatim
nom = Nominatim()
change them to these

from geopy.geocoders import ArcGIS
nom = ArcGIS()
"""