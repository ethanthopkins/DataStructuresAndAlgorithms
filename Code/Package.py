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
        self.packageID = packageID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deliveryDeadline = deliveryDeadline
        self.sKilo = sKilo
        self.notes = notes
    def getPackageID(self):
        return self.packageID
    def getAddress(self):
        return self.address
