#Ethan, Hopkins, 005830284

from Package import Package
from Truck import Truck
from Parsing import Parsing
from datetime import datetime, time

#parse data
parsing = Parsing()
parsing.parsePackages()
parsing.parseDistance()
parsing.parseAddresses()

#declare trucks
truck1 = Truck(1, datetime.combine(datetime.today(), time(hour = 8)))
truck2 = Truck(2, datetime.combine(datetime.today(), time(hour = 8)))
truck3 = Truck(3, datetime.combine(datetime.today(), time(hour = 8)))

#load trucks
truck1.loadPackages(parsing.getPackageLength(), parsing.getPackageHT(), parsing.getDistanceHT(), parsing.getAddressList())
truck3.loadPackages(parsing.getPackageLength(), parsing.getPackageHT(), parsing.getDistanceHT(), parsing.getAddressList()) #load 3 first to ensure the packages that can only be on 2 get loaded
truck2.setCurrentTime(truck1.getCurrentTime())
truck2.loadPackages(parsing.getPackageLength(), parsing.getPackageHT(), parsing.getDistanceHT(), parsing.getAddressList())

#status of packages between time
comp1 = []
comp2 = []
comp3 = []
timeCompStart1 = datetime.combine(datetime.today(), time(8, 35)) 
timeCompEnd1 = datetime.combine(datetime.today(), time(9, 25))
timeCompStart2 = datetime.combine(datetime.today(), time(9, 35))
timeCompEnd2 = datetime.combine(datetime.today(), time(10, 25))
timeCompStart3 = datetime.combine(datetime.today(), time(12, 3))
timeCompEnd3 = datetime.combine(datetime.today(), time(1, 12))

#Task G (compare times)
for package1 in truck1.getPackages():
    if ((package1[1] >= timeCompStart1) and (package1[1] <= timeCompEnd1)):
        comp1.append(package1[0])
    if ((package1[1] >= timeCompStart2) and (package1[1] <= timeCompEnd2)):
        comp2.append(package1[0])
    if ((package1[1] >= timeCompStart3) and (package1[1] <= timeCompEnd3)):
        comp3.append(package1[0])
for package2 in truck2.getPackages():
    if ((package2[1] >= timeCompStart1) and (package2[1] <= timeCompEnd1)):
        comp1.append(package1[0])
    if ((package2[1] >= timeCompStart2) and (package2[1] <= timeCompEnd2)):
        comp2.append(package1[0])
    if ((package2[1] >= timeCompStart3) and (package2[1] <= timeCompEnd3)):
        comp3.append(package2[0])
for package3 in truck3.getPackages():
    if ((package3[1] >= timeCompStart1) and (package3[1] <= timeCompEnd1)):
        comp1.append(package1[0])
    if ((package3[1] >= timeCompStart2) and (package3[1] <= timeCompEnd2)):
        comp2.append(package1[0])
    if ((package3[1] >= timeCompStart3) and (package3[1] <= timeCompEnd3)):
        comp3.append(package3[0])


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

