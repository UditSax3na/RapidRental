# program to create database and table
import mysql.connector as ms
mycon = ms.connect(host='localhost',user='root',passwd='')
cur=mycon.cursor()
# cur.execute('create database rapidrental')
cur.execute('use rapidrental')
cur.execute('''create table custrecord
(   BILLNO int not null,
    CUSTOMER varchar(40) not null,
    DOHR date not null,
    PHONENO int not null,
    Item varchar(40),
    hours int default 1,
    TOTALPRICE int )''')
mycon.close()