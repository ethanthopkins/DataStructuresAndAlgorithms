class Package:
    packageID = 0
    address = ""
    city = ""
    state = ""
    zip = 0
    deliveryDeadline = ""
    sKilo = 0
    notes = ""

    def __init__(self, packageID, address, city, state, zip, deliveryDeadline, sKilo, notes):
        self.packageID = int(packageID)
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deliveryDeadline = deliveryDeadline
        self.sKilo = sKilo
        self.notes = notes
        self.onlyTruck2 = False
        self.delayed = False
        self.together = False
        self.deadline = False
        self.checkConditions()
    def checkConditions(self):
        if "truck 2" in self.notes:
            self.onlyTruck2 = True
        if "Delayed" in self.notes:
            self.delayed = True
        togetherPackages = [13, 14, 15, 16, 19, 20]
        if (self.packageID in togetherPackages):
            self.together = True
        deadlinePackages = [1, 6, 13, 14, 15, 16, 20, 25, 29, 30, 31, 34, 37, 40]
        if (self.packageID in deadlinePackages): 
            self.deadline = True
    def getOnlyTruck2(self):
        return self.onlyTruck2
    def getPackageID(self):
        return self.packageID
    def getAddress(self):
        return self.address
    def getCity(self):
        return self.city
    def getState(self):
        return self.state
    def getZip(self):
        return self.zip
    def getDeliveryDeadline(self):
        return self.deliveryDeadline
    def getSKilo(self):
        return self.sKilo
    def getNotes(self):
        return self.notes
    def setAddress(self, newAddress):
        self.address = newAddress
    def setCity(self, city):
        self.city = city
    def setState(self, state):
        self.state = state
    def setZip(self, zip):
        self.zip = zip
    def getDelayed(self):
        return self.delayed
    def getTogetherStatus(self):
        return self.together
    def getDeadlineStatus(self):
        return self.deadline
