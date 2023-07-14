menu=["sushi","cheeseburgers","chicken nuggets", "chicken wings","pepperoni pizza","cola","pepsi","sprite","orange fanta","water"]
combo=[]
def addFood(food):
    menu.append(food)
    print("Preparing "+food+"...")
def showCombo():
    print("Your combo: ")
    print("  "+str(combo))
def addToCombo():
    food1=input("Please enter a food: ")
    combo.append(food1)
    food2=input("Please enter another food: ")
    combo.append(food2)
    drink=input("Please enter a drink: ")
    combo.append(drink)
    showCombo()
print("Welcome to the infinity restarant, where the menu is infinite!")
comba=input("Would you like to try our 'Combo Of Magic'?(y/n)")
if comba == "y":
    addToCombo()
else:
    while True:
        food=input("What would you like to order: ")
        if food in menu:
            print("Preparing "+food+"...")
        else:
            addFood(food)
        a=input("Continue ordering?(y/n)")
        if a != "y":
            break
print("Enjoy your food!")
