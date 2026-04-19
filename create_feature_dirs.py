import os

# Define all necessary directories
directories = [
    r"c:\Users\HP\Desktop\PROJECT\lib\shared\models",
    r"c:\Users\HP\Desktop\PROJECT\lib\features\camera\presentation\screens",
    r"c:\Users\HP\Desktop\PROJECT\lib\features\camera\presentation\providers",
    r"c:\Users\HP\Desktop\PROJECT\lib\features\camera\presentation\widgets",
    r"c:\Users\HP\Desktop\PROJECT\lib\features\food\presentation\screens",
    r"c:\Users\HP\Desktop\PROJECT\lib\features\food\presentation\providers",
    r"c:\Users\HP\Desktop\PROJECT\lib\features\food\presentation\widgets",
    r"c:\Users\HP\Desktop\PROJECT\lib\features\profile\presentation\screens",
    r"c:\Users\HP\Desktop\PROJECT\lib\features\profile\presentation\providers",
    r"c:\Users\HP\Desktop\PROJECT\lib\features\health\presentation\screens",
    r"c:\Users\HP\Desktop\PROJECT\lib\features\health\presentation\providers",
    r"c:\Users\HP\Desktop\PROJECT\lib\features\settings\presentation\screens",
    r"c:\Users\HP\Desktop\PROJECT\lib\features\settings\presentation\providers",
    r"c:\Users\HP\Desktop\PROJECT\lib\core\constants",
]

# Create all directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)
    print(f"Created: {directory}")

print("\nAll directories created successfully!")
