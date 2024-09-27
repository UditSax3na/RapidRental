# program to create database and table :- rapidrental and custrecord
import mysql.connector as ms
mycon = ms.connect(host=HOST,user=USERNAME,passwd=PASSWORD)
cur=mycon.cursor()
cur.execute('create database rapidrental')
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