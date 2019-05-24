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
