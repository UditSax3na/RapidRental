# program to create second table
import mysql.connector as ms
mycon = ms.connect(host='localhost',user='root',passwd='',database='rapidrental')
cur=mycon.cursor()
cur.execute('''create table items
(   modelno int not null,
    Item varchar(40),
    TYPE varchar(5) ,
    avail char(3) default 'NO',
    hours int default 1,
    price int )''')
cur.execute('''insert into items values(1010,'HERO HONDA','BIKE','YES',1,1200),(1011,'HONDA AMAZE','CAR','YES',1,5000),(1013,'DIAMOND BLACK BACK','CYCLE','YES',1,1200)''')
mycon.commit()
mycon.close()
