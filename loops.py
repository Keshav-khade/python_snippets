# python for and while loops
# this program is for pythons @for loop

'''list1= ['apple','banana','cherry','mango','lichi']

for i in list1:
	print(i,end=' ')
	if i == "mango":
		break
'''	

# iteration on a string

'''x = "my family is very good"

for i in x:
	print(i,end='')
'''


'''list1= ['apple','banana','cherry','mango','lichi']

for i in list1:
	print(i,end=' ')
	if i == "mango":
		continue
	print('ok this is just an example to show the use of continue')
'''

# range() function use we can iterate on a specific values from where you want till where
# however, the range function increments the value by 1 by default but you can also specify that by adding third parameter

'''for i in range(1,6,2):   # from 1 to 6 , till n-1
	print(i)
'''
'''
for x in range(6): 
  	if x == 3: break
  	print(x)
else:
  print("Finally finished!")
''''
# here if you use break statement then you can't expect from else to print because break stops the entire\
loop here
