# Calculate your life left in weeks from 90 years

def life_in_weeks(age):
    weeks = (90-age)*52
    print(f"You have {weeks} weeks left.")

age = int(input("Enter your current age in years: "))
life_in_weeks(age)