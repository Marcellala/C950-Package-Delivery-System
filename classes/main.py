# Marcey Dunbar 001270715

import csv
from classes.hashtable import ChainingHashTable
from classes.package import Package


# function to load package data from csv and insert into hash table
def loadPackageData(fileName):
    with open(fileName) as Package_File:
        packageData = csv.reader(Package_File, delimiter=",")
        # next(packageData)
        for package in packageData:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZipcode = package[4]
            p_delivery_deadline = package[5]
            pMass = package[6]
            pNotes = package[7]

            # Package object
            p = Package(pID, pAddress, pCity, pState, pZipcode, p_delivery_deadline, pMass, pNotes)

            # insert into hash table
            myHash.insert(pID, p)


# hash table instance - O(1)
myHash = ChainingHashTable()

# load package data to Hash Table
loadPackageData('Package_File.csv')

# get data from hash table and display  - O(n)
#for i in range(1, 40):
    #print("key: {} and Package: {}".format(i + 1, myHash.lookup(i + 1)))

# creates a 2d array to load distance table data. Distance data is hardcoded into program
distance_Table = [
    [0.0, 7.2, 3.8, 11.0, 2.2, 3.5, 10.9, 8.6, 7.6, 2.8, 6.4, 3.2, 7.6, 5.2, 4.4, 3.7, 7.6, 2.0, 3.6, 6.5, 1.9, 3.4,
     2.4, 6.4, 2.4, 5.0, 3.6],
    [7.2, 0.0, 7.1, 6.4, 6.0, 4.8, 1.6, 2.8, 4.8, 6.3, 7.3, 5.3, 4.8, 3.0, 4.6, 4.5, 7.4, 6.0, 5.0, 4.8, 9.5, 10.9,
     8.3, 6.9, 10.0, 4.4, 13.0],
    [3.8, 7.1, 0.0, 9.2, 4.4, 2.8, 8.6, 6.3, 5.3, 1.3, 10.4, 3.0, 5.3, 6.5, 5.6, 5.8, 5.7, 4.1, 3.6, 4.3, 3.3, 5.0,
     6.1, 9.7, 6.1, 2.8, 7.4],
    [11.0, 6.4, 9.2, 0.0, 5.6, 6.9, 8.6, 4.0, 11.1, 7.3, 1.0, 6.4, 11.1, 3.9, 4.3, 4.4, 7.2, 5.3, 6.0, 10.6, 5.9, 7.4,
     4.7, 0.6, 6.4, 10.1, 10.1],
    [2.2, 6.0, 4.4, 5.6, 0.0, 1.9, 7.9, 5.1, 7.5, 2.6, 6.5, 1.5, 7.5, 3.2, 2.4, 2.7, 1.4, 0.5, 1.7, 6.5, 3.2, 5.2, 2.5,
     6.0, 4.2, 5.4, 5.5],
    [3.5, 4.8, 2.8, 6.9, 1.9, 0.0, 6.3, 4.3, 4.5, 1.5, 8.7, 0.8, 4.5, 3.9, 3.0, 3.8, 5.7, 1.9, 1.1, 3.5, 4.9, 6.9, 4.2,
     9.0, 5.9, 3.5, 7.2],
    [10.9, 1.6, 8.6, 8.6, 7.9, 6.3, 0.0, 4.0, 4.2, 8.0, 8.6, 6.9, 4.2, 4.2, 8.0, 5.8, 7.2, 7.7, 6.6, 3.2, 11.2, 12.7,
     10.0, 8.2, 11.7, 5.1, 14.2],
    [8.6, 2.8, 6.3, 4.0, 5.1, 4.3, 4.0, 0.0, 7.7, 9.3, 4.6, 4.8, 7.7, 1.6, 3.3, 3.4, 3.1, 5.1, 4.6, 6.7, 8.1, 10.4, 7.8,
     4.2, 9.5, 6.2, 10.7],
    [7.6, 4.8, 5.3, 11.1, 7.5, 4.5, 4.2, 7.7, 0.0, 4.8, 11.9, 4.7, 0.6, 7.6, 7.8, 6.6, 7.2, 5.9, 5.4, 1.0, 8.5, 10.3,
     7.8, 11.5, 9.5, 2.8, 14.1],
    [2.8, 6.3, 1.6, 7.3, 2.6, 1.5, 8.0, 9.3, 4.8, 0.0, 9.4, 1.1, 5.1, 4.6, 3.7, 4.0, 6.7, 2.3, 1.8, 4.1, 3.8, 5.8, 4.3,
     7.8, 4.8, 3.2, 6.0],
    [6.4, 7.3, 10.4, 1.0, 6.5, 8.7, 8.6, 4.6, 11.9, 9.4, 0.0, 7.3, 12.0, 4.9, 5.2, 5.4, 8.1, 6.2, 6.9, 11.5, 6.9, 8.3,
     4.1, 0.4, 4.9, 11.0, 6.8],
    [3.2, 5.3, 3.0, 6.4, 1.5, 0.8, 6.9, 4.8, 4.7, 1.1, 7.3, 0.0, 4.7, 3.5, 2.6, 2.9, 6.3, 1.2, 1.0, 3.7, 4.1, 6.2, 3.4,
     6.9, 5.2, 3.7, 6.4],
    [7.6, 4.8, 5.3, 11.1, 7.5, 4.5, 4.2, 7.7, 0.6, 5.1, 12.0, 4.7, 0.0, 7.3, 7.8, 6.6, 7.2, 5.9, 5.4, 1.0, 8.5, 10.3,
     7.8, 11.5, 9.5, 2.8, 14.1],
    [5.2, 3.0, 6.5, 3.9, 3.2, 3.9, 4.2, 1.6, 7.6, 4.6, 4.9, 3.5, 7.3, 0.0, 1.3, 1.5, 4.0, 3.2, 3.0, 6.9, 6.2, 8.2, 5.5,
     4.4, 7.2, 6.4, 10.5],
    [4.4, 4.6, 5.6, 4.3, 2.4, 3.0, 8.0, 3.3, 7.8, 3.7, 5.2, 2.6, 7.8, 1.3, 0.0, 0.6, 6.4, 2.4, 2.2, 6.8, 5.3, 7.4, 4.6,
     4.8, 6.3, 6.5, 8.8],
    [3.7, 4.5, 5.8, 4.4, 2.7, 3.8, 5.8, 3.4, 6.6, 4.0, 5.4, 2.9, 6.6, 1.5, 0.6, 0.0, 5.6, 1.6, 1.7, 6.4, 4.9, 6.9, 4.2,
     5.6, 5.9, 5.7, 8.4],
    [7.6, 7.4, 5.7, 7.2, 1.4, 5.7, 7.2, 3.1, 7.2, 6.7, 8.1, 6.3, 7.2, 4.0, 6.4, 5.6, 0.0, 7.1, 6.1, 7.2, 10.6, 12.0,
     9.4, 7.5, 11.1, 6.2, 13.6],
    [2.0, 6.0, 4.1, 5.3, 0.5, 1.9, 7.7, 5.1, 5.9, 2.3, 6.2, 1.2, 5.9, 3.2, 2.4, 1.6, 7.1, 0.0, 1.6, 4.9, 3.0, 5.0, 2.3,
     5.5, 4.0, 5.1, 5.2],
    [3.6, 5.0, 3.6, 6.0, 1.7, 1.1, 6.6, 4.6, 5.4, 1.8, 6.9, 1.0, 5.4, 3.0, 2.2, 1.7, 6.1, 1.6, 0.0, 4.4, 4.6, 6.6, 3.9,
     6.5, 5.6, 4.3, 6.9],
    [6.5, 4.8, 4.3, 10.6, 6.5, 3.5, 3.2, 6.7, 1.0, 4.1, 11.5, 3.7, 1.0, 6.9, 6.8, 6.4, 7.2, 4.9, 4.4, 0.0, 7.5, 9.3,
     6.8, 11.4, 8.5, 1.8, 13.1],
    [1.9, 9.5, 3.3, 5.9, 3.2, 4.9, 11.2, 8.1, 8.5, 3.8, 6.9, 4.1, 8.5, 6.2, 5.3, 4.9, 10.6, 3.0, 4.6, 7.5, 0.0, 2.0,
     2.9, 6.4, 2.8, 6.0, 4.1],
    [3.4, 10.9, 5.0, 7.4, 5.2, 6.9, 12.7, 10.4, 10.3, 5.8, 8.3, 6.2, 10.3, 8.2, 7.4, 6.9, 12.0, 5.0, 6.6, 9.3, 2.0, 0.0,
     4.4, 7.9, 3.4, 7.9, 4.7],
    [2.4, 8.3, 6.1, 4.7, 2.5, 4.2, 10.0, 7.8, 7.8, 4.3, 4.1, 3.4, 7.8, 5.5, 4.6, 4.2, 9.4, 2.3, 3.9, 6.8, 2.9, 4.4, 0.0,
     4.5, 1.7, 6.8, 3.1],
    [6.4, 6.9, 9.7, 0.6, 6.0, 9.0, 8.2, 4.2, 11.5, 7.8, 0.4, 6.9, 11.5, 4.4, 4.8, 5.6, 7.5, 5.5, 6.5, 11.4, 6.4, 7.9,
     4.5, 0.0, 5.4, 10.6, 7.8],
    [2.4, 10.0, 6.1, 6.4, 4.2, 5.9, 11.7, 9.5, 9.5, 4.8, 4.9, 5.2, 9.5, 7.2, 6.3, 5.9, 11.1, 4.0, 5.6, 8.5, 2.8, 3.4,
     1.7, 5.4, 0.0, 7.0, 1.3],
    [5.0, 4.4, 2.8, 10.1, 5.4, 3.5, 5.1, 6.2, 2.8, 3.2, 11.0, 3.7, 2.8, 6.4, 6.5, 5.7, 6.2, 5.1, 4.3, 1.8, 6.0, 7.9,
     6.8, 10.6, 7.0, 0.0, 8.3],
    [3.6, 13.0, 7.4, 10.1, 5.5, 7.2, 14.2, 10.7, 14.1, 6.0, 6.8, 6.4, 14.1, 10.5, 8.8, 8.4, 13.6, 5.2, 6.9, 13.1, 4.1,
     4.7, 3.1, 7.8, 1.3, 8.3, 0.0],
]

