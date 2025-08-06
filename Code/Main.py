import Package
import HashTable

class Main:
    def main():
        package1 = Package(1, "195 W Oakland Ave", "Salt Lake City", "UT", 84115, "10:30AM", 21, "")
        hashTable = HashTable()
        hashTable.insert(package1)
        print(hashTable.table)
