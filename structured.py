# to calculate dearness allowance
def da(basic):
	"in general da is 80% of basic salary"
	da = basic*80/100
	return da

# to calculate house rent allowance
def hra(basic):
	"hra is 15% of basic salary"
	hra = basic*15/100
	return hra

# to calculate provident funds amount
def pf(basic):
	"pf is 12% of basic salary"
	pf = basic*12/100
	return pf

# to calculate income tax payable by employee
def itax(gross):
	"itax is calculated at 10% on gross"
	tax = gross*0.1
	return tax
"""
# this is the main program
# calculate the gross salary by taking info of basic salary
basic = float(input("Enter your basic salary: "))
# calculate the gross salary
gross_salary = ( basic + da(basic) + hra(basic) )
print("your gross salary: {:.2f}".format(gross_salary))
# calculate the net salary
net_salary = (gross_salary - pf(basic) - itax(gross_salary))
print("your net salary: {:10.2f}".format(net_salary))
"""
# alignments basics
"""10   → total width
.2   → 2 decimal places
f    → float number

print("{:.2f}".format(num)) -> just rounds up using banker's logic
print("{:10.2f}".format(num)) -> rounds up and aligned right by default

| Format      | Meaning                 |
| ----------- | ----------------------- |
| {:10.2f}    | Right aligned (default) |
| {:<10.2f}   | Left aligned            |
| {:^10.2f}   | Center aligned          |
 
"""
" we have succesffuly creating our module and use it"
from employee import *

basic = float(input("Enter your basic salary: "))
# calculate the gross salary
gross_salary = ( basic + da(basic) + hra(basic) )
print("your gross salary: {:10.2f}".format(gross_salary))
# calculate the net salary
net_salary = (gross_salary - pf(basic) - itax(gross_salary))
print("your net salary: {:10.2f}".format(net_salary))
