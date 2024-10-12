import csv

FILENAME= "data.csv"
DATADIR = “Lab01”


with open (DATADIR + Lab01, "rt") as fp:
reader = csv.reader(fp, delimiter=",")
for line in reader:
print (line)