# Q1
print("+--------------+")
print("|CHOON YEAN HEE|")
print("+--------------+")

# Q2
print("  ////// ")
print(" | o o | ")
print("(|  ^  |)")
print(" | [_] | ")
print(" ------- ")

# Q3
print("FFFFFFFF U       U NN    NN")
print("FF       U       U NNN   NN")
print("FFFFFFFF U       U NN N  NN")
print("FF        U     U  NN  N NN")
print("FF          UUU    NN   NNN")

# Q4
print("+---+---+---+")
print("| X |   | O |")
print("+---+---+---+")
print("|   | X | O |")
print("+---+---+---+")
print("|   |   | O |")
print("+---+---+---+")

# Q5 (comma style)
print("x" + "\t" + "X^2" + "\t" + "x^3")
x = 1
print(x, "\t", pow(x,2), "\t", pow(x,3))
x = 2
print(x, "\t", pow(x,2), "\t", pow(x,3))
x = 3
print(x, "\t", pow(x,2), "\t", pow(x,3))
x = 4
print(x, "\t", pow(x,2), "\t", pow(x,3))

# Q5 (string casting style)
print("x" + "\t" + "X^2" + "\t" + "x^3")
x = 1
print(str(x) + "\t" + str(pow(x,2)) + "\t" + str(pow(x,3)))
x = 2
print(str(x) + "\t" + str(pow(x,2)) + "\t" + str(pow(x,3)))
x = 3
print(str(x) + "\t" + str(pow(x,2)) + "\t" + str(pow(x,3)))
x = 4
print(str(x) + "\t" + str(pow(x,2)) + "\t" + str(pow(x,3)))
print()

# Q6
# format() -> "{:.2f}".format(result)
# round() -> round(result,2)
# % -> "%.2f"% result
# f-string -> f{result:.2f}
result = (9.5 * 4.5 - 2.5 / 3) / (45.5 - 3.5)
print("{:.2f}".format(result))

# Q7
# getting input using input() function
# the value in string format, number must conver from string to number
# int() - integer, float() - decimal number
name = input("Enter Name: ")
age = int(input("Enter Age : "))
print(name, " is ", age, " years old now.")
print()

# Q8
celcius = float(input("Enter a degree in Celcius: "))
fahrenheit = (9/5) * celcius + 32
print(celcius, "Celcius is ", fahrenheit, "fahrenheit.")
print()

# Q9
import math
PI = math.pi
radius = int(input("Enter a radius of cylinder: "))
height = int(input("Enter a height of cylinder: "))
surface_area = 2 * PI * radius * height + 2 * PI * radius * radius
volume = PI * radius * radius * height

print("It's surface area and volume are", round(surface_area,5), " and ", round(volume,5), "respectively.")

# Q10
x = int(input("Enter a number between 0 and 1000: "))
result = (x % 10) + (x // 10 % 10) + (x // 100 % 10)
print("The sum of the digit is", result)

# Q11
ANNUAL_INTEREST_RATE = 0.05
monthly_interest = ANNUAL_INTEREST_RATE / 12

saving_base = float(input("Enter the montly saving amount: "))

total = saving_base * (1 + monthly_interest)
total = saving_base + total * (1 + monthly_interest)
total = saving_base + total * (1 + monthly_interest)
total = saving_base + total * (1 + monthly_interest)
total = saving_base + total * (1 + monthly_interest)
total = saving_base + total * (1 + monthly_interest)
print(f"After the sixth month, the account value is RM {total:.2f}")

# Q12
print("Equation 1: ax + by = e")
print("Equation 2: cx + dy = f")

print("Enter a numerical value for each of the following 6 variables:")
a = float(input("a= "))
b = float(input("b= "))
e = float(input("e= "))
c = float(input("c= "))
d = float(input("d= "))
f = float(input("f= "))

x = ((e * d) - (b * f)) / ((a * d) - (b * c))
y = ((a * f) - (e * c)) / ((a * d) - (b * c))

print("Equation 1: " + str(a) + "x + " + str(b) + "y = " + str(e))
print("Equation 2: " + str(c) + "x + " + str(d) + "y = " + str(f))
print()
print("x = ", x)
print("y = ", y)