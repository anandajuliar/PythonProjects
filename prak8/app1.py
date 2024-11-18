import sqlite3

con = sqlite3.connect("DB1.db")

cur = con.cursor()

a=int(input('masukan nomor: '))

b= input('masukan nama: ')

cur.execute("""
    INSERT INTO TBL1 VALUES
        ({},'{}')
""".format(a,b))

con.commit()