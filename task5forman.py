print("Mifflin - San Geora Formula for Men", '\n')

weightKg = input("What is the patient's weight in KG? ")
weightKg = float(weightKg)

heightCm = input("What is the height of the patient in CM? ")
heightCm = float(heightCm)

age = input("What is the age of the patient? ")
print('\n')
age = float(age)
formula = (10 * (weightKg)) + (6.25 * (heightCm)) - (5 * (age)) + 5
formula = str(formula)

pyhy_act = input(
    "Do you have physical activitiy or sedentary work? (Y or N): ").lower()
if pyhy_act == "n":
    formula = float(formula) * 1.2
else:
    formula = formula

excersize = input(
    "Are you jogging or making light excersicez 1-3 times in a week? (Y or N): "
).lower()
if excersize == "y":
    formula = float(formula) * 1.375
else:
    formula = formula

sports = input(
    "Are you doing sports with medium loads 3-5 times a week? (Y or N): "
).lower()
if sports == "y":
    formula = float(formula) * 1.55
else:
    formula = formula

training = input(
    "Are you doing fully train 6-7 times a week= (Y or N): ").lower()
if training == "y":
    formula = float(formula) * 1.725
else:
    formula = formula

work_type = input(
    "If your work is associated with physical labor and you train 2 times a day include strenght training according to your training program press Y. (Y or N): "
).lower()
if work_type == "y":
    formula = float(formula) * 1.9
else:
    formula = formula

print(f'The MB (Kcal between Day) of the patient is =' + str(formula))
