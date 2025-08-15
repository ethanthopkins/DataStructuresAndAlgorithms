class Truck:
    def __init__(self):
        self.currentAddress = "4001 South 700 East"
        self.speed = 18 #miles per hour
        self.packages = []
        self.minimum = 100
        self.packageDistance = 1

    def loadPackages(self, htPackagesLength, hashTablePackages, hashTableDistance, addressList):
            while((len(self.packages) != 16) and (not hashTablePackages.isEmpty())):
                for i in range(htPackagesLength):
                    try:
                        packageAddress = hashTablePackages.search(i + 1).address
                    except AttributeError:
                        continue
                    for j, each in enumerate(addressList):
                        if (each == self.currentAddress):
                            currentAddressIndex = j
                            break
                    for n, each in enumerate(addressList):
                        if (each == packageAddress):
                            destinationPackage = n
                            break  
                    try:
                        self.packageDistance = float(hashTableDistance.search(currentAddressIndex)[destinationPackage])
                    except ValueError:
                        continue
                    if (self.packageDistance < self.minimum): #if the distance is less that the minimum found, set minimum to the stiance
                        self.minimum = self.packageDistance
                        packageIndexToLoad = i + 1 
                self.packages.append(hashTablePackages.search(packageIndexToLoad)) 
                i = 0
                j = 0
                self.minimum = 100
                tempPackageObject = hashTablePackages.search(packageIndexToLoad)
                self.currentAddress = tempPackageObject.getAddress()
                hashTablePackages.remove(packageIndexToLoad)

    def getPackages(self):
        return self.packages