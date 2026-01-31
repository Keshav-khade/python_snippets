										#type of arguments in python
""""

#positional arguments
def attach(s1,s2):
    return s1+s2
x = attach("New","York")
print(x)

# keyword arguments
def grocery(price,product):
    print("item = %s"  %product)
    print("price = %.1f"   % price)
grocery(price=23.34,product="brush")
grocery(price=45.00,product="costic soda")

# default arguments
def grocery(item,price=45.00):
     print("item = %s"  %item)
     print("price = %.2f"   % price)
grocery(price=34.45,item="ribbon")
grocery(item="drain cleaner")

"""

def add(frag , *args):
    "this program find the sum"
    sum = 0
    for i in args:
        sum = sum + i
    print(f"total sum is: {frag+sum}")
add(5,10,20,40)


# variable length **kwargs
def display(frags,**kwargs):
    "this function show how to use kwargs"
    print("this is the formal argument: ",frags)
    for x,y in kwargs.items():
        print("key :{}, value :{}".format(x,y))

display(5,rno="0808DS231064",name="kartik khade")

# if you want to overtake manual passing you can also try this
data = { "rno":"0808ds231064","name":"kartik khade","age":20,"address":"Indore,india","email":"khadekartik834@gmail.com"}
display(5,**data) # you have to pass like this here you pass keword argument as a reference