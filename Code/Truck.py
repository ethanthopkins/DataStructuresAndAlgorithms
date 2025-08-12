class Truck:
    currentAddress = "4001 South 700 East"
    speed = 18 #miles per hour
    packages = []
    minimum = 100
    packageDistance = 1

    def loadPackages(self, htPackagesLength, hashTablePackages, addressList):
        while(len(self.packages) != 16):
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
                    packageDistance = float(self.hashTableDistance.search(currentAddressIndex)[n])
                except ValueError:
                    continue
                if (packageDistance < minimum): #if the distance is less that the minimum found, set minimum to the stiance
                    minimum = packageDistance
                    packageIndexToLoad = i + 1 

        self.packages.append(self.hashTablePackages.search(packageIndexToLoad))  
        tempAddress = self.hashTablePackages.search(packageIndexToLoad)  
        currentAddress = tempAddress.address
        self.hashTablePackages.remove(packageIndexToLoad)
        i = 0
        j = 0
        minimum = 100
    def getPackages(self):
        return self.packages