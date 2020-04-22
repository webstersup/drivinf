#詢問輸入者國家和年紀,查看是否可以開車資格
#台灣18~65可以開車
#美國20~60可以開車
country = input('請輸入您的國家:')
age = input('請輸入您的年紀:')
age = int(age)
if country == '台灣' or country == '臺灣' :
	if age >= 18 and age <= 65 :
		print ('您在台灣是有開車資格')
	elif age <= 18 :
		print ('您在台(臺)灣因為年紀過小沒有開車資格')
	else : 
		print ('您在台(臺)灣因為年紀過大沒有開車資格')

elif country == '美國' :
	if age >= 20 and age <= 60 :
		print ('您在美國是有開車資格')
	elif age <= 20 :
		print ('您在美國因為年紀過小沒有開車資格')
	else :
		print ('您在美國因為年紀過小沒有開車資格')
else :
	print ('查找不到您國家得開車資格')
