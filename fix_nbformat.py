import os
import json

# Walk through all directories and subdirectories starting from the current folder
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".ipynb"):  # Only process Jupyter notebook files
            file_path = os.path.join(root, file)
            try:

                # Open the notebook file and load its JSON content
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)

                # Check if the notebook format version is 5, and downgrade it to
                if data.get("nbformat", 4) == 5:
                    data["nbformat"] = 4
                    print(f"✓ Downgraded: {file_path}")
                else:
                    print(f"- Already ok: {file_path}")

                 # Save the modified notebook back to the file
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)

            except Exception as e:
                # Handle errors like corrupt files or permission issues
                print(f"✗ Error processing {file_path}: {e}")
