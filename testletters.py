plate = input("Enter the plate number: ")

if plate[0] == 'K':
    if plate[1].isalpha() and plate[2].isalpha() and plate[3].isdigit() and plate[4].isdigit() and plate[5].isdigit() and plate[6].isalpha():
        print(plate)
    else:
        print('that is not a kenyan plate')
else:
    print("That is not a Kenyan plate")