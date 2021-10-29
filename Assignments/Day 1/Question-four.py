# 4. Write a Python program to read a given CSV file as a dictionary. Feel free to read 
# any CSV of your choice.

import csv
myfile = csv.DictReader(open("../../Sample100.csv", "r"))
print(list(myfile))

