#vending machine
items={

#chips - 4AED
11: ["Cheetos", 4, 10], 12: ["Doritos", 4, 10], 13: ["Lays", 4, 10], 14: ["Kurkure", 4, 10], 15: ["Oman Chips", 4, 10], 
16: ["Pringles", 4, 10], 17: ["Bugles", 4, 10], 18: ["Lays Max", 4, 10], 19: ["Mr Crips", 4, 10], 20: ["Takis", 4, 10],

#chocolates - 2AED
21: ["Sour Candy", 2, 10], 22: ["Mars", 2, 10], 23: ["Twix", 2, 10], 24: ["Bounty", 2, 10], 25: ["KitKat", 2, 10],

#soda - 3AED
31: ["CocaCola", 3, 10], 32: ["Pepsi", 3, 10], 33: ["Fanta", 3, 10], 34: ["Sprite", 3, 10], 35: ["Mountain Dew", 3, 10],
36: ["7Up", 3, 10], 37: ["Dr Pepper", 3, 10], 38: ["Mirinda", 3, 10],

#juices - 1AED
41: ["Orange Juice", 1, 0], 42: ["Apple Juice", 1, 10], 43: ["Grape Juice", 1, 10], 44: ["Mango Juice", 1, 10], 45: ["Pineapple Juice", 1, 10],
46: ["Cranberry Juice", 1, 10],47: ["Water", 1, 10], 48: ["Carrot Juice", 1, 10],49: ["Mixed Fruit Juice", 1, 10], 

#cookies - 2AED
51: ["Oreo", 2, 10], 52: ["Choco Chip Cookies", 2, 10], 53: ["Digestive Biscuits", 2, 10], 54: ["Marie Biscuits", 2, 10], 55: ["Butter Cookies", 2, 10],

#cupcakes - 3AED
56: ["Vanilla Cupcake", 3, 10], 57: ["Chocolate Cupcake", 3, 10], 58: ["Red Velvet Cupcake", 3, 10], 59: ["Lemon Cupcake", 3, 10], 60: ["Strawberry Cupcake", 3, 10],

#cup noodles - 5AED
61: ["Chicken Noodles", 5, 10], 62: ["Beef Noodles", 5, 10], 63: ["Vegetable Noodles", 5, 10], 64: ["Shrimp Noodles", 5, 10], 65: ["Spicy Noodles", 5, 10]
}

def show_menu():
    print("\n===== VENDING MACHINE MENU =====")
    for code, item in items.items(): #iterate through items
        name, price, stock = item
        status = "Out of stock" if stock == 0 else f"Stock: {stock}"
        print(f"{code} - {name} ({price} AED) [{status}]")
    print("===============================\n")


while True: #main loop
    show_menu() #display menu

    choice = input("Enter item code (or 0 to exit): ") #take item code input

    if choice == "0": #exit condition
        print("Thank you for using the vending machine!") #print thank you message
        break #exit condition

    if not choice.isdigit() or int(choice) not in items: #validate item code
        print("Invalid item code.\n") #print invalid code message
        continue #continue to next iteration

    choice = int(choice) #get item code
    name, price, stock = items[choice] #get item details

    if stock == 0: #check stock
        print("Sorry, this item is out of stock.\n") #print out of stock message
        continue #continue to the next iteration

    print(f"You selected: {name}") #print selected item
    print(f"Price: {price} AED") #print price of selected item

    try: #take money input
        money = float(input("Insert money: ")) #take money input
    except ValueError: #handle invalid input
        print("Invalid amount.\n") #print message
        continue #continue to next iteration

    if money < price: #if money entered is insufficient 
        print("Not enough money, try again.\n") #print message
    else: #if money entered is sufficient
        items[choice][2] -= 1   #reduce stock
        change = money - price #calculate change
        print(f"Dispensing {name}") #dispense the item
        if change > 0: #return change if any
            print(f"Change returned: {change:.2f} AED") #print change 
        print("Thank you!\n") #print thank you message