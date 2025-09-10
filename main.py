import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")


if db_password:
    print("😞Success! The .env file is working. 🎉")
    print(f"PostgreSQL User: {db_user}")
    print(f"PostgreSQL Password: {db_password}")
else:
    print("Error! The .env file is not working or the variable is not set. 😞")


print("\nDocker is likely running if you were able to start the services.")