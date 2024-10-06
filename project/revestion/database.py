'''import psycopg2

# Establish a connection to the PostgreSQL database
connection = psycopg2.connect(
    dbname='person',
    user='test',
    password='test123',
    host='localhost',
    port='5432'
)

# Create a cursor object
cursor = connection.cursor()

# Define a select query
delete_query = """
    DELETE FROM person
    WHERE first_name = 'jane'
"""
# Execute the query
cursor.execute(delete_query)
connection.commit()
print("Record deleted successfully")
# Close cursor and connection
cursor.close()
connection.close()'''

import requests

new_article = {
    "id": 4,
    "projectID": 8,
    "projectName": "Hospital Management System",
    "dateOfStart": "2024-07-25",
    "teamSize": 2
}

response = requests.post('http://127.0.0.1:8000/my/post', json=new_article)
if response.status_code == 201:
    print('POST Response:', response.json())
else:
    print('Failed to create article:', response.status_code, response.text)


