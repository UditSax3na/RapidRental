'''program for the rapidrental company for renting the bike, car and bicycles for rent'''
#------------------------------THING THAT NEED TO IMPORT BEFORE MAIN PROGRAM STARTS ----------------------------------------#
from tkinter import *
import tkinter as ttk
import tkinter.ttk as abc
from tkinter import ttk
import mysql.connector as ms
from tkinter import messagebox
from GlobalVariables import *
#-------------------------------FUNCTIONS----------------------------------------#
def CMWin():     # SECOND WINDOW
    rrc.withdraw() 
    def hvhl():     # BIKE , CYCLE and CAR HIRING WINDOW
        def bikew():    # BIKE HIRING WINDOW
            def bikewin(): # BIKE HIRING
                Iname=bikedeck1.get()
                hour=hourdeck2.get()
                def ADDREC():       # ADDING RECORD INTO TABLE 
                    billno=int(E1.get())
                    customername=str(E2.get())
                    phoneno=int(E3.get())
                    itemname=E4.get()
                    hours=int(E5.get())
                    date=E6.get()
                    print(f'{E7.get()} and {type(E7.get())}')
                    totalprice=int(float(E7.get()))
                    mycon = ms.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
                    mycur = mycon.cursor()
                    SQ = '''INSERT into custrecord(BILLNO,CUSTOMER,DOHR,PHONENO,Item,hours,TOTALPRICE)values(%s,%s,%s,%s,%s,%s,%s)'''
                    tres = (billno,customername,date,phoneno,itemname,hours,totalprice)
                    mycur.execute(SQ,tres)
                    mycon.commit()
                    st='''Update Items set avail=%s where Item = %s'''
                    trd=('NO',itemname)
                    mycur.execute(st,trd)
                    mycon.commit()
                    mycon.close()
                    messagebox.showinfo("BOOKING STATUS","BOOKED SUCCESSFULLY")
                    BW.destroy()
                    sm.destroy()
    #-------------------------------------billing layout window for bikes starting--------------------------------------------------#
                BW = Toplevel()
                BW.title("BOOKING")
                BW.geometry("540x560") 
                BW.configure(background="Purple")
                LF=LabelFrame(BW, text="BILL", font="25", fg="white", bd=20, bg="Purple")
                lab1=Label(LF, text="BILL NO" ,font="25", bg="purple", fg="white")
                lab1.grid(row=1,column=1,padx=20,pady=20)
                lab2=Label(LF, text="CUSTOMER NAME",font="25", bg="purple", fg="white")
                lab2.grid(row=2,column=1,padx=20,pady=20)
                lab3=Label(LF, text="PHONE NO"  ,font="25", bg="purple", fg="white")
                lab3.grid(row=3,column=1,padx=20,pady=20)
                lab4=Label(LF, text="ITEM NAME" ,font="25", bg="purple", fg="white")
                lab4.grid(row=4,column=1,padx=20,pady=20)
                lab5=Label(LF, text="HOURS" ,font="25", bg="purple", fg="white")
                lab5.grid(row=5,column=1,padx=20,pady=20)
                lab8=Label(LF, text="DATE (yyyy-mm-dd)" ,font="25", bg="purple", fg="white")
                lab8.grid(row=6,column=1,padx=20,pady=20)
                lab7=Label(LF, text="TOTAL PRICE" ,font="25", bg="purple", fg="white")
                lab7.grid(row=7,column=1,padx=20,pady=20)

                E1=Entry(LF, width=30,font="25")
                E1.grid(row=1,column=2,padx=20,pady=20)
                E2=Entry(LF, width=30,font="25", )
                E2.grid(row=2,column=2,padx=20,pady=20)
                E3=Entry(LF, width=30,font="25")
                E3.grid(row=3,column=2,padx=20,pady=20)
                E4=Entry(LF, width=30,font="25")
                E4.grid(row=4,column=2,padx=20,pady=20)
                E4.insert(0,Iname)
                E5=Entry(LF, width=30,font="25")
                E5.grid(row=5,column=2,padx=20,pady=20)
                E5.insert(0,hour)
                E6=Entry(LF, width=30,font="25")
                E6.grid(row=6,column=2,padx=20,pady=20)
                mycon = ms.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
                mycur = mycon.cursor()
                mycur.execute('select curdate()')
                myres = mycur.fetchall()
                E6.insert(0,myres)
                Sq ='''select hours,price from items where Item=%s'''
                tres = (Iname,)
                mycur.execute(Sq,tres)
                mycod= mycur.fetchall()
                pr = mycod[0][1]/mycod[0][0]
                fhour=float(hour)
                tpr=pr*fhour
                E7=Entry(LF, width=30,font="25")
                E7.grid(row=7,column=2,padx=20,pady=20)
                E7.insert(0,tpr)
                LF.grid()
                bQ=Button(LF, text="PROCEED", bg='cyan',font="25", command=ADDREC)
                bQ.grid(row=8,column=1,padx=20,pady=20)
                bx=Button(LF, text="BACK", bg="red",font="25", command=BW.destroy)
                bx.grid(row=8,column=2,padx=20,pady=20)
    #----------------------------------------BIKE HIRING WINDOW LAYOUT----------------------------------------#

            sm = Toplevel()     # designing the BIKE BOOKING/HIRING window
            sm.title("BIKE BOOKING/HIRING")
            sm.geometry("680x600")
            sm.configure(background="Purple")
            frm=Frame(sm, bg="purple")
            frm.grid(row=1,column=1,pady=20,padx=20)
            Label(frm, text="BIKE", background="Purple", fg="White",font="Gabriola 50").grid()
            frm2=Frame(sm, bg="purple")
            frm2.grid(row=2,column=1,pady=20,padx=20)
            Label(frm2, text="SELECT BIKE :", background="Purple", fg="White",font="25").grid(row=1,column=1,padx=20,pady=20)
            L1=[]
            conn=ms.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
            mycur=conn.cursor()
            Sq ='''select Item from items where TYPE='BIKE' and avail='YES' '''  # THIS IS WHERE ONLY AVAILABLE ITEMS ARE SELECT INTO THE LIST SHOWN IN LAYOUT 
            mycur.execute(Sq)
            myres = mycur.fetchall()
            if len(myres[0]) == 0:
                L1=['Bikes are not available']
            else:
                for i in range(0,len(myres)):
                    a = myres[i][0]
                    L1.append(a)
                        
            mycur.close()
            conn.close()
            n=StringVar()
            bikedeck1=ttk.Combobox(frm2, width=30, textvariable=n,font="25")
            bikedeck1['values'] = L1
            bikedeck1.grid(row=1,column=2,padx=20,pady=20)
            bikedeck1.current()
            labh=Label(frm2, text="HOURS", bg="Purple", fg="white",font="25")
            labh.grid(row=2,column=1,padx=20,pady=20)
            hourdeck2 =Entry(frm2, width=30,font="25")
            hourdeck2.grid(row=2,column=2,padx=20,pady=20)
            frm3=Frame(sm, bg="purple")
            frm3.grid(row=3,column=1,pady=20,padx=20)
            but1=Button(frm3, text="SUBMIT",font="Gabriola 15 bold", bg='cyan', command=bikewin)
            but1.grid(row=1,column=1,pady=10,padx=100)
            blab2 = Button(frm3, text='BACK',font="Gabriola 15 bold", bg='cyan', command=sm.destroy)
            blab2.grid(row=1,column=2,pady=10,padx=100)
    #---------------------BIKE HIRING SECTION END HERE-----------------------------------------------------------#
    #------------------------------------CYCLE HIRING SECTION START HERE-----------------------------------------#
        def cyclew():   # CYCLE HIRING WINDOW 
            def cyclewin():# CYCLE HIRING WINDOW BILLING
                Iname=bikedeck1.get()
                hour=hourdeck2.get()
                def ADDREC():#  ADDING THE RECORD INTO THE TABLE 
                    billno=int(E1.get())
                    customername=E2.get()
                    phoneno=int(E3.get())
                    itemname=E4.get()
                    hours=int(E5.get())
                    date=E6.get()
                    totalprice=int(E7.get())
                    mycon = ms.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
                    mycur = mycon.cursor()
                    SQ = '''INSERT into custrecord(BILLNO, CUSTOMER,DOHR,PHONENO,Item,Hours,TOTALPRICE)
        values(%s,%s,%s,%s,%s,%s,%s)'''
                    tres = (billno,customername,date,phoneno,itemname,hours,totalprice)
                    mycur.execute(SQ,tres)
                    mycon.commit()
                    st='''Update Items set avail=%s where Item = %s'''
                    trd=('NO',itemname)
                    mycur.execute(st,trd)
                    mycon.commit()
                    mycon.close()
                    messagebox.showinfo("BOOKING STATUS","BOOKED SUCCESSFULLY")
                    BW.destroy()
                    sm.destroy()
    #-------------------------------------BILLING WINDOW LAYOUT START HERE--------------------------------------------------#
                BW = Toplevel()
                BW.title("BOOKING")
                BW.geometry("540x560") 
                BW.configure(background="Purple")
                LF=LabelFrame(BW, text="BILL", font="25", fg="white", bd=20, bg="Purple")
                lab1=Label(LF, text="BILL NO" ,font="25", bg="purple", fg="white")
                lab1.grid(row=1,column=1,padx=20,pady=20)
                lab2=Label(LF, text="CUSTOMER NAME",font="25", bg="purple", fg="white")
                lab2.grid(row=2,column=1,padx=20,pady=20)
                lab3=Label(LF, text="PHONE NO"  ,font="25", bg="purple", fg="white")
                lab3.grid(row=3,column=1,padx=20,pady=20)
                lab4=Label(LF, text="ITEM NAME" ,font="25", bg="purple", fg="white")
                lab4.grid(row=4,column=1,padx=20,pady=20)
                lab5=Label(LF, text="HOURS" ,font="25", bg="purple", fg="white")
                lab5.grid(row=5,column=1,padx=20,pady=20)
                lab8=Label(LF, text="DATE (yyyy-mm-dd)" ,font="25", bg="purple", fg="white")
                lab8.grid(row=6,column=1,padx=20,pady=20)
                lab7=Label(LF, text="TOTAL PRICE" ,font="25", bg="purple", fg="white")
                lab7.grid(row=7,column=1,padx=20,pady=20)

                E1=Entry(LF, width=30,font="25")
                E1.grid(row=1,column=2,padx=20,pady=20)
                E2=Entry(LF, width=30,font="25", )
                E2.grid(row=2,column=2,padx=20,pady=20)
                E3=Entry(LF, width=30,font="25")
                E3.grid(row=3,column=2,padx=20,pady=20)
                E4=Entry(LF, width=30,font="25")
                E4.grid(row=4,column=2,padx=20,pady=20)
                E4.insert(0,Iname)
                E5=Entry(LF, width=30,font="25")
                E5.grid(row=5,column=2,padx=20,pady=20)
                E5.insert(0,hour)
                E6=Entry(LF, width=30,font="25")
                E6.grid(row=6,column=2,padx=20,pady=20)
                mycon = ms.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
                mycur = mycon.cursor()
                mycur.execute('select curdate()')
                myres = mycur.fetchall()
                E6.insert(0,myres)
                Sq ='''select hours,price from items where Item=%s'''
                tres = (Iname,)
                mycur.execute(Sq,tres)
                mycod= mycur.fetchall()
                pr = mycod[0][1]/mycod[0][0]
                fhour=float(hour)
                tpr=pr*fhour
                E7=Entry(LF, width=30,font="25")
                E7.grid(row=7,column=2,padx=20,pady=20)
                E7.insert(0,tpr)
                LF.grid()
                bQ=Button(LF, text="PROCEED", bg='cyan',font="25", command=ADDREC)
                bQ.grid(row=8,column=1,padx=20,pady=20)
                bx=Button(LF, text="BACK", bg="red",font="25", command=BW.destroy)
                bx.grid(row=8,column=2,padx=20,pady=20)
    #--------------------------CYCLE HIRING WINDOW LAYOUT-------------------------------------#
            sm = Toplevel()     # designing the Cycle BOOKING/HIRING window
            sm.title("CYCLE BOOKING/HIRING")
            sm.geometry("680x600")
            sm.configure(background="Purple")
            frm=Frame(sm, bg="purple")
            frm.grid(row=1,column=1,pady=20,padx=20)
            Label(frm, text="CYCLE", background="Purple", fg="White",font="Gabriola 50").grid()
            frm2=Frame(sm, bg="purple")
            frm2.grid(row=2,column=1,pady=20,padx=20)
            l1=Label(frm2, text="SELECT CYCLE :", background="Purple", fg="White",font="25")
            l1.grid(row=1,column=1,padx=20,pady=20)
            L1=[]
            conn=ms.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
            mycur=conn.cursor()
            Sq ='''select Item from items where TYPE='CYCLE' and avail='YES' ''' # THIS IS WHERE ONLY AVAILABLE ITEMS ARE SELECT INTO THE LIST SHOWN IN LAYOUT 
            mycur.execute(Sq)
            myres = mycur.fetchall()
            if len(myres[0]) == 0:
                L1=['Cycle are not available']
            else:
                for i in range(0,len(myres)):
                    a = myres[i][0]
                    L1.append(a)
                        
            mycur.close()
            conn.close()
            n=StringVar()
            bikedeck1=ttk.Combobox(frm2, width=30, textvariable=n,font="25")
            bikedeck1['values'] = L1
            bikedeck1.grid(row=1,column=2,padx=20,pady=20)
            bikedeck1.current()
            labh=Label(frm2, text="HOURS", bg="Purple", fg="white",font="25")
            labh.grid(row=2,column=1,padx=20,pady=20)
            hourdeck2 =Entry(frm2, width=30,font="25")
            hourdeck2.grid(row=2,column=2,padx=20,pady=20)
            frm3=Frame(sm, bg="purple")
            frm3.grid(row=3,column=1,pady=20,padx=20)
            but1=Button(frm3, text="SUBMIT",font="Gabriola 15 bold", bg='cyan', command=cyclewin)
            but1.grid(row=1,column=1,pady=10,padx=100)
            blab2 = Button(frm3, text='BACK',font="Gabriola 15 bold", bg='cyan', command=sm.destroy)
            blab2.grid(row=1,column=2,pady=10,padx=100)
    #-----------------------------------------CAR HIRING WINDOW STARTS HERE-------------------------------------------#
        def carw():     # CAR HIRING WINDOW
            def carwin():   # CAR BILLING WINDOW 
                Iname=bikedeck1.get()
                hour=hourdeck2.get()
                def ADDREC():
                    billno=int(E1.get())
                    customername=E2.get()
                    phoneno=int(E3.get())
                    itemname=E4.get()
                    hours=int(E5.get())
                    date=E6.get()
                    totalprice=int(E7.get())
                    mycon = ms.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
                    mycur = mycon.cursor()
                    SQ ='''INSERT into custrecord(BILLNO, CUSTOMER,DOHR,PHONENO,Item,Hours,TOTALPRICE)
        values(%s,%s,%s,%s,%s,%s,%s)'''
                    tres = (billno,customername,date,phoneno,itemname,hours,totalprice)
                    mycur.execute(SQ,tres)
                    mycon.commit()
                    st='''Update Items set avail=%s where Item = %s'''
                    trd=('NO',itemname)
                    mycur.execute(st,trd)
                    mycon.commit()
                    mycon.close()
                    messagebox.showinfo("BOOKING STATUS","BOOKED SUCCESSFULLY")
                    BW.destroy()
                    sm.destroy()
    #-------------------------------------BILLING WINDOW LAYOUT FOR CAR--------------------------------------------------#’’’
                BW = Toplevel()
                BW.title("BOOKING")
                BW.geometry("540x560") 
                BW.configure(background="Purple")
                LF=LabelFrame(BW, text="BILL", font="25", fg="white", bd=20, bg="Purple")
                lab1=Label(LF, text="BILL NO" ,font="25", bg="purple", fg="white")
                lab1.grid(row=1,column=1,padx=20,pady=20)
                lab2=Label(LF, text="CUSTOMER NAME",font="25", bg="purple", fg="white")
                lab2.grid(row=2,column=1,padx=20,pady=20)
                lab3=Label(LF, text="PHONE NO"  ,font="25", bg="purple", fg="white")
                lab3.grid(row=3,column=1,padx=20,pady=20)
                lab4=Label(LF, text="ITEM NAME" ,font="25", bg="purple", fg="white")
                lab4.grid(row=4,column=1,padx=20,pady=20)
                lab5=Label(LF, text="HOURS" ,font="25", bg="purple", fg="white")
                lab5.grid(row=5,column=1,padx=20,pady=20)
                lab8=Label(LF, text="DATE (yyyy-mm-dd)" ,font="25", bg="purple", fg="white")
                lab8.grid(row=6,column=1,padx=20,pady=20)
                lab7=Label(LF, text="TOTAL PRICE" ,font="25", bg="purple", fg="white")
                lab7.grid(row=7,column=1,padx=20,pady=20)

                E1=Entry(LF, width=30,font="25")
                E1.grid(row=1,column=2,padx=20,pady=20)
                E2=Entry(LF, width=30,font="25", )
                E2.grid(row=2,column=2,padx=20,pady=20)
                E3=Entry(LF, width=30,font="25")
                E3.grid(row=3,column=2,padx=20,pady=20)
                E4=Entry(LF, width=30,font="25")
                E4.grid(row=4,column=2,padx=20,pady=20)
                E4.insert(0,Iname)
                E5=Entry(LF, width=30,font="25")
                E5.grid(row=5,column=2,padx=20,pady=20)
                E5.insert(0,hour)
                E6=Entry(LF, width=30,font="25")
                E6.grid(row=6,column=2,padx=20,pady=20)
                mycon = ms.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
                mycur = mycon.cursor()
                mycur.execute('select curdate()')
                myres = mycur.fetchall()
                E6.insert(0,myres)
                Sq ='''select hours,price from items where Item=%s'''
                tres = (Iname,)
                mycur.execute(Sq,tres)
                mycod= mycur.fetchall()
                pr = mycod[0][1]/mycod[0][0]
                fhour=float(hour)
                tpr=pr*fhour
                E7=Entry(LF, width=30,font="25")
                E7.grid(row=7,column=2,padx=20,pady=20)
                E7.insert(0,tpr)
                LF.grid()
                bQ=Button(LF, text="PROCEED", bg='cyan',font="25", command=ADDREC)
                bQ.grid(row=8,column=1,padx=20,pady=20)
                bx=Button(LF, text="BACK", bg="red",font="25", command=BW.destroy)
                bx.grid(row=8,column=2,padx=20,pady=20)
    #------------------------------------- CAR HIRING WINDOW LAYOUT---------------------------------------------#
            sm = Toplevel()     # designing the CARS BOOKING/HIRING window
            sm.title("CAR BOOK/HIRING")
            sm.geometry("680x600")
            sm.configure(background="Purple")
            frm=Frame(sm, bg="purple")
            frm.grid(row=1,column=1,pady=20,padx=20)
            Label(frm, text="CAR", background="Purple", fg="White",font="Gabriola 50").grid()
            frm2=Frame(sm, bg="purple")
            frm2.grid(row=2,column=1,pady=20,padx=20)
            Label(frm2, text="SELECT CAR :", background="Purple", fg="White",font="25").grid(row=1,column=1,padx=20,pady=20)
            L1=[]
            conn=ms.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
            mycur=conn.cursor()
            Sq ='''select Item from items where TYPE='CAR' and avail='YES' ''' # THIS IS WHERE ONLY AVAILABLE ITEMS ARE SELECT INTO THE LIST SHOWN IN LAYOUT 
            mycur.execute(Sq)
            myres = mycur.fetchall()
            if len(myres[0]) == 0:
                L1=['Bikes are not available']
            else:
                for i in range(0,len(myres)):
                    a = myres[i][0]
                    L1.append(a)
                        
            mycur.close()
            conn.close()
            n=StringVar()
            bikedeck1=ttk.Combobox(frm2, width=30, textvariable=n,font="25")
            bikedeck1['values'] = L1
            bikedeck1.grid(row=1,column=2,padx=20,pady=20)
            bikedeck1.current()
            labh=Label(frm2, text="HOURS", bg="Purple", fg="white",font="25")
            labh.grid(row=2,column=1,padx=20,pady=20)
            hourdeck2 =Entry(frm2, width=30,font="25")
            hourdeck2.grid(row=2,column=2,padx=20,pady=20)
            frm3=Frame(sm, bg="purple")
            frm3.grid(row=3,column=1,pady=20,padx=20)
            but1=Button(frm3, text="SUBMIT",font="Gabriola 15 bold", bg='cyan', command=carwin)
            but1.grid(row=1,column=1,pady=10,padx=100)
            blab2 = Button(frm3, text='BACK',font="Gabriola 15 bold", bg='cyan', command=sm.destroy)
            blab2.grid(row=1,column=2,pady=10,padx=100)
    #----------------------------MAIN WINDOW LAYOUT FOR HIRING BIKE, CYCLE AND CAR-----------------------------------------#’’’
    # Main window for the hire vehicle window                
        hvhlw = Toplevel()
        hvhlw.title('HIRING WINDOW')
        hvhlw.configure(bg = 'purple')
        hvhlw.geometry('400x600')
        F3=Frame(hvhlw, bd=50, bg="Purple")     
        F3.grid()
        lab5=Label(F3, text='BOOK/HIRE', font="Gabriola 50 bold", bg="Purple", fg="Ghost White")
        lab5.grid(row=1,column=1,padx=10,pady=10)
        B4=Button(F3, text="    BIKE     ", font='arial 20', bg="cyan",command=bikew)
        B4.grid(row=2,column=1,padx=10,pady=10)
        B5=Button(F3, text="     CYCLE   ", font='arial 20', bg="cyan",command = cyclew)
        B5.grid(row=3,column=1,padx=10,pady=10)
        B6=Button(F3, text="     CAR     ", font='arial 20', bg="cyan",command=carw)
        B6.grid(row=4,column=1,padx=10,pady=10)
        B7=Button(F3, text="    BACK    ", font='arial 20', bg="cyan",command=hvhlw.destroy)
        B7.grid(row=5,column=1,padx=10,pady=10)
    #----------------------ADD RECORD OF THE VEHICLES INTO TABLES------------------------------------------------------#’’’
    def addvehicle(): # ADD VEHICLES WINDOW LAYOUT
        def addveh(): # ADD VEHICLE INTO TABLE
            mnumber=int(ie1.get())
            Iname=ie2.get()
            Tname=ie3.get()
            astatus=ie4.get()
            hours=ie5.get()
            price=ie6.get()
            mycon=ms.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DATABASE)
            cur = mycon.cursor()
            Sq='''insert into items(modelno,Item,TYPE, avail,Hours,price)
    values(%s,%s,%s,%s,%s,%s)'''
            tres=(mnumber,Iname,Tname,astatus,hours,price)
            cur.execute(Sq,tres)
            mycon.commit()
            cur.close()
            mycon.close()
            messagebox.showinfo('ADDING VEHICLE STATUS','VEHICLE ADDED SUCCESSFULLY')
            addwin.destroy()            
    #------------------------------------LAYOUT--------------------------------------------------#’’’
        addwin=Toplevel()
        addwin.title('ADD VEHICLE')
        addwin.geometry('800x750')
        addwin.configure(bg='purple')
        f4=Frame(addwin, bd=20, bg='purple')
        f4.grid(row=1,column=1,pady=10,padx=10)
        f5 = Frame(addwin, bd=20, bg='purple')
        f5.grid(row=2,column=1,pady=10,padx=10)
        f6=Frame(addwin,bd=20,bg='purple')
        f6.grid(row=3,column=1,padx=10,pady=10)
        lab6=Label(f4, text='ADD RECORD', font="Gabriola 50 bold", bg="Purple", fg="Ghost White")
        lab6.grid(row=1,column=1,padx=10,pady=10)

        l1=Label(f5, text='Model No', font='arial 20 bold', bg="Purple", fg="Ghost White")
        l1.grid(row=1,column=1,padx=50,pady=10)
        ie1=Entry(f5, width=30, font='arial 18 ')
        ie1.grid(row=1,column=2,padx=50,pady=10)
        l2=Label(f5, text='ITEM', font='arial 20 bold', bg="Purple", fg="Ghost White")
        l2.grid(row=2,column=1,padx=50,pady=10)
        ie2=Entry(f5, width=30, font='arial 18')
        ie2.grid(row=2,column=2,padx=50,pady=10)
        l3=Label(f5, text='TYPE', font='arial 20 bold', bg="Purple", fg="Ghost White")
        l3.grid(row=3,column=1,padx=50,pady=10)
        ie3=Entry(f5, width=30, font='arial 18')
        ie3.grid(row=3,column=2,padx=50,pady=10)
        l4=Label(f5, text='AVAILABLE', font='arial 20 bold', bg="Purple", fg="Ghost White")
        l4.grid(row=4,column=1,padx=50,pady=10)
        ie4=Entry(f5, width=30, font='arial 18')
        ie4.grid(row=4,column=2,padx=50,pady=10)
        l5=Label(f5, text='HOURS', font='arial 20 bold', bg="Purple", fg="Ghost White")
        l5.grid(row=5,column=1,padx=50,pady=10)
        ie5=Entry(f5, width=30, font='arial 18')
        ie5.grid(row=5,column=2,padx=50,pady=10)
        l6=Label(f5, text='PRICE', font='arial 20 bold', bg="Purple", fg="Ghost White")
        l6.grid(row=6,column=1,padx=50,pady=10)
        ie6=Entry(f5, width=30, font='arial 18')
        ie6.grid(row=6,column=2,padx=50,pady=10)

        b1=Button(f5, text='ADD VEHICLE',font='arial 18', bg='cyan', command=addveh)
        b1.grid(row=9,column=1,padx=50,pady=10)
        b2=Button(f5,text='BACK',font='arial 18', bg='cyan',command=addwin.destroy)
        b2.grid(row=9,column=2,padx=50,pady=10)
    #----------------------------REMOVING VEHICLES FROM TABLE-----------------------------------------------#’’’
    def rmvehicle():    # REMOVING TABLES WINDOW LAYOUT
        def delteit():  # REMOVING FUNCTION FROM TABLE
            a=str(E1.get())
            mycon=ms.connect(host="localhost",user="root",passwd='',database='rapidrental')
            cur=mycon.cursor()
            sq='select * from items where modelno='+a
            cur.execute(sq)
            mytmp = cur.fetchall()
            if len(mytmp) == 0:
                messagebox.showinfo('RECORD STATUS','RECORD NOT EXISTS')
                E1.delete(0,END)
            else:
                yn = messagebox.askyesno("CONFORMATION","ARE YOU SURE TO DELETE THIS....")
                if yn == True:
                    mycon=ms.connect(host="localhost",user="root",passwd='',database='rapidrental')
                    cur=mycon.cursor()
                    SQ="Delete From items where modelno="+a
                    cur.execute(SQ)
                    mycon.commit()
                    mycon.close()
                    E1.delete(0,END)
                    messagebox.showinfo('RECORD STATUS','RECORD IS DELETED')
                else:
                    messagebox.showinfo('RECORD STATUS','RECORD IS NOT DELETED')
    #----------------------------------------------------REMOVING FUNCTION LAYOUT----------------------------------------#’’’        
        rmvwin = Toplevel()
        rmvwin.title('REMOVE RECORD WINDOW')
        rmvwin.configure(bg='purple')
        frm =LabelFrame(rmvwin, text="REMOVE VEHICLE RECORD",font='gabriola 25 bold',bg="Purple", fg="white", bd=15)
        lab1=Label(frm,text='MODELNO',font='gabriola 25 bold',bg="Purple", fg="white")
        lab1.grid(row=1,column=1, padx=10,pady=10)
        E1 = Entry(frm , bd = 10,font='arial 20 ', bg='purple', fg='white')
        E1.grid(row=1,column=2, padx=10,pady=10)
        b1 = Button(frm, text=' REMOVE RECORD',font='gabriola 15 bold', bg="purple", fg="white", command=delteit)
        b1.grid(row=1,column=3, padx=10,pady=10)
        b2=Button(frm, text='BACK',font='gabriola 15 bold',bg="purple",fg="white", command=rmvwin.destroy)
        b2.grid(row=2,column=3,padx=10,pady=10)
        frm.grid()
    #-------------------------------------------UPDATING WINDOW-------------------------------------#’’’
    def updvehicle():# UPDATING WINDOW LAYOUT
        def updateit(): # UPDTING FUNCTION 
            mycon=ms.connect(user="root",host="localhost",passwd='',database="Rapidrental")
            mycur=mycon.cursor()
            availabitity=str(En4.get()) 
            hour=str(En5.get())
            prices=str(En6.get())
            Sq='''Update items set modelno = %s, Item = %s, TYPE = %s, avail = %s, Hours=%s, price=%s where modelno = %s'''
            trec=(lab1a['text'],En2['text'],En3['text'],availabitity,hour,prices,lab1a['text'])
            mycur.execute(Sq,trec)
            mycon.commit()
            messagebox.showinfo('RECORD STATUS','Record Updated')
            udatwin.destroy()
        def ShowRec(): # SHOWING RECORD FOR UPDATING
            mycon=ms.connect(user="root",host="localhost",passwd='',database="Rapidrental")
            mycur=mycon.cursor()
            tadm=str(En1.get())
            SQ="select * from items where modelno="+tadm
            mycur.execute(SQ) 
            myres=mycur.fetchall()
            if len(myres)==0:
                messagebox.showinfo("RECORD STATUS","Record not exist")
            else:
                lab1a['text']=myres[0][0]
                En2['text']=myres[0][1]
                En3['text']=myres[0][2]
                En4.insert(0,myres[0][3])
                En5.insert(0,myres[0][4])
                En6.insert(0,myres[0][5]) 
                bu['state']='normal'           
            mycon.close()
            mycur.close()
    #---------------------------------------------LAYOUT-------------------------------------------------------------#
        udatwin = Toplevel()
        udatwin.geometry('727x721')
        udatwin.title('UPDATE RECORD WINDOW')
        udatwin.configure(bg='Purple')
        frmlab = LabelFrame(udatwin, text='UPDATE RECORD',font='gabriola 20 bold', fg = 'white',bg='purple',bd='20')
        lab=Label(frmlab, text="MODELNO", font='gabriola 20 bold',bg="Purple", fg="white")
        lab.grid(row=1,column=1,padx=10,pady=10)
        En1=Entry(frmlab,font='arial 20 ',bg="Purple", fg="white")
        En1.grid(row=1,column=2,padx=10,pady=10)
        Bu1=Button(frmlab, text="SEARCH",font='gabriola 20 bold',bg='cyan', command=ShowRec)
        Bu1.grid(row=1,column=3,padx=10,pady=10)
        lab1=Label(frmlab,text="MODELNO",font='gabriola 20 bold',bg="Purple", fg="white")
        lab1.grid(row=2,column=1,padx=10,pady=10)
        lab1a=Label(frmlab,text="",font='arial 20 ',bg="Purple", fg="white")
        lab1a.grid(row=2,column=2,padx=10,pady=10)
        lab2=Label(frmlab,text='ITEM NAME',font='gabriola 20 bold',bg="Purple", fg="white")
        lab2.grid(row=3,column=1,padx=10,pady=10)
        En2=Label(frmlab, text='',font='arial 20 ',bg="Purple", fg="white")
        En2.grid(row=3,column=2,padx=10,pady=10)
        lab3=Label(frmlab, text="TYPE",font='gabriola 20 bold',bg="Purple", fg="white")
        lab3.grid(row=4,column=1,padx=10,pady=10)
        En3=Label(frmlab,text='',font='arial 20 ',bg="Purple", fg="white")
        En3.grid(row=4,column=2,padx=10,pady=10)
        lab4=Label(frmlab, text="AVAILABILITY STATUS",font='gabriola 20 bold',bg="Purple", fg="white")
        lab4.grid(row=5,column=1,padx=10,pady=10)
        En4=Entry(frmlab, font='arial 20 ',bg="Purple", fg="white")
        En4.grid(row=5,column=2,padx=10,pady=10)
        lab5=Label(frmlab, text="HOURS",font='gabriola 20 bold',bg="Purple", fg="white")
        lab5.grid(row=6,column=1,padx=10,pady=10)
        En5=Entry(frmlab, font='arial 20 ',bg="Purple", fg="white")
        En5.grid(row=6,column=2,padx=10,pady=10)
        lab6=Label(frmlab, text="TOTAL PRICE",font='gabriola 20 bold',bg="Purple", fg="white")
        lab6.grid(row=7,column=1,padx=10,pady=10)
        En6=Entry(frmlab,font='arial 20 ',bg="Purple", fg="white")
        En6.grid(row=7,column=2,padx=10,pady=10)
        bu = Button(frmlab, text='UPDATE', font='gabriola 15 bold',state = 'disabled',bg="cyan", command=updateit)
        bu.grid(row=8,column=1,padx=10,pady=10)
        B1=Button(frmlab, text='BACK', font='gabriola 15 bold',bg="cyan", command=udatwin.destroy)
        B1.grid(row=8,column=2,padx=10,pady=10)
        frmlab.grid(row=2, column=1)
    #--------------------------------------------ALL VEHICLE RECORD-----------------------------------------------#’’’
    def allvehicle(): # ALL VEHICLE RECORD WINDOW LAYOUT
        allvwin=Toplevel()
        allvwin.geometry('1500x500')
        allvwin.configure(background='Purple')
        allvwin.title("Show Record Window")
        TitLab=Label(allvwin,text="List Records")
        TitLab.pack()
        frame1=Frame(allvwin,background="white")  #Define frame container
        frame1.pack()
        mycon=ms.connect(user="root",host="localhost",passwd='',database="Rapidrental")
        mycur=mycon.cursor()
        SQ="select * from items "
        mycur.execute(SQ)
        myres=mycur.fetchall()
        if len(myres)==0:
            messagebox.showinfo("Record Status","Record is Empty")
        else:
            lhead=['MODELNO','ITEM NAME','TYPE','AVAILABLE STATUS','HOURS','GIVEN PRICE'] #define heading list
            style=abc.Style() #define style variable calling Style function of ttk
            style.configure("mystyle.Treeview",highlightthickness=0,bd=2,font=('caliibri',10,'bold')) #configure
            style.configure("mystyle.Treeview.Heading",font=('caliibri',10,'bold'))
            style.layout("mystyle.Treeview",[('mystyle.Treeview.treearea',{'sticky':'nwse'})])
            tree=abc.Treeview(allvwin,style="mystyle.Treeview",columns=lhead,show="headings")
            tree.grid(in_=frame1)
            for col in lhead:
                tree.heading(col,text=col.title())
            for item in myres:
                tree.insert("",'end',values=item)
        mycon.close()
        mycur.close()
        backBT=Button(allvwin,text="Back ",fg="black",command=allvwin.destroy)
        backBT.pack()
    #--------------------------------------------AVAILABLE VEHICLE RECORD------------------------------------------#’’’
    def availvehicle():        # AVAILABLE VEHCILE RECORD LAYOUT
        availvwin=Toplevel()
        availvwin.geometry('1500x500')
        availvwin.configure(background='Purple')
        availvwin.title("Show Record Window")
        TitLab=Label(availvwin,text="List Records")
        TitLab.pack()
        frame1=Frame(availvwin,background="white")  #Define frame container
        frame1.pack()
        mycon=ms.connect(user="root",host="localhost",passwd='',database="Rapidrental")
        mycur=mycon.cursor()
        SQ="select * from items where avail = 'YES' "
        mycur.execute(SQ)
        myres=mycur.fetchall()
        if len(myres)==0:
            messagebox.showinfo("Record Status","Record is Empty")
        else:
            lhead=['MODELNO','ITEM NAME','TYPE','AVAILABLE STATUS','HOURS','GIVEN PRICE'] #define heading list
            style=abc.Style() #define style variable calling Style function of ttk
            style.configure("mystyle.Treeview",highlightthickness=0,bd=2,font=('caliibri',10,'bold')) #configure
            style.configure("mystyle.Treeview.Heading",font=('caliibri',10,'bold'))
            style.layout("mystyle.Treeview",[('mystyle.Treeview.treearea',
            {'sticky':'nwse'})])
            tree=abc.Treeview(availvwin,style="mystyle.Treeview",columns=lhead,show="headings")
            tree.grid(in_=frame1)
            for col in lhead:
                tree.heading(col,text=col.title())
            for item in myres:
                tree.insert("",'end',values=item)
        mycon.close()
        mycur.close()
        backBT=Button(availvwin,text="Back ",fg="black",command=availvwin.destroy)
        backBT.pack()
    #---------------------------------------BOOKING RECORD WINDOW-----------------------------------------------#’’’
    def custrd():# BOOKING RECORD WINDOW LAYOUT
        custswin=Toplevel()
        custswin.geometry('1500x500')
        custswin.configure(background='Purple')
        custswin.title("Show Record Window")
        TitLab=Label(custswin,text="List Records")
        TitLab.pack()
        frame1=Frame(custswin,background="white")  #Define frame container
        frame1.pack()
        mycon=ms.connect(user="root",host=
    "localhost",passwd='',database="Rapidrental")
        mycur=mycon.cursor()
        SQ="select * from custrecord"
        mycur.execute(SQ)
        myres=mycur.fetchall()
        if len(myres)==0:
            messagebox.showinfo("Record Status","Record is Empty")
        else:
            lhead=['BILLNO','CUSTOMER NAME','DATE','PHONENO','ITEM','HOURS', 'TOTALPRICE'] #define heading list
            style=abc.Style() #define style variable calling Style function of ttk
            style.configure("mystyle.Treeview",highlightthickness=0,bd=2,font=('caliibri',10,'bold')) #configure
            style.configure("mystyle.Treeview.Heading",font=('caliibri',10,'bold'))
            style.layout("mystyle.Treeview",[('mystyle.Treeview.treearea',
            {'sticky':'nwse'})])
            tree=abc.Treeview(custswin,style="mystyle.Treeview",columns=lhead,show="headings")
            tree.grid(in_=frame1)
            for col in lhead:
                tree.heading(col,text=col.title())
            for item in myres:
                tree.insert("",'end',values=item)
        mycon.close()
        mycur.close()
        backBT=Button(custswin,text="Back ",fg="black",command=custswin.destroy)
        backBT.pack()
