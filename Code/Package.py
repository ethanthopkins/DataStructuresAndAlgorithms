class Package:
    packageID = 0
    address = ""
    city = ""
    state = ""
    zip = 0
    deliveryDeadline = ""
    sKilo = 0
    notes = ""
    onlyTruck2 = False

    def __init__(self, packageID, address, city, state, zip, deliveryDeadline, sKilo, notes):
        self.packageID = packageID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deliveryDeadline = deliveryDeadline
        self.sKilo = sKilo
        self.notes = notes
        self.checkConditions()
    def checkConditions(self):
        if "truck 2" in self.notes:
            self.onlyTruck2 = True
    def getOnlyTruck2(self):
        return self.onlyTruck2
    def getPackageID(self):
        return self.packageID
    def getAddress(self):
        return self.address
    def setAddress(self, newAddress):
        self.address = newAddress