# address dictionary to store address information
address_table = {
    '4001 South 700 East': 0,
    '1060 Dalton Ave S': 1,
    '1330 2100 S': 2,
    '1488 4800 S': 3,
    '177 W Price Ave': 4,
    '195 W Oakland Ave': 5,
    '2010 W 500 S': 6,
    '2300 Parkway Blvd': 7,
    '233 Canyon Rd': 8,
    '2530 S 500 E': 9,
    '2600 Taylorsville Blvd': 10,
    '2835 Main St': 11,
    '300 State St': 12,
    '3060 Lester St': 13,
    '3148 S 1100 W': 14,
    '3365 S 900 W': 15,
    '3575 W Valley Central Sta bus Loop': 16,
    '3595 Main St': 17,
    '380 W 2880 S': 18,
    '410 S State St': 19,
    '4300 S 1300 E': 20,
    '4580 S 2300 E': 21,
    '5025 State St': 22,
    '5100 South 2700 West': 23,
    '5383 South 900 East #104': 24,
    '600 E 900 South': 25,
    '6351 South 900 East': 26
}


# distance lookup function that returns the distance between current position and destination - O(1)
def distance_lookup(source_address, destination_address):
    row = address_table[source_address]
    col = address_table[destination_address]
    distance = distance_Table[row][col]

    return float(distance)


