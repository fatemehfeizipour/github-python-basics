name = input("what is your name? ")
age = int(input("How old are you?"))

print(f"\nHello {name} ")
print(f"Next year, you will be {age + 1 } years old.")

if age >=18:
	print("You are an adult")
else:
	print("You are under 18")