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
for i in range(htPackagesLength):
    #set temp var to string address of lsit of packages
    packageAddress = hashTablePackages.search(i + 1).address
    #iterate thru address list. 
    for j, each in enumerate(addressList):
        #if the current address is equal to the package selected
        if (each == currentAddress):
            currentAddressIndex = j
        if (each == packageAddress):
            #save the index of where the address is located in list
            #use that index to search within the hashtable to find the distance to that address
            packageDistance = float(hashTableDistance.search(currentAddressIndex)[j])
            if (packageDistance < minimum): #if the distance is less that the minimum found, set minimum to the stiance
                minimum = packageDistance
                packageIndexToLoad = i 
                truck1.packages.append(hashTablePackages.search(packageIndexToLoad))
                
#load the trucks
#check to see if the truck is full
#look at the list of packages for addresses
#see which address has the shortage distance from current location
#while(len(truck1.packages) < 16):
    