# manually add the packages to each truck

truck1 = [1, 13, 14, 15, 16, 19, 20, 27, 29, 30, 31, 34, 35, 37, 40]
truck2 = [3, 6, 10, 17, 18, 25, 28, 32, 33, 36, 38, 39, 2, 5, 26]
truck3 = [4, 9, 8, 7, 11, 12, 21, 22, 23, 24]

# delivery algorithm for truck 1
truck_address = '4001 South 700 East'
roundtrip = []
truck_time = 8.0  # start time

# set all packages to leave at 8:00am - o(n)
for i in truck1:
    package = myHash.lookup(i)
    package.time_left_hub = 8.0

# loop until truck 1 list is empty (outer loop)
# Time Complexity - O(N^2)
# space Complexity - O(N)
while len(truck1) != 0:
    min_distance = 999
    min_package_id = None
    # nearest neighbor search
    for i in truck1:
        package = myHash.lookup(i)
        distance = distance_lookup(truck_address, package.address)
        if distance < min_distance:
            min_distance = distance
            min_package_id = i

    # calculate delivery time and change the status of the package
    time_traveled = min_distance / 18.0
    truck_time = truck_time + time_traveled
    myHash.lookup(min_package_id).delivery_timestamp = truck_time

    # remove package from list (truck1)
    truck1.remove(min_package_id)
    # add mileage to roundtrip distance

    roundtrip.append(min_distance)
    total_distance = sum(roundtrip)

    # change truck address to min package address
    truck_address = myHash.lookup(min_package_id).address

