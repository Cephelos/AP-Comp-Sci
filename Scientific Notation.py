
validInput = False

while validInput == False:
    convert = int(input('Enter Starting Notation: \nSci(1) \nDec(2) \n'))
    if convert == 1:
        n = int(input("Enter base: "))
        e = int(input("Enter exponent: "))
        print str(n) + 'x10^' + str(e)
        print str(n*(10**e))
        validInput = True
    elif convert == 2:
        n = int((input("Enter decimal number: ")))
        nString = str(n)
        digits = len(nString)
        print nString


        print nString[0] + '.' + nString[1:] + 'x10^' + str(digits - 1)

        validInput = True




