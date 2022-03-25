import sqlite3

def to_cat_dict(cat_tuple):
    cat = {'item_num':cat_tuple[0], 'amount':cat_tuple[1], 'category':cat_tuple[2], 'date':cat_tuple[3], 'desc':cat_tuple[4]}
    return cat

def to_cat_dict_list(cat_tuples):
    ''' convert a list of category tuples into a list of dictionaries'''
    return [to_cat_dict(cat) for cat in cat_tuples]

class Transaction():
    ''' Transaction represents a table of financial transactions'''

    def __init__(self,dbfile):
        con= sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (amount integer, category text, date date, desc text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile

    def select_all(self):
        ''' return all of the categories as a list of dicts.'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict_list(tuples)

    def select_one(self,rowid):
        ''' return a category with a specified rowid '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions where rowid=(?)",(rowid,) )
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict(tuples[0])

    def add(self,item):
        ''' add a category to the categories table.
            this returns the rowid of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?)",(item['amount'], item['category'], item['date'], item['desc']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    def update(self,rowid,item):
        ''' add a category to the categories table.
            this returns the rowid of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''UPDATE categories
                        SET name=(?), desc=(?)
                        WHERE rowid=(?);
        ''',(item['name'],item['desc'],rowid))
        con.commit()
        con.close()

    def delete(self,rowid):
        ''' add a category to the categories table.
            this returns the rowid of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''DELETE FROM transactions
                       WHERE rowid=(?);
        ''',(rowid,))
        con.commit()
        con.close()

    #Ben
    def select_date(self,date):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions where date=(?)",(date,) )
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict_list(tuples)

#Ava
    def select_month(self,month):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions where strftime('%m', date)=(?)",(month,))
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict_list(tuples)

    #Zach
    def select_year(self,y):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions where strftime('%Y', date)=(?)",(y,))
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict_list(tuples)
    
    #Eric
    def select_cat(self,c):
        ''' return a category with a specified category '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions where category=(?)",(c,) )
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict_list(tuples)