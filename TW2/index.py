tutor_name = "Olga"
module = "CFS"
print(f"Hello, My name is {tutor_name} and I'm teaching {module}")

student_id = input("Enter your ID: ")
print(f"Hello, Ms. {tutor_name}, I'm your student and my id is: {student_id} ")

first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
operand = input("Enter operator: ")

if operand == "+":
	print(f"The result is: {first_num + second_num}")
elif (operand == "-"):
	print(f"The result is: {first_num - second_num}")
elif operand == "*":
	print(f"The result is: {first_num * second_num}")
elif operand == "/":
	print(f"The result is: {first_num / second_num}")
elif operand == "**":
	print(f"The result is: {first_num ** second_num}")
elif operand == "//":
	print(f"The result is: {first_num // second_num}")
elif operand == "%":
	print(f"The result is: {first_num % second_num}")
else:
	print("Choose one of the following operands: +, -, *, /, **, //, %")

lesson = 0
def myfunc():
	global lesson
	lesson+=1
	print(lesson)

myfunc()
myfunc()
myfunc()
myfunc()