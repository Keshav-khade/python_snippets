									# python little snippet

for i in range(3):
    sum =0
    if i == 1:
        sum = sum + i
print(sum)
    

									# ATM login with max attempts

correct_pin = "1234"
for attempts in range(3):
    pin = input("Enter your pin sir: ")
    if pin == correct_pin:
        print("access granted")
        break
    print("wrong password try again sir !")
else:
    print("Your account is blocked: ")


									# Filter out invalid scores 

scores = [12,34,-9,67,-15,7,-54]
for i in scores:
    if i < 0:
        continue
    print(i)

									# stop once correct item is found in inventory

inventory = ["pen","Bottle","books","copy","watch","eraser","lunch box"]
item_ = "books"

for item in inventory:
    if item == item_:
        print(f"{item_}: is found in inventory")
        break


