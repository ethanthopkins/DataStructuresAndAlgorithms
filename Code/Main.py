#Ethan, Hopkins, 005830284

from Package import Package
from Truck import Truck
from Parsing import Parsing
from datetime import datetime, time

class Main:
    def __init__(self):
        #parse data
        self.parsing = Parsing()
        self.parsing.parsePackages()
        self.parsing.parseDistance()
        self.parsing.parseAddresses()

        #declare trucks
        self.truck1 = Truck(1, datetime.combine(datetime.today(), time(hour = 8)))
        self.truck2 = Truck(2, datetime.combine(datetime.today(), time(hour = 8)))
        self.truck3 = Truck(3, datetime.combine(datetime.today(), time(hour = 8)))

        #load trucks
        self.truck1.loadPackages(self.parsing.getPackageLength(), self.parsing.getPackageHT(), self.parsing.getDistanceHT(), self.parsing.getAddressList())
        self.truck3.loadPackages(self.parsing.getPackageLength(), self.parsing.getPackageHT(), self.parsing.getDistanceHT(), self.parsing.getAddressList()) #load 3 first to ensure the packages that can only be on 2 get loaded
        self.truck2.setCurrentTime(self.truck1.getCurrentTime())
        self.truck2.loadPackages(self.parsing.getPackageLength(), self.parsing.getPackageHT(), self.parsing.getDistanceHT(), self.parsing.getAddressList())

    def makeAddressCorrect(self, package, bool):
        if (bool):
            package.setAddress("410 S State St")
            package.setCity("Salt Lake City")
            package.setState("UT")
            package.setZip(84111)  
        else:
            package.setAddress("300 State St")
            package.setCity("Salt Lake City")
            package.setState("UT")
            package.setZip(84103)          
    def totalMileage(self):
        print("Truck 1 Total Mileage: ", self.truck1.getTotalMileage())
        print("Truck 2 Total Mileage: ", self.truck2.getTotalMileage())
        print("Truck 3 Total Mileage: ", self.truck3.getTotalMileage())
    def taskG(self):
        hoursInput = int(input("Input the start hours: "))
        minutesInput = int(input("Input the start minutes: "))

        checkTime = time(hoursInput, minutesInput)

        #status of packages between time
        comp1 = []
        comp2 = []
        comp3 = []
        packageTimeCheck = datetime.combine(datetime.today(), checkTime) 

    #Task G (compare times)
        for package1 in self.truck1.getPackages():
            if (package1[0].getPackageID() != 0):
                #this handles the exception for package 9
                if (package1[0].getPackageID() == 9): 
                    if (packageTimeCheck <= datetime.combine(datetime.today(), time(10, 20))):
                        self.makeAddressCorrect(package1[0], False)
                        comp1.append(["Delayed", package1])
                        continue
                    else:
                        self.makeAddressCorrect(package1[0], True)                
                if (package1[1] <= packageTimeCheck):
                    comp1.append(["Delivered", package1])
                else: 
                    comp1.append(["En Route", package1])
        for package2 in self.truck2.getPackages():
            if (packageTimeCheck <= datetime.combine(datetime.today(), time(9, 5))):
                if (package2[0].getPackageID() in [6, 25, 28, 32]):
                    comp1.append(["Delayed", package2])
                    continue
            if (package2[0].getPackageID() != 0):
                comp1.append(["At the hub", package2])
        for package3 in self.truck3.getPackages():
            if (package3[0].getPackageID() != 0):
                if (package3[1] <= packageTimeCheck):
                    comp1.append(["Delivered", package3])
                else: comp1.append(["En Route", package3])
        
        print("Package Status ")
        for index1, status1 in enumerate(comp1):
            print("Count: ", index1, end=" ")
            if (status1[0] == "Delivered"):
                print("Status: ", status1[0], ": ", status1[1][1].time(), end=" ")
            else:
                print("Status: ", status1[0], end=" ")    
            print("Truck ID: ", status1[1][0].getTruckID(),
                "PACKAGE ID:", status1[1][0].getPackageID(), 
                "ADDRESS:", status1[1][0].getAddress(), 
                "CITY:", status1[1][0].getCity(),
                "STATE:", status1[1][0].getState(),
                "ZIP", status1[1][0].getZip(),
                "DELIVERY DEADLINE:", status1[1][0].getDeliveryDeadline(),
                "SKILO:", status1[1][0].getSKilo(),
                "NOTES:", status1[1][0].getNotes())
main = Main()
main.totalMileage()
#main.taskG()            