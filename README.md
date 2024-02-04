# Doomsday - Day of the Week Guesser

## Introduction
Welcome to Doomsday, a Python program designed to test your skills in guessing the day of the week for random dates! In this program, the user is prompted to provide a starting and ending year. They then receive random dates within that year range and must guess the day of the week that the date falls on. The program allows users to exit at any time by typing 'exit'. Various stats are tracked and are given to the user when they exit.

## Instructions
1. Run the program.
2. Enter the starting year.
3. Enter the ending year.
4. Guess the day of the week for the presented date.
5. Repeat until deciding to exit the program.

## Usage
```bash
$ python doomsday.py
```
## Example
```bash
PS D:\doomsday> python doomsday.py

Welcome to Doomsday! You will be asked to give a starting year and an ending year. Random dates from that range of year(s) will be given to you and you must answer what day of the week the date falls on.
To exit the program, type 'exit'.

What is the starting year? 1950
What is the ending year? 2050

What day of the week does this date fall on: February, 16, 2042?
        sunday
Correct! You got the answer in 19.43 seconds! 

What day of the week does this date fall on: April, 08, 1988?
        friday
Correct! You got the answer in 12.98 seconds! 

What day of the week does this date fall on: October, 11, 1950?
        tuesday
Wrong, the correct day was Wednesday. You spent 4.28 seconds on that question.

What day of the week does this date fall on: March, 02, 2007?
        friday
Correct! You got the answer in 12.71 seconds! 

What day of the week does this date fall on: March, 24, 2000?
        friday
Correct! You got the answer in 6.02 seconds! 

What day of the week does this date fall on: June, 21, 1959?
        exit

Session Stats
Correct guesses: 4
Incorrect guesses: 1
Answer percentage: 80.0%
Average time spent per question: 11.08 seconds

Bye!
```


