import sys
import random

def verify():
    luhnFormula = []
    cardNumber = sys.argv[2]
    loopCounter = 1
    luhnSum = 0

    for x in cardNumber:
        x = int(x)

        if loopCounter % 2 != 0:  # If the position on the array is not even
            x = x * 2  # multiply x by two
        luhnFormula.append(x)
        loopCounter = loopCounter + 1

    loopCounter = -1
    for x in luhnFormula:

        if len(str(x)) == 2:
            x = str(x)
            luhnSum += int(x[0]) + int(x[1])
        else:
            luhnSum += x

    print(luhnSum)
    if int(luhnSum) % 10 == 0:
        # print("Credit Card Number Valid")
        return 1
    else:
        # print("Credit Card Number Invalid")
        return 0


def verifySpecific(cardNumber):
    luhnFormula = []
    loopCounter = 1
    luhnSum = 0

    for x in cardNumber:
        x = int(x)

        if loopCounter % 2 != 0:  # If the position on the array is not even
            x = x * 2  # multiply x by two
        luhnFormula.append(x)
        loopCounter = loopCounter + 1

    loopCounter = -1
    for x in luhnFormula:

        if len(str(x)) == 2:
            x = str(x)
            luhnSum += int(x[0]) + int(x[1])
        else:
            luhnSum += x

    print(luhnSum)
    if int(luhnSum) % 10 == 0:
        # print("Credit Card Number Valid")
        return 1
    else:
        # print("Credit Card Number Invalid")
        return 0



if str(sys.argv[1]) == 'verify':

    if verify() == 0:
        print("Credit Card Number Invalid")
    else:
        print("Credit Card Number Valid")

# ------------------VENDOR--------------


if str(sys.argv[1]) == 'vendor':

    cardNumber = sys.argv[2]

    # 1 American Express
    if cardNumber[0] == '3' and (cardNumber[1] == '4' or cardNumber[1] == '7') and len(cardNumber) == 15:
        print("This card could be American Express")

    # 2 Diners Club - Carte Blanche
    if (cardNumber[0] == '3') and (cardNumber[1] == '0') and ((cardNumber[2] == '1') or (cardNumber[2] == '2') or (cardNumber[2] == '3') or (cardNumber[2] == '4') or (cardNumber[2] == '5')) and (len(cardNumber) == 14):
        print("This card could be Diners Club - Carte Blanche")

    # 3 Diners Club - International
    if cardNumber[0] == '3' and cardNumber[1] == '6' and len(cardNumber) == 14:
        print("This card could be Diners Club - International")

    # 4 Diners Club - USA & Canada
    if (cardNumber[0] == '5') and (cardNumber[1] == '4') and (len(cardNumber) == 16):
        print("This card could be Diners Club - USA & Canada")

    # 5 Discover
    testString = str(cardNumber[0]) + str(cardNumber[1]) + str(cardNumber[2]) + str(cardNumber[3] + str(cardNumber[4]) + str(cardNumber[5]))
    if cardNumber[0] == '6' and ((cardNumber[1] == '0' and cardNumber[2] == '1' and cardNumber[3] == '1') or (cardNumber[1] == '4' and cardNumber[2] == '4' or cardNumber[2] == '5' or cardNumber[2] == '6' or cardNumber[2] == '7' or cardNumber[2] == '8' or cardNumber[2] == '9') or (cardNumber[1] == '5') or (int(testString) in range(622126, 622925))) and len(cardNumber) in range(16, 19):
        print("This card could be Discover")

    # 6 InstaPayment
    if cardNumber[0] == '6' and cardNumber[1] == '3' and (cardNumber[3] == '7' or cardNumber[3] == '8' or cardNumber[3] == '9') and len(cardNumber) == 16:
        print("This card could be InstaPayment")

    # 7 JCB
    testString = str(cardNumber[0]) + str(cardNumber[1]) + str(cardNumber[2]) + str(cardNumber[3])
    if int(testString) in range(3528, 3589) and (len(cardNumber) in range(16, 19)):
        print("This card could be JCB")

    # 8 Maestro
        testString = str(cardNumber[0]) + str(cardNumber[1]) + str(cardNumber[2]) + str(cardNumber[3])
    if (testString == '5018' or testString == '5020' or testString == '5038' or testString == '5893' or testString == '6304' or testString == '6759' or testString == '6761' or testString == '6762' or testString == '6763') and (len(cardNumber) in range(16, 19)):
        print("This card could be Maestro")

    # 9 MasterCard
    testString = str(cardNumber[0]) + str(cardNumber[1]) + str(cardNumber[2]) + str(cardNumber[3]) + str(cardNumber[4]) + str(cardNumber[5])
    if (int(testString) in range(51, 55)) or (int(testString) in range(222100, 272099)) and (len(cardNumber) == 16):
        print("This card could be MasterCard")

    # 10 Visa
    if (cardNumber[0] == '4') and (len(cardNumber) == 13 or len(cardNumber) == 16 or len(cardNumber) == 19):
        print("This card could be Visa")

    # 11 Visa Electron
    if ((cardNumber[0:3] == '4026' or cardNumber[0:3] == '4508' or cardNumber[0:3] == '4844' or cardNumber[0:3] == '4913' or cardNumber[0:3] == '4917') or cardNumber[0:5] == '417500') and len(cardNumber) == 16:
        print(len(cardNumber))
        print("This card could be Visa Electron")




