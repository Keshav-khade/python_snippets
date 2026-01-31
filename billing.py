# modular billing system

def inputs():
    price = int(input("Enter price :"))
    quant = int(input("Enter quantity :"))
    return price,quant

def total(price,quant):
    return price * quant

def display_bill(total):
    print(f"your total amount is :₹{total}")

# that is ongoing flow
price,quant = inputs()
sum = total(price,quant)
display_bill(sum)