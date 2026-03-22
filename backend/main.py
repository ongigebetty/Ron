food = ["Ugali", "Rice","Chapati","Pancakes", "indomie"]
day_of_the_week =["Monday","Tuesday", "Wednesday","Thursday", "Friday"]


def food_suggestion ():
	user_input = input("What day is it today?")
	if user_input in day_of_the_week:
		index = day_of_the_week.index(user_input)

		suggest = food[index]
		
		print (f"Today is {user_input} so lets eat {suggest}!")
	else:
		print ("Sorry not today")


food_suggestion()



	