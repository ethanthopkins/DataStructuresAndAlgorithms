from Package import Package
from MyHashTable import MyHashTable
import csv

#declare hashtable
hashTable = MyHashTable()

#parse packages csv
with open('Materials/package_list.csv') as packageListCSV:
    readerPackage = csv.reader(packageListCSV)
    for index, row in enumerate(readerPackage):
        instance = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        hashTable.insert(index + 1, instance)

#parse distance csv
with open('Materials/distance_table') as distanceListCSV:
    readerDistance = csv.reader(distanceListCSV)
    for row in readerDistance:
        

#print(hashTable.search(6).notes)

#for bucket in hashTable.table:
#    for key, value in bucket:
#        print(f"Key: {key}, Package ID: {value.packageID}")

#package1 = Package(1, "195 W Oakland Ave", "Salt Lake City", "UT", 84115, "10:30AM", 21, "")
#hashTable.insert(1, package1)



