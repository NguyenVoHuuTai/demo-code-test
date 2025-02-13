# Ctrl + / to disable or enable comment
# print("hello world")
# x = input()
# print(x)
# print("The first name")
# first_name = input()
# print("The first name is " + first_name) #concanitation
# print("The last name")
# last_name = input()
# print("The last name is" + last_name)
# print("Your name is " + last_name + " " + first_name)
# first_name = input("Your first name: ")
# last_name = input("Your last name: ")
# print("Your name is " + last_name + " " + first_name)
# CURRENT_YEAR = 2025
# year_born = int(input("Enter the year you were born: "))
# age = CURRENT_YEAR - year_born
# year_born = input("Enter the year you were born: ")
# year_born = int(year_born) #overwrite
# age = CURRENT_YEAR - int(year_born)
# print("You are " + str(age) + " years old")
# print("You are " + str(age) + " years old in " + str(CURRENT_YEAR))
# print("You are {0} years old in {1}".format(age, CURRENT_YEAR))
# x = "1.856963254488"
# x = float(x)
# x = round(x,5) #lam tron so
# print(x)
# temperature = int(input("Enter the temperature: "))
# if temperature < 15:
# 	print("It's cold")
# elif temperature >= 15 and temperature <= 25:
#    	print("It's good")
# else:
# 	print("It's hot")
# one tab = 4 spaces
# temperature = 14
# hot = False
# if temperature > 30:
# 	hot = True
# if not hot:
# 	print("It's not hot")
# if temperature < 15:
# 	print("It's cold")
# 	if temperature >=10 and temperature <= 12 or temperature == 14:
# 		print("It's very cold")
# else:
# 	print("It's good")
gender_input = input("Are you male (yes or no): ")
is_male = None

if gender_input == "yes":
    is_male = True
elif gender_input == "no":
	is_male = False
else:
    is_male = None

if is_male == True:
	print("You are male")
elif is_male == False:
	print("You are female")
elif is_male == None:
	print("Unknown")