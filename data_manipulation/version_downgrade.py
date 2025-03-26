import nbformat

# Load the notebook in the highest available version
with open("C:/Users/Oliver/Desktop/Scientific_Computing/data_manipulation/data_assignment.ipynb", "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=nbformat.NO_CONVERT)  # Load without enforcing version

# Downgrade to version 4
nb.nbformat = 4
nb.nbformat_minor = 4  # Ensures compatibility with version 4 notebooks

# Save the downgraded notebook
output_path = "C:/Users/Oliver/Desktop/Scientific_Computing/data_manipulation/data_assignment_v4.ipynb"
with open(output_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print(f"Notebook successfully downgraded to version 4 at {output_path}")
