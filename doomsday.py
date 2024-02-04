from datetime import datetime, timedelta
from random import randrange
from time import time

print("\nWelcome to Doomsday! You will be asked to give a starting year and an ending year. Random dates from that range of year(s) will be given to you and you must answer what day of the week the date falls on. \nTo exit the program, type 'exit'.\n")

# Used for tracking correct answer percentage and time spent per question
correct_guesses = 0
incorrect_guesses = 0
times = []

start_year = (input("What is the starting year? "))
if(start_year == "exit"):
    print("\nBye!")
    exit()

end_year = (input("What is the ending year? "))
if(end_year == "exit"):
    print("\nBye!")
    exit()

# A random date will be selected from January 1st of the start year and December 31st of the end year given by the user.
start_year = datetime.strptime(start_year,"%Y")
end_year = datetime.strptime(end_year +",12,31","%Y,%m,%d")

def random_date_generator(start_year,end_year):
    days_between_years = (end_year - start_year).days
    random_day = randrange(0,days_between_years)

    return start_year + timedelta(days = random_day)


# User is given random dates until they decide stop. A random date is generated between the years they gave, and the user guesses what day of the week it falls on. Correct guesses, incorrect guesses, and time spent per question are tracked.
while(1):
    rand_date = random_date_generator(start_year, end_year)
    day_of_week = rand_date.strftime("%A")
    formatted_date = rand_date.strftime("%B, %d, %Y")
    start_time = time()
    user_day_of_week = (input(f"\nWhat day of the week does this date fall on: {formatted_date}?\n\t"))
    end_time = round(time() - start_time,2)

    # While loop is broken out of if user types 'exit'
    if(user_day_of_week == "exit"):
        break
    # User guesses the correct day of week the date falls on
    elif(user_day_of_week.lower() == day_of_week.lower()):
        print(f"Correct! You got the answer in {end_time} seconds! ")
        correct_guesses += 1
    else:
    # User guesses the incorrect day of week the date falls on
        print(f"Wrong, the correct day was {day_of_week}. You spent {end_time} seconds on that question.")
        incorrect_guesses += 1

    times.append(end_time)

# Give stats to user if they attempted at least 1 question.
if(max(correct_guesses,incorrect_guesses) == 0):
    print("\nBye!")
else:
    print(f"\nSession Stats\nCorrect guesses: {correct_guesses}\nIncorrect guesses: {incorrect_guesses}\nAnswer percentage: {round((correct_guesses/(correct_guesses+incorrect_guesses))*100,2)}%\nAverage time spent per question: {round(sum(times)/len(times),2)} seconds\n\nBye!")