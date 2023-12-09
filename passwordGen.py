import random


characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

pass_length = int(input("Enter the length of required password: "))
pass_count = int(input("Enter the number of required passwords:"))

for i in range (0,pass_count):
	password = ""
	for j in range (0,pass_length):
		pass_char = random.choice(characters)
		password = password+pass_char
	print("The generated Password is:",password)