from sympy import symbols, diff, solve

# Define the symbol x
x = symbols('x')

# Define the loss function
L = 3 * x**2 + 2 * x - 5

# Calculate the gradient (first derivative)
gradient = diff(L, x)

# Calculate the second derivative
second_derivative = diff(gradient, x)

# Find the optimal solution (gradient = 0)
optimal_x = solve(gradient, x)[0]

print(f"Optimal x (gradient = 0): {optimal_x}")

# Check if it's a minimum or maximum using the second derivative
second_deriv_val = second_derivative.subs(x, optimal_x)

if second_deriv_val > 0:
  print("The optimal solution is a minimum.")
elif second_deriv_val < 0:
  print("The optimal solution is a maximum.")
else:
  print("The second derivative is zero, inconclusive.")

#Verify the gradient at the optimal x.
gradient_at_optimal = gradient.subs(x, optimal_x)
print(f"Gradient at optimal x: {gradient_at_optimal}")

#Verify the Loss at the optimal x.
loss_at_optimal = L.subs(x, optimal_x)
print(f"Loss at optimal x: {loss_at_optimal}")