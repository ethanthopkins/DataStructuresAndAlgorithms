class Truck:
    speed = 18 #miles per hour
    packages = []
    def loadPackages(self, htPackagesLength, hashTablePackages):
        while(len(self.packages) != 16):
            for i in range(htPackagesLength):
                try:
                    packageAddress = hashTablePackages.search(i + 1).address
                except AttributeError:
                    continue
                for j, each in enumerate(addressList):
                    if (each == currentAddress):
                        currentAddressIndex = j
                        break
                for n, each in enumerate(addressList):
                    if (each == packageAddress):
                        destinationPackage = n
                        break  
                try:
                    packageDistance = float(hashTableDistance.search(currentAddressIndex)[n])
                except ValueError:
                    continue
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