from Package import Package
from MyHashTable import MyHashTable
from Truck import Truck
import csv

#DECLARATIONS
#declare hashtable
hashTablePackages = MyHashTable(40)
hashTableDistance = MyHashTable(28)
#declare trucks
truck1 = Truck()
truck2 = Truck()
truck3 = Truck()
#declare loading variables
currentLocation = "4001 South 700 East"

#parse packages csv
with open('Materials/package_list.csv') as packageListCSV:
    readerPackage = csv.reader(packageListCSV)
    for index, row in enumerate(readerPackage):
        instance = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        hashTablePackages.insert(index + 1, instance)
#parse distance csv
with open('Materials/distance_table_2.csv') as distanceListCSV:
    readerDistance = csv.reader(distanceListCSV)
    next(readerDistance)
    #addressList = list(readerDistance)[1]
    rows = list(readerDistance)
    columns = list(zip(*rows))
 
    for index, each in enumerate(columns):
        hashTableDistance.insert(index, columns[index])  

#print(addressList)
#print("")
print(hashTableDistance.search(0))
#load the trucks
#check to see if the truck is full
#look at the list of packages for addresses
#see which address has the shortage distance from current location
#while(len(truck1.packages) < 16):
    