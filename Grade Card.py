print("╔══════════════════════════════════╗")
print("║          🎓 GRADE CARD           ║")
print("╚══════════════════════════════════╝")

name = input("\nEnter student name: ")
roll_no = input("Enter roll number: ")

print("\nEnter marks out of 100:")

python = float(input("Python: "))
dbms = float(input("DBMS: "))
ai = float(input("AI: "))
maths = float(input("Mathematics: "))
english = float(input("English: "))

# Calculate total and average
total = python + dbms + ai + maths + english
average = total / 5

# Find grade
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Pass / Fail
if average >= 40:
    status = "PASS ✅"
else:
    status = "FAIL ❌"

# Display Grade Card
print("\n")
print("╔══════════════════════════════════╗")
print("║          🎓 GRADE CARD           ║")
print("╠══════════════════════════════════╣")
print(f"║ Student : {name:<22} ║")
print(f"║ Roll No : {roll_no:<22} ║")
print("╠══════════════════════════════════╣")
print(f"║ Python       : {python:>6.1f}             ║")
print(f"║ DBMS         : {dbms:>6.1f}             ║")
print(f"║ AI           : {ai:>6.1f}             ║")
print(f"║ Mathematics  : {maths:>6.1f}             ║")
print(f"║ English      : {english:>6.1f}             ║")
print("╠══════════════════════════════════╣")
print(f"║ Total        : {total:>6.1f} / 500       ║")
print(f"║ Average      : {average:>6.1f}%          ║")
print(f"║ Grade        : {grade:<22} ║")
print(f"║ Status       : {status:<22} ║")
print("╚══════════════════════════════════╝")