try:
	i=int(input("enter ur number"))
	if i<3:
		b=(i/i-3)
	elif i==3:
		raise ZeroDivisionError
	else:
		raise TypeError
except ZeroDivisionError:
	print("u hv choosen 3")
except TypeError:
	print(" u hv chosen greater than 3")
else:
	print(b)
finally:
	print("completed")	