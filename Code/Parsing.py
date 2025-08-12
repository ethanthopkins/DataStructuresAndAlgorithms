from Package import Package
from Truck import Truck
from MyHashTable import MyHashTable
import csv

class Parsing:
    hashTablePackages = MyHashTable(40)
    hashTableDistance = MyHashTable(28)
    addressList = list()
    htPackagesLength = 0

    def parsePackages(self):
            #parse packages csv
            with open('Materials/package_list.csv') as packageListCSV:
                readerPackage = csv.reader(packageListCSV)
                for k, row in enumerate(readerPackage):
                    instance = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    self.hashTablePackages.insert(k + 1, instance)
                    htPackagesLength = k + 1
    def parseDistance(self):
        #get distances in a hashmap
        with open('Materials/distance_table.csv') as distanceListCSV: 
            readerDistance = csv.reader(distanceListCSV)
            next(readerDistance)
            rows = list(readerDistance)
            columns = list(zip(*rows))
            for m, each in enumerate(columns):
                self.hashTableDistance.insert(m, columns[m])  
                htDistanceLength = m
    def parseAddresses(self):
        with open('Materials/distance_table.csv') as distanceListCSV:
            readerDistance = csv.reader(distanceListCSV)
            self.addressList = list(readerDistance)[0]
    def getPackageHT(self):
         return self.hashTablePackages
    def getDistanceHT(self):
         return self.hashTableDistance
    def getAddressList(self):
         return self.addressList
    def getPackageLength(self):
         return self.htPackagesLength
