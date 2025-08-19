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
                    #if the truck is 3 then load 15 first. It has an early delivery deadline
                    try:
                        if ((hashTablePackages.search(15) is not None) and (self.id == 3)):
                            currentAddressIndex = self.getAddressIndex(self.currentAddress, addressList) #find the index of the current address
                            destinationPackage = self.getAddressIndex(hashTablePackages.search(15).getAddress(), addressList) #find the index of the current destination package
                            packageIndexToLoad = 15
                            break
                    except AttributeError:
                        continue
                    try:
                        package = hashTablePackages.search(i + 1)
                        packageAddress = package.address
                        #if the package can only be on truck 2 or is delayed skip it
                        if (self.id != 2):
                            if (package.getOnlyTruck2()):
                                continue
                            if (package.getDelayed()):
                                continue
                        #if the package has to be delivered with other packages throw it on truck 3
                        if (self.id == 1):
                            if (not package.getTogetherStatus()):
                                if (package.getDeadlineStatus()):
                                    currentAddressIndex = self.getAddressIndex(self.currentAddress, addressList) #find the index of the current address
                                    destinationPackage = self.getAddressIndex(packageAddress, addressList) #find the index of the current destination package
                                    packageIndexToLoad = i + 1
                                    break
                        if (self.id != 3):
                            if (package.getTogetherStatus()):
                                continue
                        #deliver the packages with deadlines first
                        else:
                            if (package.getTogetherStatus()):
                                if (package.getDeadlineStatus()):
                                    currentAddressIndex = self.getAddressIndex(self.currentAddress, addressList) #find the index of the current address
                                    destinationPackage = self.getAddressIndex(packageAddress, addressList) #find the index of the current destination package
                                    packageIndexToLoad = i + 1
                                    break
                                currentAddressIndex = self.getAddressIndex(self.currentAddress, addressList) #find the index of the current address
                                destinationPackage = self.getAddressIndex(packageAddress, addressList) #find the index of the current destination package
                                packageIndexToLoad = i + 1
                                break
                    except AttributeError:
                        continue
                    currentAddressIndex = self.getAddressIndex(self.currentAddress, addressList) #find the index of the current address
                    destinationPackage = self.getAddressIndex(packageAddress, addressList) #find the index of the current destination package
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
    def getAddressIndex(self, address, addressList):
        for j, each in enumerate(addressList):
            if (each == address):
                currentAddressIndex = j
                break
        return j
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