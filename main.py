
a = 3
b = 2

c = 3+2
print(c)
import csv

with open("data.csv","r",encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


print("hallo")
