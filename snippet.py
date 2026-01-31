										# bank pin entry attempts

attempts = 0
max_attempts=3
c_pin = "1234"
flag = 1

while attempts < max_attempts:
    if flag == 1:
        pin = input("Enter your pin: ")

    if c_pin == pin:
        print("access granted")
        break
    else:
        print("access denied")
        flag = 0 
        pin = input("please re-enter your pin sir: ")
        attempts += 1
       

        if attempts == max_attempts:
            print("please try later on sir: ")
            break 