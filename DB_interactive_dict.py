import mysql.connector
import json
import os
import time
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database")

cursor = con.cursor()

def meaning(word):
    cursor.execute("SELECT Expression FROM Dictionary")
    data = cursor.fetchall()
    data = [i[0] for i in data]
    if word.lower() in data or word.title() in data or word.upper() in data:
        cursor.execute("Select Definition From Dictionary where Expression = '%s' " % word)
        return cursor.fetchall()
    elif len(get_close_matches(word, data, cutoff = 0.8)) > 0:
        yn = input(f"Did you mean {get_close_matches(word, data)[0]}? Enter Y for yes, or N for no: ")
        if yn == 'Y':
            cursor.execute("Select Definition From Dictionary where Expression = '%s'" % get_close_matches(word,data)[0])
            return cursor.fetchall()
        elif yn == 'N':
            return "This word doesn't exist, Please double check it"
        else:
            return "You can only enter Y or N"
    else:
        return "No such word exists, Please double check it"


word = input('Enter a word: ')
output = meaning(word)
if type(output) == list:
    for item in output:
        print(item[0])
else:
    print(output)   

    
