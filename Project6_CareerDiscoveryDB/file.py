'''
Goal: 
(1) Develop a 'career discovery algorithm' using web-scraping and data mining for the aims of (a) what's out there? and (b) analyze what career may be a good fit for me, meaning I have aptitude for the job, the job pays well, and most importantly the social and mental requirements will not over-stress me to the point of burning out again.
(2) Support this with a database of potential career paths, scored by "good-fit" categories.
(3) The idea is to fill the database first, then apply different analyses of career best-fits to the data.

Database columns: Title, Field, Salary, Employment, Cooperative, Low-stress, Stimulating, Personal_Value, Sexiness
    'Title': the title of the position
    'Field': the career type or field. e.g. software
    'Salary': annual income
    'Employment': ('Hi/Med/Low') the availability of this job, measured by total number of positions versus candidates seeking the position
    'Cooperative': the degree to which this job promotes an environment of working together versus competing against co-workers.
    'Stress': ('Hi/Med/Low') 
    'Stimulating': ('Hi/Med/Low') the degree to which this job presents new experiences and challenges on a daily basis.
    'Personal_Value': ('Hi/Med/Low') how much do I feel I'm contributing to a cause or effort that I value?
    'Sexiness': ('Hi/Med/Low') to what degree will the job be perceived as 'attractive' versus 'repulsive' by potential mates?

'''

import sqlite3 as sql

class Database:

    def __init__(self, db):
        self.conn=sql.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS career (id INTEGER PRIMARY KEY, title text, field text, salary integer, employment integer, cooperative integer, stress integer, stimulating integer, personal_value integer, sexiness integer)")
        self.conn.commit()


    def insert(self, title, field, salary, employment, cooperative, stress, stimulating, personal_value, sexiness):
        self.cur.execute("",())
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM career")
        rows=self.cur.fetchall()
        return rows

    def update(self, id, title, field, salary, employment, cooperative, stress, stimulating, personal_value, sexiness):
        self.cur.execute("UPDATE career SET title=?, field=?, salary=?, employment=?, cooperative=?, stress=?, stimulating=?, personal_value=?, sexiness=? WHERE id=?", (title, field, salary, employment, cooperative, stress, stimulating, personal_value, sexiness, id))
        self.conn.commit()

    def delete(self,id):
        self.cur.execute("DELETE FROM career WHERE id=?", (id,))
        self.conn.commit()

    def __del__(self,):
        self.conn.close()

db = Database('careers')
db.insert("Software Developer", "Software", 80, 1, 1, 1, 1, 0, 1)
print(db.view())