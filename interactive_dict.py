import json
import os
import time
from difflib import get_close_matches

data = json.load(open("original.json"))
def read_key(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]    
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(w,data.keys())[0])
        if yn == "Y" or yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N" or yn == "n":
            return "The word doesn't exist please double check your spelling." 
        else:
            return "We Didn't understand your Entry."    
    else:
        return "item does not exist try"
    
        
        #search = input("what word do you want to know the definition of: ")
        


word = input("enter word: ")
output = read_key(word)
print(read_key(word))
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)





