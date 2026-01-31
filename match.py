# match statement in python

day = 1
is_holiday = False

match day: # evaluate once
	case 1 if not is_holiday:
		print("sunday is a holiday")
	case 2:
		print('monday')
	case 3:
		print('tuesday')
	case 4 if not is_holiday:
		print("wednesday")
	case 5:
		print('thursday')
	case 6:
		print("friday")
	case 7:
		print('saturday')
	case _:
		print('Invalid')

	