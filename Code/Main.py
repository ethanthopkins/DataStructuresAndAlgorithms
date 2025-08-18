#Ethan, Hopkins, 005830284

from Package import Package
from Truck import Truck
from Parsing import Parsing

#parse data
parsing = Parsing()
parsing.parsePackages()
parsing.parseDistance()
parsing.parseAddresses()

#declare trucks
truck1 = Truck(1)
truck2 = Truck(2)
truck3 = Truck(3)

#load trucks
truck1.loadPackages(parsing.getPackageLength(), parsing.getPackageHT(), parsing.getDistanceHT(), parsing.getAddressList())
truck3.loadPackages(parsing.getPackageLength(), parsing.getPackageHT(), parsing.getDistanceHT(), parsing.getAddressList()) #load 3 first to ensure the packages that can only be on 2 get loaded
truck2.loadPackages(parsing.getPackageLength(), parsing.getPackageHT(), parsing.getDistanceHT(), parsing.getAddressList())

#test
print("truck 1: " + str(truck1.totalMileage))
for element1 in truck1.getPackages():
    print("ID: " + str(element1[0].getPackageID()) + " Address: " + element1[0].getAddress() + " TIME: " + str(element1[1].time()))
print("")
print("truck 2: " + str(truck2.totalMileage))
for element2 in truck2.getPackages():
    print("ID: " + str(element2[0].getPackageID()) + " Address: " + element2[0].getAddress() + " TIME: " + str(element2[1].time()))
print("")
print("truck 3: " + str(truck3.totalMileage))
for element3 in truck3.getPackages():    
    print("ID: " + str(element3[0].getPackageID()) + " Address: " + element3[0].getAddress() + " TIME: " + str(element3[1].time()))