# JUST BACK FUNCTION
    def cmwdest(): # BACK FUNCTION OR DESTORY WINDOW FUNTION 
        cmw.destroy()
        rrc.deiconify()
#------------------------------MAIN WINDOW LAYOUT------------------------------------------------------#’’’
    cmw=Toplevel()           # MAIN WINDOW 
    cmw.title("OPERATING WINDOW")
    cmw.geometry("350x760")
    cmw.configure(bg="Purple")
    F2=Frame(cmw,bd=30, bg="Purple")
    F2.grid(row=2,column=1)
    F3=Frame(cmw,bd=30,bg='purple')
    F3.grid(row=1,column=1)
    lab4=Label(F3, text="RAPID RENTAL", font="gabriola 40 bold ", bg="Purple", fg="Ghost White")
    lab4.grid()
    b3 = Button(F2, text='ADD NEW VEHICLE',font='arial 15 ', bg='cyan',command=addvehicle)
    b3.grid(row=1,column=1,padx=10,pady=10)
    b4 = Button(F2, text='REMOVE VEHICLE',font='arial 15', bg='cyan',command=rmvehicle)
    b4.grid(row=2,column=1,padx=10,pady=10)
    b5 = Button(F2, text='UPDATE VEHICLE',font='arial 15', bg='cyan',command=updvehicle)
    b5.grid(row=3,column=1,padx=10,pady=10)
    b6 = Button(F2, text='   ALL VEHICLE   ',font='arial 15', bg='cyan',command=allvehicle)
    b6.grid(row=4,column=1,padx=10,pady=10)
    b7 = Button(F2, text='AVAILABLE VEHICLE',font='arial 15', bg='cyan',command=availvehicle)
    b7.grid(row=5,column=1,padx=10,pady=10)
    b1 = Button(F2,text='   HIRE VEHICLE   ', font='arial 15' , bg='cyan', command=hvhl)
    b1.grid(row=6,column=1,padx=10,pady=10)
    b2 = Button(F2,text='VEHCILE RECORD', font='arial 15' , bg='cyan', command=custrd)
    b2.grid(row=7,column=1,padx=10,pady=10)
    B4=Button(F2, text = "    BACK    ", font='arial 15', bg="cyan", command=cmwdest)
    B4.grid(row=8,column=1,padx=10,pady=10)
#-----------OPENING WINDOW--------------------#
rrc = Tk()      # making the opening window 
rrc.title("RAPID RENTAL COMPANY")
rrc.geometry("420x560")
rrc.configure(bg="Purple")
F1=Frame(rrc, bd=10, bg="Purple")      
a ='''WELCOME
TO 
RAPID RENTAL'''
lab1 = Label(F1, text=a , bg='Purple', fg='white', font='gabriola 58 bold')
lab1.grid()
B1=Button(F1, text=">>>>>", font="arial 20 bold",bg="cyan" , command=CMWin)
B1.grid()
F1.pack(expand=True, fill=BOTH)

rrc.mainloop()   # closing the window 