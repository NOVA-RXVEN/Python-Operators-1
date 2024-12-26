print("Enter Marks Obtained in 4 Subjects: ")

Math = int(input("Maths :"))
English = int(input("English :"))
Science = int(input("Science :"))
Bangla = int(input("Bangla :"))

sum = Math + English + Science + Bangla
print(f"Total Marks : {sum}")

perc = (sum/400) * 100

print(f"Percentage Mark = {perc}")