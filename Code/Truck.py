from MyHashTable import MyHashTable
from datetime import datetime, time, timedelta
from Package import Package

class Truck:
    speed = 18 #miles per hour
    minutesInHour = 60
    secondsInMinute = 60
    def __init__(self, id, currentTime):
        self.id = id
        self.totalMileage = 0
        self.currentAddress = "4001 South 700 East"
        self.packages = []
        self.packagesLoaded = 0
        self.minimum = 100
        self.packageDistance = 1
        self.currentTime = currentTime
    def loadPackages(self, htPackagesLength, hashTablePackages, hashTableDistance, addressList):
            #if the truck is not full and there are still packages to load
            while((self.packagesLoaded != 16) and (not hashTablePackages.isEmpty())):
                #iterate through all packages.
                for i in range(htPackagesLength):
                    try:
                        package = hashTablePackages.search(i + 1)
                        packageAddress = package.address
                        #if the package can only be on truck 2 skip it
                        if ((package.getOnlyTruck2()) and (self.id != 2)):
                            continue
                    except AttributeError:
                        continue
                    #find the index of the current address
                    for j, each in enumerate(addressList):
                        if (each == self.currentAddress):
                            currentAddressIndex = j
                            break
                    #find the index of the current destination package
                    for n, each in enumerate(addressList):
                        if (each == packageAddress):
                            destinationPackage = n
                            break  
                    #get the attached distance using the index of the current address and destination address\
                    #when the addresses are parsed, it is set up to align
                    try:
                        self.packageDistance = float(hashTableDistance.search(currentAddressIndex)[destinationPackage])
                    except ValueError:
                        continue
                    #if the distance from the shortest package is shorter than the current minimum, then set the minimum to that.
                    #the minimum is set to be an arbitrarily large value so the first distance replaces the minimum. 
                    if (self.packageDistance < self.minimum): #if the distance is less that the minimum found, set minimum to the stiance
                        self.minimum = self.packageDistance
                        packageIndexToLoad = i + 1 
                self.calculateTime()
                self.packages.append([hashTablePackages.search(packageIndexToLoad), self.currentTime]) #load the package with the shortest distance into the truck. 
                self.packagesLoaded += 1
                self.totalMileage += self.packageDistance
                #reset all the looping variables so it can accurately pull the indices of the addresses
                i = 0
                j = 0
                self.minimum = 100
                tempPackageObject = hashTablePackages.search(packageIndexToLoad)
                self.currentAddress = tempPackageObject.getAddress()
                #remove the package so it is not found again
                hashTablePackages.remove(packageIndexToLoad)
            self.packageDistance = float(hashTableDistance.search(currentAddressIndex)[0])
            self.totalMileage += self.packageDistance
            self.calculateTime()
            hubHolderPackage = Package(0, "4001 South 700 East", "Salt Lake City", "Utah", 11111, "", 0, "")
            self.packages.append([hubHolderPackage, self.currentTime])
    def calculateTime(self):
        timeTraveledTemp = (self.packageDistance / Truck.speed) * Truck.minutesInHour * Truck.secondsInMinute
        hoursTraveled = int(timeTraveledTemp // (60 * 60))
        minutesTraveled = int(timeTraveledTemp // 60)
        secondsTraveled = int(timeTraveledTemp % 60)
        timeTraveled = timedelta(hours = hoursTraveled, minutes = minutesTraveled, seconds = secondsTraveled)
        self.currentTime = self.currentTime + timeTraveled
    def getPackages(self):
        return self.packages
    def getCurrentTime(self):
        return self.currentTime
    def setCurrentTime(self, currentTime):
        self.currentTime = currentTime