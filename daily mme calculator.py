import math

while True:
    print("\nChoose the drug to calculate MME per day.\n\n0 - Codeine\n1 - Fentanyl transdermal (in mcg/hr)\n2 - Fentanyl buccal\n3 - Fentanyl Spray/film\n4 - Hydrocodone\n5 - Hydromorphone\n6 - Levorphanol\n7 - Morphine\n8 - Oxycodone\n9 - Oxymorphone\n10 - Tramadol\n")

    oper = input("\nYour option from the menu: ") 

    #Codeine
    if oper == "0":
        val1 = float(input("\nCodeine strength: ")) 
        val2 = float(input("\nQuantity dispensed: "))
        val3 = float(input("\nDays supply: ")) 

        print("\nThe MME per day is: " + str((val1 * (val2 / val3)) * 0.15) + "\n")

        back = input('\nGo back to the main menu? (y/n) ')

        if back == 'y':
            continue
        else:
            break

    #Fentanyl transdermal (in mcg/hr)
    elif oper == "1":
        val1 = float(input("\nFentanyl strength: ")) 
        val2 = float(input("\nQuantity dispensed: "))
        val3 = float(input("\nDays supply: ")) 

        print("\nThe MME per day is: " + str((val1 * (val2 / val3)) * 2.4) + "\n")

        back = input('\nGo back to the main menu? (y/n) ')

        if back == 'y':
            continue
        else:
            break

    #Fentanyl buccal
    elif oper == "2":
        val1 = float(input("\nFentanyl strength: ")) 
        val2 = float(input("\nQuantity dispensed: "))
        val3 = float(input("\nDays supply: ")) 

        print("\nThe MME per day is: " + str((val1 * (val2 / val3)) * 0.13) + "\n")

        back = input('\nGo back to the main menu? (y/n) ')

        if back == 'y':
            continue
        else:
            break

    #Fentanyl spray/film
    elif oper == "3":
        val1 = float(input("\nFentanyl strength: ")) 
        val2 = float(input("\nQuantity dispensed: "))
        val3 = float(input("\nDays supply: ")) 

        print("\nThe MME per day is: " + str((val1 * (val2 / val3)) * 0.18) + "\n")

        back = input('\nGo back to the main menu? (y/n) ')

        if back == 'y':
            continue
        else:
            break

    #Hydrocodone
    elif oper == "4":
        val1 = float(input("\nHydrocodone strength: ")) 
        val2 = float(input("\nQuantity dispensed: "))
        val3 = float(input("\nDays supply: ")) 

        print("\nThe MME per day is: " + str((val1 * (val2 / val3)) * 1) + "\n")

        back = input('\nGo back to the main menu? (y/n) ')

        if back == 'y':
            continue
        else:
            break

    #Hydromorphone
    elif oper == "5":
        val1 = float(input("\nHydromorphone strength: ")) 
        val2 = float(input("\nQuantity dispensed: "))
        val3 = float(input("\nDays supply: ")) 

        print("\nThe MME per day is: " + str((val1 * (val2 / val3)) * 4) + "\n")

        back = input('\nGo back to the main menu? (y/n) ')

        if back == 'y':
            continue
        else:
            break

    #Levorphanol
    elif oper == "6":
        val1 = float(input("\nLevorphanol strength: ")) 
        val2 = float(input("\nQuantity dispensed: "))
        val3 = float(input("\nDays supply: ")) 

        print("\nThe MME per day is: " + str((val1 * (val2 / val3)) * 11) + "\n")

        back = input('\nGo back to the main menu? (y/n) ')

        if back == 'y':
            continue
        else:
            break
    
    #Morphine
    elif oper == "7":
        val1 = float(input("\nMorphine strength: ")) 
        val2 = float(input("\nQuantity dispensed: "))
        val3 = float(input("\nDays supply: ")) 

        print("\nThe MME per day is: " + str((val1 * (val2 / val3)) * 1) + "\n")

        back = input('\nGo back to the main menu? (y/n) ')

        if back == 'y':
            continue
        else:
            break
    
    #Oxycodone
    elif oper == "8":
        val1 = float(input("\nOxycodone strength: ")) 
        val2 = float(input("\nQuantity dispensed: "))
        val3 = float(input("\nDays supply: ")) 

        print("\nThe MME per day is: " + str((val1 * (val2 / val3)) * 1.5) + "\n")

        back = input('\nGo back to the main menu? (y/n) ')

        if back == 'y':
            continue
        else:
            break

    #Oxymorphone
    elif oper == "9":
        val1 = float(input("\nOxymorphone strength: ")) 
        val2 = float(input("\nQuantity dispensed: "))
        val3 = float(input("\nDays supply: ")) 

        print("\nThe MME per day is: " + str((val1 * (val2 / val3)) * 3) + "\n")

        back = input('\nGo back to the main menu? (y/n) ')

        if back == 'y':
            continue
        else:
            break

    #Tramadol
    elif oper == "10":
        val1 = float(input("\nTramadol strength: ")) 
        val2 = float(input("\nQuantity dispensed: "))
        val3 = float(input("\nDays supply: ")) 

        print("\nThe MME per day is: " + str((val1 * (val2 / val3)) * 0.1) + "\n")

        back = input('\nGo back to the main menu? (y/n) ')

        if back == 'y':
            continue
        else:
            break
    
    else:
        print("\nInvalid option!\n")
        continue

#End of the program     
