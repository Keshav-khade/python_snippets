# exception handling by python

# try:
#          name = input("enter you file name: ")
#          f = open(name,"r")
# except IOError:
#           print("file not found: try again !")
# finally:
#           lines = f.readlines()
#           content = "".join(lines)
#           n = len(lines)
#           print(content)
#           print(name,"has",n,"line")
#           f.close()

# def cal_avg(lst):
#           sum = 0
#           avg = 0
#           for x in lst:
#                   sum += x
#           n = len(lst)
#           avg = sum / n
#           return sum, avg
# try:
#           lst = []
#           for _ in range(5):
#                  '''eval find the alter native of this'''
#                  x = eval(input("Enter your sequence: "))
#                  if len(lst) == 0:
#                          raise ZeroDivisionError
#                  lst.append(x)
#           sum,avg = cal_avg(lst)
#           print("your total is: %d"%sum)
#           print("your avg is: %f"%avg)

# except TypeError:
#         print("might you Entered wrong type")
# except ZeroDivisionError:
#         print("don't Enter number less than 1")

