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
truck1.loadPackages(parsing.getPackageLength(), parsing.getPackageHT(), parsing.getAddressList())
truck2.loadPackages(parsing.getPackageLength(), parsing.getPackageHT(), parsing.getAddressList())
truck3.loadPackages(parsing.getPackageLength(), parsing.getPackageHT(), parsing.getAddressList())

#test
print("truck 1")
for package1 in truck1.getPackages():
    print(package1)

#print("truck 2")
#for package2 in truck2.getPackages():
#    print(package2)

#print("truck 3")
#for package3 in truck3.getPackages():
#   print(package3)

