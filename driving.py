country = input('請問您是哪國人：')
age = int(input('請輸入年齡：'))
if country == '台灣':
	if age >= 18:
		print('可以考駕照摟~')
	else:
		print('你8可以開車或騎車')
elif country == '美國':
	if age >= 16:
		print('You can apply driving license.')
	else:
		print('You cannot drive.')