import math

# Function to calculate the area of a rectangle
def rectangle_area(length, width):
    return length * width

# Function to calculate the area of a circle
def circle_area(radius):
    return math.pi * radius ** 2

# Function to calculate the volume of a sphere
def sphere_volume(radius):
    return (4/3) * math.pi * radius ** 3

# Function to convert Fahrenheit to Celsius
def to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Function to convert Celsius to Fahrenheit
def to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to solve a quadratic equation
def quadratic(a=1, b=-7, c=10):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        return "No real roots"

# Function to calculate the distance between two points
def distance (x1=1, y1=1, x2=4, y2=5):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to print all the information using the suggested test values
def print_test_values():
    print(f"Rectangle area L=12,W=13): {rectangle_area(12, 13)} square units")
    print(f"Circle area r=5: {circle_area(5):.2f} square units")
    print(f"Sphere volume r=9: {sphere_volume(9):.2f} cubic units")
    print(f"100°C to Fahrenheit: {to_fahrenheit(100):.2f}°F")
    print(f"0°C to Fahrenheit: {to_fahrenheit(0):.2f}°F")
    print(f"212°F to Celsius: {to_celsius(212):.2f}°C")
    print(f"32°F to Celsius: {to_celsius(32):.2f}°C")
    print(f"Quadratic roots a=1, b=-7, c=10: {quadratic(1, -7, 10)}")
    print(f"Quadratic roots a=1, b=-1, c=-2: {quadratic(1, -1, -2)}")
    print(f"Distance (2, 5) to (7, 17): {distance(2, 5, 7, 17):.2f} units")
    print(f"Distance default points (1, 1) to (4, 5): {distance():.2f} units")
    print("Thank you for testing ")

if __name__ == '__main__':
    print_test_values()
