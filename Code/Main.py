from Package import Package
from MyHashTable import MyHashTable
import csv

#parse csv
with open('../Materials/package_list.csv') as packageListCSV:
    readerOBJ = csv.reader(packageListCSV)
    for row in readerOBJ:
        print(row)

package1 = Package(1, "195 W Oakland Ave", "Salt Lake City", "UT", 84115, "10:30AM", 21, "")
hashTable = MyHashTable()
hashTable.insert(1, package1)
print(hashTable.search(1).address)


