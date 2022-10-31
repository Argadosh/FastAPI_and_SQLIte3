import sqlite3

db = sqlite3.connect('student.db')

c = db.cursor()
# c.execute("""CREATE TABLE student(
#     name text,
#     surname text,
#     GPA float
# )""")

# c.execute("""INSERT INTO student VALUES
#     ('Vanya','Nikitin','3.2'),
#     ('Vanya','Smirnov','3.3'),
#     ('Dmitriy', 'Ivanov', 3.2),
#     ('Dmitriy','Sobolev','2.3'),
#     ('Dmitriy','Sokolov','4.1'),
#     ('Evgeniy','Lazarev','2.1'),
#     ('Evgeniy','Tarasov','2.7'),
#     ('Ekaterina', 'Ivanova', 4.1),
#     ('Ekaterina','Nikitina','4.7'),
#     ('Nastya','Lavrova','3.7'),
#     ('Nastya','Ponomareva','4.3'),
#     ('Nikita','Bykov','4.1'),
#     ('Nikita','Korolev','3.0'),
#     ('Olga','Kotova','3.1'),
#     ('Olga','Maslova','3.6'),
#     ('Olga','Ponomareva','4.9')
# """)

enter_name = (input())

c.execute("SELECT rowid, * FROM student WHERE name = ?", (enter_name,))
print(c.fetchall())

db.commit()


db.close()
