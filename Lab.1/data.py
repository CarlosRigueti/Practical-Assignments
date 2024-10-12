import csv

FILENAME= "data.csv"
DATADIR = “../Lab.1/”


with open (DATADIR + FILENAME, "rt") as fp:
reader = csv.reader(fp, delimiter=",")
for line in reader:
print (line)