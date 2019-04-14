def bmi_app():
	height = input('how tall are you?')
	weight = input('how much do you weight?')
	bmi_value = int(weight)/(int(height)/100)**2
	print('BMI = {}'.format(round(bmi_value, 2)))
	if bmi_value < 18.5:
		print('You\'d better eat more!')
	elif bmi_value >= 18.5 and bmi_value <= 24:
		print('Good job!')
	else:
		print('You\'d better do some exercies!')
bmi_app()
