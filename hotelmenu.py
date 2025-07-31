#define the menu of restaurant

menu={
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80,
}
#greet

print("Welcome to Restaurant")
print("Pizza:Rs 40\nPasta:Rs 50\nBurger:60\nSalad:70\nCoffee:80")

order_total=0
item_1=input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"Your item{item_1} has been added to your order")

else:
    print("Please order something else")
another_order=input("Do you want to add another item? (Yes/No)")
if another_order=="Yes":
    item_2=input("Enter thr name of second item = ")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available")

print(f" the total amount of item is {order_total}")