import sqlite3
# Connect to SQlite
connection = sqlite3.connect("student.db")

# Create a cursor object to insert record,create table
cursor = connection.cursor()
# Create a table
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
"""
cursor.execute(table_info)

# Insert some more records
cursor.execute('''Insert Into STUDENT values('Aqsa','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Aliza','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Kareena','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Ishu','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Disha','DEVOPS','A',35)''')
# Display all the records
print("The inserted records are ")

data = cursor.execute('''select * from STUDENT''')

for row in data:
    print(row)
    
# Close the connection
connection.commit()
connection.close()
