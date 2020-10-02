import sqlite3 
conector = sqlite3.connect('aulaDB.db')
cursor = conector.cursor()
sql = """
CREATE TABLE pessoa (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome varchar(60) NOT NULL,
    nascimento date NOT NULL
);
"""

cursor.execute(sql)

sql = """
INSERT INTO pessoa (nome, nascimento) 
VALUES	('dennis','1997-07-31'),
		('priscila','2000-08-14'),
        ('beltrano','2001-01-07'),
        ('fulana','2006-09-19'),
        ('ciclano','1991-02-22');
"""

cursor.execute(sql)
conector.commit()
cursor.close()
conector.close()