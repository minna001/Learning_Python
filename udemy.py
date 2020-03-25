# with open("veggies.txt","a+") as myfile:
#     myfile.write("\nOkra")
#     myfile.seek(0)
#     content = myfile.read()

# print(content)


import time
import os
import pandas

while True:
    if os.path.exists("C:/Users/mikem/pythonTest/original.csv"):
        data = pandas.read_csv("C:/Users/mikem/pythonTest/original.csv")
        print(data.mean()["st1"])
    else:
        print("File does not exist.")
        
    time.sleep(10)





