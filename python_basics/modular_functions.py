import math

# Function to calculate area of different shapes
def calculate_area(shape, dimension1, dimension2=0):
    if shape == "circle":
        area = math.pi * (dimension1 ** 2)
    elif shape == "rectangle":
        area = dimension1 * dimension2
    elif shape == "triangle":
        area = 0.5 * dimension1 * dimension2
    else:
        raise ValueError("Invalid shape. Supported shapes are 'circle', 'rectangle', and 'triangle'.")
    return area

# Test the function with the different shapes
circle_area = calculate_area("circle", 9)  # Radius
rectangle_area = calculate_area("rectangle", 7, 15)  # Length , Width
triangle_area = calculate_area("triangle", 4, 10)  # Base, Height

# Print the results
print(f"Area of the circle: {circle_area:.2f}")
print(f"Area of the rectangle: {rectangle_area:.2f}")
print(f"Area of the triangle: {triangle_area:.2f}")