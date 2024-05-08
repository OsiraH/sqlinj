import sqlite3

def get_user_info(user_input):
 # Connect to the database

 conn = sqlite3.connect('users.db')
 cursor = conn.cursor()

 # Build and execute a SQL query to retrieve user information
 # sqlite doesn't have prepared statement objects, but supports parametized queries
 query = f"SELECT * FROM users WHERE name = ?"
 input_to_search = [user_input]
 cursor.execute(query, input_to_search)

 # Fetch and return the results
 results = cursor.fetchall()
 conn.close()
 return results

# Example usage:
user_input = input("Enter your username: ")
user_info = get_user_info(user_input)

#implicit booleanness in python
if not user_info:
    print("no user found")
else:
    print(user_info)
