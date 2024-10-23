# Semi-final Exam 
# Author : Michaella Mae M. Estrella

print("==========================================")
print("         ~ Record Keeping App ~")
print("==========================================")
print("Available Operators:")
print("A) Add Data\t\tB) Delete Data")
print("C) End")
print()
selection = str(input("Select an option [A,B,C]: "))

try:
 File <main.py> module>  open("record.txt", "r")
except FileNotFoundError:
    file = open("record.txt", "x")

if selection.upper() == "A":
    var1 = str(input("Michaella Mae: "))
    var2 = str(input("Estrella: "))
    file = open("record.txt", "a")
    file.write(f"\n{var1}, {var2}")
    file.close()
elif selection.upper() == "B":
    file = open("record.txt", "r")
    print(file.read())
    file.close()
elif selection.upper() == "C":
    print("Thank you")
else:
    print("Invalid input.")
