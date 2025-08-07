from Package import Package
from MyHashTable import MyHashTable
from Truck import Truck
import csv

#declare hashtable
hashTablePackages = MyHashTable(40)
hashTableDistance = MyHashTable(28)
truck1 = Truck()
truck2 = Truck()
truck3 = Truck()

#parse packages csv
with open('Materials/package_list.csv') as packageListCSV:
    readerPackage = csv.reader(packageListCSV)
    for index, row in enumerate(readerPackage):
        instance = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        hashTablePackages.insert(index + 1, instance)

#parse distance csv
with open('Materials/distance_table_2.csv') as distanceListCSV:
    readerDistance = csv.reader(distanceListCSV)
    rows = list(readerDistance)
    columns = list(zip(*rows))
    for index, each in enumerate(columns):
        hashTableDistance.insert(index, columns[index])   

#load the trucks



