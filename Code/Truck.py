from MyHashTable import MyHashTable
from datetime import datetime, time, timedelta

class Truck:
    speed = 18 #miles per hour
    minutesInHour = 60
    currentTime = datetime.combine(datetime.today(), time(hour = 8))
    def __init__(self):
        self.currentAddress = "4001 South 700 East"
        self.packages = []
        self.packagesLoaded = 0
        self.minimum = 100
        self.packageDistance = 1
    def loadPackages(self, htPackagesLength, hashTablePackages, hashTableDistance, addressList):
            #if the truck is not full and there are still packages to load
            while((self.packagesLoaded != 16) and (not hashTablePackages.isEmpty())):
                #iterate through all packages.
                for i in range(htPackagesLength):
                    try:
                        packageAddress = hashTablePackages.search(i + 1).address
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
                timeTraveledTemp = (self.packageDistance / Truck.speed) * Truck.minutesInHour
                hoursTraveled = int(timeTraveledTemp // 60)
                minutesTraveled = int(timeTraveledTemp % 60)
                timeTraveled = timedelta(hours = hoursTraveled, minutes = minutesTraveled)
                self.currentTime = self.currentTime + timeTraveled
                self.packages.append([hashTablePackages.search(packageIndexToLoad), self.currentTime]) #load the package with the shortest distance into the truck. 
                self.packagesLoaded += 1
                #reset all the looping variables so it can accurately pull the indices of the addresses
                i = 0
                j = 0
                self.minimum = 100
                tempPackageObject = hashTablePackages.search(packageIndexToLoad)
                self.currentAddress = tempPackageObject.getAddress()
                #remove the package so it is not found again
                hashTablePackages.remove(packageIndexToLoad)
    def getPackages(self):
        return self.packages