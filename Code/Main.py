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
currentAddress = "4001 South 700 East"
minimum = 100
packageDistance = 1

#parse packages csv
with open('Materials/package_list.csv') as packageListCSV:
    readerPackage = csv.reader(packageListCSV)
    for k, row in enumerate(readerPackage):
        instance = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        hashTablePackages.insert(k + 1, instance)
        htPackagesLength = k + 1
#get addresses in a list
#print(hashTablePackages.search(1).address)

with open('Materials/distance_table.csv') as distanceListCSV:
    readerDistance = csv.reader(distanceListCSV)
    addressList = list(readerDistance)[0]

#get distances in a hashmap
with open('Materials/distance_table.csv') as distanceListCSV: 
    readerDistance = csv.reader(distanceListCSV)
    next(readerDistance)
    rows = list(readerDistance)
    columns = list(zip(*rows))
    for m, each in enumerate(columns):
        hashTableDistance.insert(m, columns[m])  
        htDistanceLength = m
#core logic
while(len(truck1.packages) != 16):
    for i in range(htPackagesLength):
        try:
            packageAddress = hashTablePackages.search(i + 1).address
        except ValueError:
            continue
        for j, each in enumerate(addressList):
            if (each == currentAddress):
                currentAddressIndex = j
            if (each == packageAddress):
                packageDistance = float(hashTableDistance.search(currentAddressIndex)[j])
                if (packageDistance < minimum): #if the distance is less that the minimum found, set minimum to the stiance
                    minimum = packageDistance
                    packageIndexToLoad = i + 1 
    truck1.packages.append(hashTablePackages.search(packageIndexToLoad))  
    tempAddress = hashTablePackages.search(packageIndexToLoad)  
    currentAddress = tempAddress.address
    hashTablePackages.remove(packageIndexToLoad)
    i = 0
    j = 0
    minimum = 100

print(truck1.packages)
    