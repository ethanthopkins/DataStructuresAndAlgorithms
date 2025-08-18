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
truck1 = Truck()
truck2 = Truck()
truck3 = Truck()

#load trucks
truck1.loadPackages(parsing.getPackageLength(), parsing.getPackageHT(), parsing.getDistanceHT(), parsing.getAddressList())
truck2.loadPackages(parsing.getPackageLength(), parsing.getPackageHT(), parsing.getDistanceHT(), parsing.getAddressList())
truck3.loadPackages(parsing.getPackageLength(), parsing.getPackageHT(), parsing.getDistanceHT(), parsing.getAddressList())

#test
print("truck 1")
for element1 in truck1.getPackages():
    print(element1[0].getAddress() + " TIME: " + str(element1[1].time()))
print("")
print("truck 2")
for element2 in truck2.getPackages():
    print(element2[0].getAddress() + " TIME: " + str(element2[1].time()))
print("")
print("truck 3")
for element3 in truck3.getPackages():
    print(element3[0].getAddress() + " TIME: " + str(element3[1].time()))