# print(total_distance)

# delivery algorithm for truck 2
# Time Complexity - O(N^2)
# space Complexity - O(N)
truck_address = '4001 South 700 East'
roundtrip2 = []
truck_time = 9.083  # start time
# set all packages to leave at 9:05am - o(n)
for i in truck2:
    package = myHash.lookup(i)
    package.time_left_hub = 9.083

# loop until truck 2 list is empty (outer loop)
while len(truck2) != 0:
    min_distance = 999
    min_package_id = None
    # nearest neighbor search
    for i in truck2:
        package = myHash.lookup(i)
        distance = distance_lookup(truck_address, package.address)
        if distance < min_distance:
            min_distance = distance
            min_package_id = i

    # calculate delivery time and change the status of the package
    time_traveled = min_distance / 18.0
    truck_time = truck_time + time_traveled
    myHash.lookup(min_package_id).delivery_timestamp = truck_time

    # remove package from list (truck1)
    truck2.remove(min_package_id)
    # add mileage to roundtrip distance

    roundtrip2.append(min_distance)
    total_distance2 = sum(roundtrip2)

    # change truck address to min package address
    truck_address = myHash.lookup(min_package_id).address
# print(total_distance2)

# delivery algorithm for truck 3
# Time Complexity- O(N^2)
# space Complexity - O(N)
truck_address = '4001 South 700 East'
roundtrip3 = []
truck_time = 10.333
# set all packages to leave at 10:20am - o(n)
for i in truck3:
    package = myHash.lookup(i)
    package.time_left_hub = 10.333
# loop until truck 3 list is empty (outer loop)
while len(truck3) != 0:
    min_distance = 999
    min_package_id = None
    # nearest neighbor search
    for i in truck3:
        package = myHash.lookup(i)
        distance = distance_lookup(truck_address, package.address)
        if distance < min_distance:
            min_distance = distance
            min_package_id = i

    # calculate delivery time and change the status of the package
    time_traveled = min_distance / 18.0
    truck_time = truck_time + time_traveled
    myHash.lookup(min_package_id).delivery_timestamp = truck_time

    # remove package from list (truck1)
    truck3.remove(min_package_id)
    # add mileage to roundtrip distance

    roundtrip3.append(min_distance)
    total_distance3 = sum(roundtrip3)

    # change truck address to min package address
    truck_address = myHash.lookup(min_package_id).address
# print(total_distance3)

# add total distance of all trucks to get total mileage. Print to user - 0(1)
total_mileage = (total_distance + total_distance2 + total_distance3)
print("Total Mileage for All Trucks: ")
print(total_mileage)

# UI for program
# get time from user and convert to pseudotime

user_selection = int(input("Press 1 to see the status of all packages at a given time"
                           " or press 2 to see a specific package by ID: "))
if user_selection == 1:
    user_hour = int(input("Please enter a time in hours: "))
    user_minutes = int(input("Please enter a time in minutes: "))
    total_time = user_hour + user_minutes/60.0
    # test to confirm pseudotime is converting
    # print(f'You entered:  {total_time}')

    # print all packages at time
    for i in range(1,41):
        package = myHash.lookup(i)
        print("key: {} and Package: {}".format(i, myHash.lookup(i)))
        if package.delivery_timestamp < total_time:
            print("Delivered")
        elif package.time_left_hub > total_time:
            print("at hub")
        else:
            print("En route")
elif user_selection == 2:
    user_package = int(input("Please enter a package number 1-40: "))
    package = myHash.lookup(user_package)
    print("key: {} and Package: {}".format(user_package, myHash.lookup(user_package)))
else:
     print("Not a valid option")


# testing for hash table
# print(myHash.table)

# unit test for distance lookup
# print(distance_lookup('2530 S 500 E', '177 W Price Ave'))

# print(distance_Table[26])
