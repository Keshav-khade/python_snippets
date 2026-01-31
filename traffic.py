# traffic light controller using the match statement

signal = str(input("tell me the light !"))
is_emergency = input("is this emergency ? {yes/no}").lower() == "yes"

match signal:
	case 'green':
		print("emergency allowed" if is_emergency else "Go Hurry up !")

	case 'yellow':
		print("emergency allowed" if is_emergency else "Slow down buddy !")

	case 'red' :
		if is_emergency:
			print("Emergency pass allowed")
		else:
			print("Stop ! please wait")