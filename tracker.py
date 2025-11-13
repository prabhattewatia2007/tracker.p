#
#name:prabhat tewatia
#date:11/11/2025
#
print("Welcome to the Daily Calorie Tracker CLI!")
print("This tool helps you track your daily meals and total calorie intake.\n")
# Collect user input for number of meals
num_meals = int(input("How many meals do you want to log today? "))

meal_names = []
meal_calories = []

for i in range(num_meals):
    meal = input(f"Enter name of meal {i+1}: ")
    calories = float(input(f"Enter calories for {meal}: "))
    meal_names.append(meal)
    meal_calories.append(calories)

print("\nMeals and calorie data recorded successfully!\n")
# Calculate total and average
total_calories = sum(meal_calories)
average_calories = total_calories / num_meals

# Ask for daily limit
daily_limit = float(input("Enter your daily calorie limit: "))

print(f"\nYour total calorie intake is {total_calories:.2f} calories.")
print(f"Average calories per meal: {average_calories:.2f}")
if total_calories > daily_limit:
    print("⚠️ Warning: You have exceeded your daily calorie limit!")
else:
    print("✅ Great job! You are within your daily calorie limit.")
print("\n------- Daily Calorie Summary -------")
print("Meal Name\tCalories")
print("------------------------------------")
for i in range(num_meals):
    print(f"{meal_names[i]}\t\t{meal_calories[i]}")

print("------------------------------------")
print(f"Total:\t\t{total_calories:.2f}")
print(f"Average:\t{average_calories:.2f}")
print("------------------------------------\n")
import datetime

save = input("Do you want to save this session to a file? (yes/no): ").strip().lower()

if save == "yes":
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = "calorie_log.txt"

    with open(filename, "w") as file:
        file.write(f"Calorie Tracker Log - {timestamp}\n\n")
        file.write("Meal Name\tCalories\n")
        file.write("------------------------------------\n")
        for i in range(num_meals):
            file.write(f"{meal_names[i]}\t\t{meal_calories[i]}\n")
        file.write("------------------------------------\n")
        file.write(f"Total:\t\t{total_calories:.2f}\n")
        file.write(f"Average:\t{average_calories:.2f}\n")
        file.write(f"Daily Limit:\t{daily_limit}\n")
        if total_calories > daily_limit:
            file.write("Status: Exceeded Limit ⚠️\n")
        else:
            file.write("Status: Within Limit ✅\n")

    print(f"\nSession saved successfully in {filename}!")
Welcome to the Daily Calorie Tracker CLI!
This tool helps you track your daily meals and total calorie intake.

How many meals do you want to log today? 3
Enter name of meal 1: Breakfast
Enter calories for Breakfast: 400
Enter name of meal 2: Lunch
Enter calories for Lunch: 600
Enter name of meal 3: Dinner
Enter calories for Dinner: 500

Meals and calorie data recorded successfully!

Enter your daily calorie limit: 1500

Your total calorie intake is 1500.00 calories.
Average calories per meal: 500.00
✅ Great job! You are within your daily calorie limit.

------- Daily Calorie Summary -------
Meal Name   Calories
------------------------------------
Breakfast   400.0
Lunch       600.0
Dinner      500.0
------------------------------------
Total:      1500.00
Average:    500.00
------------------------------------

Do you want to save this session to a file? yes
Session saved successfully in calorie_log.txt!
