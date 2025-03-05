import sympy as sp

# Define the matrix A
A = sp.Matrix([[2, 1], [1, 3]])

# Calculate the symbolic determinant of A
determinant_A = A.det()
print(f"Determinant of A: {determinant_A}")

# Find the eigenvalues of A
eigenvalues = A.eigenvals()
print(f"Eigenvalues of A: {eigenvalues}")

# Extract the eigenvalues (keys of the dictionary)
eigenvalues_list = list(eigenvalues.keys())

# Verify the characteristic equation
x = sp.Symbol('x')
characteristic_equation = (A - x * sp.eye(2)).det() # |A-xI| = 0

print(f"Characteristic Equation: {characteristic_equation}")

# Verify that the eigenvalues satisfy the characteristic equation
for eigenvalue in eigenvalues_list:
    result = characteristic_equation.subs(x, eigenvalue)
    print(f"Characteristic equation at eigenvalue {eigenvalue}: {result}")
    if result == 0:
        print(f"Eigenvalue {eigenvalue} satisfies the characteristic equation.")
    else:
        print(f"Eigenvalue {eigenvalue} does not satisfy the characteristic equation.")