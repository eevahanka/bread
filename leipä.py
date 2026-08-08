''' 
nonii elikkäs tän projektin tarkoitus on että 
 1) mä voin heittää kui paljon käytän juurta  
 2) ja mun haluaman hydraatioprosentin (veden määrä suhteessa jauhojen määrään)  (tähä on varmaa default)
 -> ni saan kui paljon pitää lisätä jauhoi ja vettä + suolaa
 (käytän bellatablen reseptiä pohjana https://www.bellatable.fi/reseptit/hapanjuurileipa101?rq=hapanjuurileip%C3%A4) 
 '''

import os #ni voin tyhjentää terminaalin

defautl_hydration = 70
default_flour_amount= 880
default_salt_prosent = 1.6

def custom_ingredients(starter_amount):
    s = starter_amount
    flour_amount = int(input("kuinka paljon jauhoja?"))
    hydration_per = int(input("hydraatio%?"))
    salt_per = int(input("suola%?"))
    return calculate_ingredients(s, flour_amount, hydration_per, salt_per)

def calculate_ingredients( starter_amount, flour_amount=default_flour_amount, hydration_percentage=defautl_hydration, salt_prosent=default_salt_prosent):
    starter_flour = starter_water = starter_amount/2
    flour_to_add = flour_amount - starter_flour
    water_needed = flour_amount * hydration_percentage / 100
    water_to_add = water_needed - starter_water
    salt_needed = flour_amount * salt_prosent / 100

    return int(flour_to_add), int(water_to_add), int(salt_needed)

def io():
    clear()
    print("Hello and welcome to Eevas leipätehdas kerro kuinka paljon lisäät juurta leipääsi niin me kerromme lopun :))))))))))))))")
    print("Mitä haluat tehdä? \n (1) perus loaffi \n (2) focaccia \n (3) sämpylä \n (4) custom leipä")
    bread_type = input("paina 1, 2, 3 tai 4 ")
   
    starter_amount = int(input("how much starter (grams)? "))
    if bread_type == '1':
        flour_to_add, water_to_add, salt_needed = calculate_ingredients(starter_amount)
    elif bread_type == '2':  # focaccia
        flour_to_add, water_to_add, salt_needed = calculate_ingredients(starter_amount, 575, 83, 1.74)
        print("näiden lisäksi lisää 25g nestettä suolan kanssa (puolet oliiviöljyä?)")
    elif bread_type == '3':  # sämpylä
        flour_to_add, water_to_add, salt_needed = calculate_ingredients(starter_amount, starter_amount*4.5, 100, 2.3)
    elif bread_type == '4':  # custom
        flour_to_add, water_to_add, salt_needed = calculate_ingredients(custom_ingredients(starter_amount))
    else:
        print("tuntematon valinta, oletetaan perus leipä")
        flour_to_add, water_to_add, salt_needed = calculate_ingredients(starter_amount)
    print(f" add {water_to_add}g of water \n {flour_to_add}g of flour \n {salt_needed}g of salt (remeber to wait for autolyse first!)")

def clear():
    '''
    Clears the terminal screen and scroll back to present
    the user with a nice clean, new screen. Useful fperor managing
    menu screens in terminal applications.
    '''
    os.system('cls||echo -e \\\\033c')

if __name__ == "__main__":
    io()