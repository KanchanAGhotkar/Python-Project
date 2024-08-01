import datetime
import csv
import pandas as pd

def zodiac_sign(day, month):

    if month == "december" and day>22:
        astro_sign = "Sagittarius"
    elif month == "january" and day >20:
        astro_sign = "Capricorn"
    elif month == "february" and day >19:
        astro_sign = "Aquarius"
    elif month == "March" and day > 21:
        astro_sign = "Aries"
    elif month == "April" and day > 20:
        astro_sign = "Taurus"
    elif month == "May" and day >21:
            astro_sign = "Gemini"
    elif month == "June" and day > 21:
        astro_sign = "Cancer"
    elif month == "July" and day > 23:
        astro_sign = "lio"
    elif month == "August" and day > 23:
            astro_sign = "Virgo"
    elif month == "September" and day >23:
            astro_sign = "Libra"
    elif month == "October" and day > 23:
        astro_sign = "Scorpio"
    elif month == "November" and day > 23 :
        astro_sign = "Sagittarius"
    print(astro_sign)
    
    #def userInput(name, day, month)
#taking user input
    name = input("Enetr your name: ")
    dateOfBirth_str = input("Enter your date of birth in (YYYY/MM/DD)")
    # Step 3: Determine the Zodiac Sign
birthdate = datetime.strptime(dateOfBirth_str, "%Y-%m-%d")
zodiac_sign = get_zodiac_sign(birthdate.day, birthdate.month)
data = {
    "Name": [name],
    "Birthdate": [dateOfBirth_str],
    "Zodiac Sign": [zodiac_sign]
}
df = pd.DataFrame(data)

# Step 5: Save the DataFrame to a CSV File
filename = 'zodiac_signs_data.csv'
df.to_csv(filename, mode='a', header=not pd.io.common.file_exists(filename), index=False)

print(f"{name}'s zodiac sign ({zodiac_sign}) has been saved to '{filename}'.")
        

        
        

        