# Filename: hide_secretkeys.py
# Description: Hide secret keys and passwords in environment variables
# Date: 04-03-2025

# Create environment variable
# Close the IDE (vscode)

import os


# Access the environment variable
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")


# These variables are only in our system
print(db_user)
print(db_password)
