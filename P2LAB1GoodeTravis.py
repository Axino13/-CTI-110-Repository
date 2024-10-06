# Travis Goode
# 10/6/2024
# Assignment Name: P2lab1
# Using the radius finds the Diameter, circumference, and area of a circle.

# Get the radius from the user
radius = float(input("What is the radius of the circle: "))

# Calculate diameter, circumference, and area
diameter = 2 * radius
circumference = 2 * 3.14159 * radius  
area = 3.14159 * radius ** 2

# Display the results
print()
print(f"The diameter of the circle is: {diameter:.1f}")
print()
print(f"The circumference of the circle is: {circumference:.2f}")
print()
print(f"The area of the circle is: {area:.3f}")
