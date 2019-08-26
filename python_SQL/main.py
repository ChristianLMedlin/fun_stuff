import sqlite3

connection = sqlite3.connect('practice.db')
c = connection.cursor()

# c.execute(
# '''
# CREATE TABLE Hospital (Hospital_Id INT UNSIGNED NOT NULL , Hospital_Name TEXT NOT NULL , Bed_Count INT)
# '''
# )

# c.execute(
# '''
# INSERT INTO 'Hospital' ('Hospital_Id', 'Hospital_Name', 'Bed_Count') VALUES 
# ('1', 'Mayo Clinic', '200'), 
# ('2', 'Cleveland Clinic', '400'), 
# ('3', 'Johns Hopkins', '1000'), 
# ('4', 'UCLA Medical Center', '1500')
# '''
# )

connection.commit()

