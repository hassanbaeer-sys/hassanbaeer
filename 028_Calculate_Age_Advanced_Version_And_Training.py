# -------------------------------------------------
# -- Calculate Age Advanced Version and Training --
# -------------------------------------------------

# Write A Very Beautiful Note
print("#" * 80)
print(" You Can Write The Frist Letter or Full Name of The Time Unit ".center(80,'#') )
print("#" * 80)

# Collect Age Data
age = input("please Enter Your Age :").strip()

# Collect Time Unit Data
unit = input("Please Choose Time Unit : Monthes , Weeks , Days , Hours . ").strip().lower()

# Get Time Units
monthes = int(age)* 12
weeks   = monthes * 4 
days    = int(age)*365
hours   = days * 24

if unit == "monthes" or unit == "m" :
    print(f"Your Age by Monthes = {monthes} Monthes")

elif unit == "weeks" or unit == "w" :
    print(f"Your Age by weeks = {weeks:,} Weeks")

elif unit == "days" or unit == "d":
    print(f"Your Age by Days = {days:,} Days")

elif unit == "hours" or unit == "h" :
    print(f"Your Age by Hours = {hours:,} Hours")

else :
    print ("Invalid Value. Please Enter The Correct Unit  ")