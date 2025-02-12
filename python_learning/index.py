
# Function to calculate the perimeter of a triangle
def calculate_perimeter(a, b, c):
    return a + b + c

# Input lengths of the sides of the triangle
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Calculate the perimeter
perimeter = calculate_perimeter(side1, side2, side3)

# Output the result
print(f"The perimeter of the triangle is: {perimeter}")