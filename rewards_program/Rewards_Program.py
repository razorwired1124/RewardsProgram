purchases = [["Bob", "3March", 87],
            ["Bob", "3March", 65],
            ["Bob", "4April", 872],
            ["Bob", "5May", 671],
            ["Bill", "3March", 3],
            ["Bill", "4April", 9],
            ["Bill", "4April", 120],
            ["Bill", "5May", 111],
            ["Joe", "3March", 225],
            ["Joe", "4April", 104],
            ["Joe", "5May", 21],
            ["Joe", "5May", 92]]

def take_second(elem):
    return elem[1]

purchases.sort(key=take_second)



print("| Name  | Date     | Purchase Amount | ")

for item in purchases:
    print("|", item[0], " "*(4-len(item[0])),
          "|", item[1], " "*(7-len(item[1])),
          "|", item[2], " "*(14-len(str(item[2]))),
          "|")

print("")

print("")
print("Bob's Rewards")

for item in purchases:
    if item[0] == "Bob" and item[1] == "3March":
        print("March Rewards")
        if item[2] > 50 and item[2] <= 100:
            print(item[2]- 50)
        elif item[2] > 100:
             print((item[2] - 100) * 2 + 50)
        else:
            print('0')
    if item[0] == "Bob" and item[1] == "4April":
        print("April Rewards")
        if item[2] > 50 and item[2] <= 100:
            print(item[2]- 50)
        elif item[2] > 100:
            print((item[2] - 100) * 2 + 50)
        else:
            print('0')
    if item[0] == "Bob" and item[1] == "5May":
        print("May Rewards")
        if item[2] > 50 and item[2] <= 100:
            print(item[2]- 50)
        elif item[2] > 100:
            print((item[2] - 100) * 2 + 50)
        else:
            print('0')
        print("Total Rewards: ", 37 + 15 + 1594 + 1192)
print("")
print("Bill's Rewards")

for item in purchases:
    if item[0] == "Bill" and item[1] == "3March":
        print("March Rewards")
        if item[2] > 50 and item[2] <= 100:
            print(item[2]- 50)
        elif item[2] > 100:
            print((item[2] - 100) * 2 + 50)
        else:
            print('0')
    if item[0] == "Bill" and item[1] == "4April":
        print("April Rewards")
        if item[2] > 50 and item[2] <= 100:
            print(item[2]- 50)
        elif item[2] > 100:
            print((item[2] - 100) * 2 + 50)
        else:
            print('0')
    if item[0] == "Bill" and item[1] == "5May":
        print("May Rewards")
        if item[2] > 50 and item[2] <= 100:
            print(item[2]- 50)
        elif item[2] > 100:
            print((item[2] - 100) * 2 + 50)
        else:
            print('0')
        print("Total Rewards: ", 0 + 0 + 90 + 72)
print("")
print("Joe's Rewards")

for item in purchases:
    if item[0] == "Joe" and item[1] == "3March":
        print("March Rewards")
        if item[2] > 50 and item[2] <= 100:
            print(item[2]- 50)
        elif item[2] > 100:
            print((item[2] - 100) * 2 + 50)
        else:
            print('0')
    if item[0] == "Joe" and item[1] == "4April":
        print("April Rewards")
        if item[2] > 50 and item[2] <= 100:
            print(item[2]- 50)
        elif item[2] > 100:
            print((item[2] - 100) * 2 + 50)
        else:
            print('0')
    if item[0] == "Joe" and item[1] == "5May":
        print("May Rewards")
        if item[2] > 50 and item[2] <= 100:
            print(item[2]- 50)
        elif item[2] > 100:
            print((item[2] - 100) * 2 + 50)
        else:
            print('0')
        print("Total Rewards: ", 300 + 58 + 0 + 42)



purchase = input("How much was your purchase? : ")
over_50 = int(purchase) - 50
over_100 = int(purchase) - 100 + over_50

print("")

if int(purchase) > 50 and int(purchase) <= 100:
    print("You have gained " + str(over_50) + " rewards points with your purchase")
elif int(purchase) > 100:
    print("You have gained " + str(over_100) + " rewards points with your purchase")
else:
    print("You have gained 0 rewards points")
    