# !!!WARNING!!! the script is written by AI and is not checked. i tested once, it seems to work properly.
# the script installs libs from requirements.txt

import subprocess
import sys

# List of libraries to install
libraries = [
    "Django==3.2.16",
    "pep8-naming==0.13.3",
    "pytest==7.1.3",
    "pytest-django==4.5.2",
    "pytest-pythonpath==0.7.3",
    "flake8==5.0.4",
    "flake8-docstrings==1.7.0"
]

# Check if script is being run in a virtual environment
if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
    print("Error: You are not inside a virtual environment.")
    print("Please activate your virtual environment and try again.")
    sys.exit(1)

# Install each library
for lib in libraries:
    print(f"Installing {lib}...")
    result = subprocess.run([sys.executable, "-m", "pip", "install", lib], capture_output=True, text=True)

    # Check for success or failure
    if result.returncode == 0:
        print(f"Successfully installed {lib}.\n")
    else:
        print(f"Failed to install {lib}. Error:\n{result.stderr}\n")

# copy this to run server:
# python blogicum/manage.py runserver
# python blogicum\manage.py runserver