# ------------------Generate--------------

if str(sys.argv[1]) == 'generate':

    newCardNumber = []

    print("Please type the number of what option you'd like")
    print("------------------------------------------------")
    print(" 1 --> American Express ")
    print(" 2 --> Diners Club - Carte Blanche ")
    print(" 3 --> Diners Club - International ")
    print(" 4 --> Diners Club - USA & Canada ")
    print(" 5 --> Discover ")
    print(" 6 --> InstaPayment ")
    print(" 7 --> JCB ")
    print(" 8 --> Maestro ")
    print(" 9 --> MasterCard ")
    print("10 --> Visa ")
    print("11 --> Visa Electron ")
    print("")

    option = input("Option: ")

    if option == 1:   # 1 American Express
        coin = random.randint(1, 2)

        newCardNumber.append(3)

        if coin == 1:
            newCardNumber.append(4)
        elif coin == 2:
            newCardNumber.append(7)

        guard = 0
        while guard == 0:

            del newCardNumber[3:15]
            x = 2
            while x < 14:
                newCardNumber.append(random.randint(1, 9))
                x += 1
            if verifySpecific(newCardNumber) == 1:
                guard = 1

        print("Valid Card number for American Express: ")
        print(newCardNumber)

    elif option == 2:   # 2 Diners Club - Carte Blanche

        newCardNumber.append(3)
        newCardNumber.append(0)
        coin = random.randint(1, 5)
        newCardNumber.append(coin)

        guard = 0
        while guard == 0:

            del newCardNumber[3:15]
            x = 2
            while x < 13:
                newCardNumber.append(random.randint(1, 9))
                x += 1
            if verifySpecific(newCardNumber) == 1:
                guard = 1

        print ("Valid Card number for Diners Club - Carte Blanche: ")
        print(newCardNumber)

    elif option == 3:    # 3 Diners Club - International

        newCardNumber.append(3)
        newCardNumber.append(6)

        guard = 0
        while guard == 0:

            del newCardNumber[3:17]
            x = 2
            while x < 13:
                newCardNumber.append(random.randint(1, 9))
                x += 1
            if verifySpecific(newCardNumber) == 1:
                guard = 1

        print ("Valid Card number for Diners Club - International: ")
        print(newCardNumber)

    elif option == 4:   # 4 Diners Club - USA & Canada
        newCardNumber.append(5)
        newCardNumber.append(4)

        guard = 0
        while guard == 0:
            del newCardNumber[2:17]
            x = 2
            while x < 16:
                newCardNumber.append(random.randint(1, 9))
                x += 1
            if verifySpecific(newCardNumber) == 1:
                guard = 1

        print ("Valid Card number for Diners Club - USA & Canada: ")
        print(newCardNumber)

    elif option == 5:   # 5 Discover
        x = 0
        newCardNumber.append(6)
        coin = random.randint(1, 800)

        if coin < 25:
            newCardNumber.append(0)
            newCardNumber.append(1)
            newCardNumber.append(1)
            x = 4
        elif coin >= 25 and coin < 50:
            newCardNumber.append(4)
            newCardNumber.append(random.randint(4, 9))
            x = 3
        elif coin >= 50 and coin < 75:
            newCardNumber.append(5)
            x = 2
        elif coin >= 75:
            newCardNumber.append(2)
            newCardNumber.append(2)

            numberRange = str(random.randint(126, 925))
            x = 6

            for y in numberRange:
                newCardNumber.append(y)

        length = random.randint(16, 19)
        guard = 0
        counter = x

        while guard == 0:
            del newCardNumber[x:length]

            counter = x

            while counter < length:
                newCardNumber.append(random.randint(1, 9))
                counter += 1
                print(counter)

            if verifySpecific(newCardNumber) == 1:
                guard = 1
            else:
                guard = 0

        print ("Valid Card number for Discover: ")
        print(newCardNumber)

    elif option == 6:   # 6 InstaPayment
        newCardNumber.append(6)
        newCardNumber.append(3)
        newCardNumber.append(random.randint(7, 9))

        guard = 0
        while guard == 0:

            del newCardNumber[3:17]
            x = 3
            while x < 16:
                newCardNumber.append(random.randint(1, 9))
                x += 1
            if verifySpecific(newCardNumber) == 1:
                guard = 1

        print ("Valid Card number for InstaPayment: ")
        print(newCardNumber)

    elif option == 7:  # 7 JCB
        numberRange = str(random.randint(3528, 3589))

        for y in numberRange:
            newCardNumber.append(y)

        length = random.randint(16, 19)

        guard = 0
        x = 4

        while guard == 0:
            del newCardNumber[x:length]

            counter = x

            while counter < length:
                newCardNumber.append(random.randint(1, 9))
                counter += 1
                print (counter)

            if verifySpecific(newCardNumber) == 1:
                guard = 1
            else:
                guard = 0

        print ("Valid Card number for JCB: ")
        print(newCardNumber)

    elif option == 8:     # 8 Maestro

        coin = random.randint(1, 9)
        if coin == 1:
            newCardNumber.append(5)
            newCardNumber.append(0)
            newCardNumber.append(1)
            newCardNumber.append(8)
        elif coin == 2:
            newCardNumber.append(5)
            newCardNumber.append(0)
            newCardNumber.append(2)
            newCardNumber.append(0)
        elif coin == 3:
            newCardNumber.append(5)
            newCardNumber.append(0)
            newCardNumber.append(3)
            newCardNumber.append(8)
        elif coin == 4:
            newCardNumber.append(5)
            newCardNumber.append(8)
            newCardNumber.append(9)
            newCardNumber.append(3)
        elif coin == 5:
            newCardNumber.append(6)
            newCardNumber.append(3)
            newCardNumber.append(0)
            newCardNumber.append(4)
        elif coin == 6:
            newCardNumber.append(6)
            newCardNumber.append(7)
            newCardNumber.append(5)
            newCardNumber.append(9)
        elif coin == 7:
            newCardNumber.append(6)
            newCardNumber.append(7)
            newCardNumber.append(6)
            newCardNumber.append(1)
        elif coin == 8:
            newCardNumber.append(6)
            newCardNumber.append(7)
            newCardNumber.append(6)
            newCardNumber.append(2)
        elif coin == 9:
            newCardNumber.append(6)
            newCardNumber.append(7)
            newCardNumber.append(6)
            newCardNumber.append(3)

        length = random.randint(16, 19)

        guard = 0
        x = 4

        while guard == 0:
            del newCardNumber[x:length]

            counter = x

            while counter < length:
                newCardNumber.append(random.randint(1, 9))
                counter += 1
                print (counter)

            if verifySpecific(newCardNumber) == 1:
                guard = 1
            else:
                guard = 0

        print ("Valid Card number for Maestro: ")
        print(newCardNumber)

    elif option == 9:   # 9 MasterCard
        coin = random.randint(1, 50000)

        x = 0

        if coin < 50 :
            numberRange = str(random.randint(51, 55))
            x = 2
            for y in numberRange:
                newCardNumber.append(y)
        elif coin >= 50 :
            numberRange = str(random.randint(222100, 272099))
            x = 6
            for y in numberRange:
                newCardNumber.append(y)

        length = 16

        guard = 0

        while guard == 0:
            del newCardNumber[x:length]

            counter = x

            while counter < length:
                newCardNumber.append(random.randint(1, 9))
                counter += 1
                print (counter)

            if verifySpecific(newCardNumber) == 1:
                guard = 1
            else:
                guard = 0

        print ("Valid Card number for MasterCard: ")
        print(newCardNumber)

    elif option == 10:  # 10 Visa
        newCardNumber.append(4)

        coin = random.randint(1,3)

        if coin == 1:
            length = 13
        elif coin == 2:
            length = 16
        elif coin == 3:
            length = 19

        guard = 0
        while guard == 0:

            del newCardNumber[1:20]
            x = 1
            while x < length:
                newCardNumber.append(random.randint(1, 9))
                x += 1
            if verifySpecific(newCardNumber) == 1:
                guard = 1

        print("Valid Card number for Visa: ")
        print(newCardNumber)


    elif option == 11:      # 11 Visa Electron

        coin = random.randint(1, 6)

        if coin == 1:
            newCardNumber.append(4)
            newCardNumber.append(0)
            newCardNumber.append(2)
            newCardNumber.append(6)
            x = 4
        elif coin == 2:
            newCardNumber.append(4)
            newCardNumber.append(5)
            newCardNumber.append(0)
            newCardNumber.append(8)
            x = 4
        elif coin == 3:
            newCardNumber.append(4)
            newCardNumber.append(8)
            newCardNumber.append(4)
            newCardNumber.append(4)
            x = 4
        elif coin == 4:
            newCardNumber.append(4)
            newCardNumber.append(9)
            newCardNumber.append(1)
            newCardNumber.append(3)
            x = 4
        elif coin == 5:
            newCardNumber.append(4)
            newCardNumber.append(9)
            newCardNumber.append(1)
            newCardNumber.append(7)
            x = 4
        elif coin == 6:
            newCardNumber.append(4)
            newCardNumber.append(1)
            newCardNumber.append(7)
            newCardNumber.append(5)
            newCardNumber.append(0)
            newCardNumber.append(0)
            x = 6

        length = 16
        guard = 0
        while guard == 0:
            del newCardNumber[x:length]

            counter = x

            while counter < length:
                newCardNumber.append(random.randint(1, 9))
                counter += 1
                print (counter)

            if verifySpecific(newCardNumber) == 1:
                guard = 1
            else:
                guard = 0

        print ("Valid Card number for Visa Electron: ")
        print(newCardNumber)



if sys.argv[1] == "test":

    x = 12


    testArray = []

    testArray.append(5)
    testArray.append(5)
    testArray.append(5)
    testArray.append(5)

    testString =  str(testArray[0]) + str(testArray[1]) + str(testArray[2]) + str(testArray[3])


    if int(testString) in range(5000, 6000):
        print("yes")




# ------------------Generate--------------

if str(sys.argv[1]) == 'checksum':

    preLength = len(sys.argv[2])
    lengthToBe = random.randint(14, 19)

    guard = 0
    while guard == 0:
        cardNumber = []
        for x in sys.argv[2]:
            cardNumber.append(x)
            currentLength = len(cardNumber)

        while currentLength < lengthToBe:
            cardNumber.append(random.randint(1, 9))
            print(len(cardNumber))
            currentLength = len(cardNumber)

        if verifySpecific(cardNumber) == 1:
            guard = 1
        else:
            del cardNumber[preLength:lengthToBe]
    print("Card for " + sys.argv[2] + " calculated valid checksum: ")
    print("New Card Number : " + str(cardNumber))


if str(sys.argv[1]) == 'test':

    for x in range(5):
        print(x)
