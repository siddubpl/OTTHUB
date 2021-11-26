
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont

import cx_Oracle
window = Tk()
window.title("OTT Database Hub")
window.geometry('1920x1080')

# -------------------------------labels
f=tkFont.Font(family="Courier New Bold",size=30)
f2=tkFont.Font(family="Courier New Bold",size=20)
lbl = Label(window,text="                            OTT-HUB                              ", bg="Black",fg="Dark Orange",font=(f))
lblp = Label(window,text="                Search To See If Your Favorite Movies Are In Any of Our Platforms                              ", bg="Black",fg="Dark Orange",font=(f2))
lblu = Label(window,text="                                        Start Exploring!                                        ", bg="Black",fg="White",font=(f2))
#lbl1 = Label(window,text=" Hello User ",font=("Arial Bold", 20))
lbl.place(x=0,y=0)
#lbl1.place(x=0,y=200)
lblp.place(x=0,y=50)
lblu.place(x=0,y=85)

# ---------------------------------buttons
#global m
#m=200

def clickprime():
    btn = Button(window, text="Movies",  bg="Teal", fg="White", font=("Courier New Bold", 17), command=clickmovies_prime)
    btn.place(x=180,y=230)
    btn = Button(window, text="TV-Shows",  bg="Teal", fg="White", font=("Courier New Bold", 17), command=clicktvshows_prime)
    btn.place(x=330,y=230)
def clicknetflix():
    btn1 = Button(window, text="Movies",  bg="Floral White", fg="Red2", font=("Courier New Bold", 17), command=clickmovies_netflix)
    btn1.place(x=1050,y=230)
    btn2 = Button(window, text="TV-Shows",  bg="Floral White", fg="Red2", font=("Courier New Bold", 17), command=clicktvshows_netflix)
    btn2.place(x=1200,y=230)


    
def clickmovies_prime():
    def clear():
        for i in range(len(label)):
            label[i].place_forget()
    def romance_pm():
        global label
        global lab1
        global lab2
        global lab3
        label=[]
        sql1="""select name,genre,imdb from movies_p where GENRE='ROMANCE'"""
        c.execute(sql1)
        row=c.fetchall()
        print(row)
        m=300
        for i in range(len(row)):
            print(i)
            l=200
            k=1
            for j in range(len(row[i])):
                a=row[i]
                lb=Label(window,text=a[j],font=("Courier New Bold", 15))
                #lb.grid(column=5+j*2,row=20+i*2)
                lb.place(x=440+j*300,y=400+i*50)
                label.append(lb)
                #labele=Label(window,text=" ")
                #labele.grid(column=5+j*2+1,row=20+i*2)
                k=k+1
        f2=tkFont.Font(family="Courier New Bold",size=20)
        lab1=Label(window,text="NAME",fg="Dark Orange",font=(f2))
        lab1.place(x=440,y=350)
        label.append(lab1)
        lab2=Label(window,text="GENRE",fg="Dark Orange",font=(f2))
        lab2.place(x=745,y=350)
        label.append(lab2)
        lab3=Label(window,text="IMDB",fg="Dark Orange",font=(f2))
        lab3.place(x=1030,y=350)
        label.append(lab3)
        lab4=Label(window,text="-----------------------------------------------------------------------------------------------------------------------------------")
        lab4.place(x=440,y=380)
        label.append(lab4)

    def drama_pm():
        global label
        global lab1
        global lab2
        global lab3
        label=[]
        sql1="""select name,genre,imdb from movies_p where GENRE='DRAMA'"""
        c.execute(sql1)
        row=c.fetchall()
        print(row)
        m=300
        for i in range(len(row)):
            print(i)
            l=200
            k=1
            for j in range(len(row[i])):
                a=row[i]
                lb=Label(window,text=a[j],font=("Courier New Bold", 15))
                #lb.grid(column=5+j*2,row=20+i*2)
                lb.place(x=440+j*300,y=400+i*50)
                label.append(lb)
                #labele=Label(window,text=" ")
                #labele.grid(column=5+j*2+1,row=20+i*2)
                k=k+1
        f2=tkFont.Font(family="Courier New Bold",size=20)
        lab1=Label(window,text="NAME",fg="Dark Orange",font=(f2))
        lab1.place(x=440,y=350)
        label.append(lab1)
        lab2=Label(window,text="GENRE",fg="Dark Orange",font=(f2))
        lab2.place(x=745,y=350)
        label.append(lab2)
        lab3=Label(window,text="IMDB",fg="Dark Orange",font=(f2))
        lab3.place(x=1030,y=350)
        label.append(lab3)
        lab4=Label(window,text="-----------------------------------------------------------------------------------------------------------------------------------")
        lab4.place(x=440,y=380)
        label.append(lab4)

    def action_pm():
        global label
        global lab1
        global lab2
        global lab3
        label=[]
        sql1="""select name,genre,imdb from movies_p where GENRE='ACTION'"""
        c.execute(sql1)
        row=c.fetchall()
        print(row)
        m=300
        for i in range(len(row)):
            print(i)
            l=200
            k=1
            for j in range(len(row[i])):
                a=row[i]
                lb=Label(window,text=a[j],font=("Courier New Bold", 15))
                #lb.grid(column=5+j*2,row=20+i*2)
                lb.place(x=440+j*300,y=400+i*50)
                label.append(lb)
                #labele=Label(window,text=" ")
                #labele.grid(column=5+j*2+1,row=20+i*2)
                k=k+1
        f2=tkFont.Font(family="Courier New Bold",size=20)
        lab1=Label(window,text="NAME",fg="Dark Orange",font=(f2))
        lab1.place(x=440,y=350)
        label.append(lab1)
        lab2=Label(window,text="GENRE",fg="Dark Orange",font=(f2))
        lab2.place(x=745,y=350)
        label.append(lab2)
        lab3=Label(window,text="IMDB",fg="Dark Orange",font=(f2))
        lab3.place(x=1030,y=350)
        label.append(lab3)
        lab4=Label(window,text="-----------------------------------------------------------------------------------------------------------------------------------")
        lab4.place(x=440,y=380)
        label.append(lab4)
        

    def thriller_pm():
        global label
        global lab1
        global lab2
        global lab3
        label=[]
        sql1="""select name,genre,imdb from movies_p where GENRE='THRILLER'"""
        c.execute(sql1)
        row=c.fetchall()
        print(row)
        m=300
        for i in range(len(row)):
            print(i)
            l=200
            k=1
            for j in range(len(row[i])):
                a=row[i]
                lb=Label(window,text=a[j],font=("Courier New Bold", 15))
                #lb.grid(column=5+j*2,row=20+i*2)
                lb.place(x=440+j*300,y=400+i*50)
                label.append(lb)
                #labele=Label(window,text=" ")
                #labele.grid(column=5+j*2+1,row=20+i*2)
                k=k+1
        f2=tkFont.Font(family="Courier New Bold",size=20)
        lab1=Label(window,text="NAME",fg="Dark Orange",font=(f2))
        lab1.place(x=440,y=350)
        label.append(lab1)
        lab2=Label(window,text="GENRE",fg="Dark Orange",font=(f2))
        lab2.place(x=745,y=350)
        label.append(lab2)
        lab3=Label(window,text="IMDB",fg="Dark Orange",font=(f2))
        lab3.place(x=1030,y=350)
        label.append(lab3)
        lab4=Label(window,text="-----------------------------------------------------------------------------------------------------------------------------------")
        lab4.place(x=440,y=380)
        label.append(lab4)
        

    def horror_pm():
        global label
        global lab1
        global lab2
        global lab3
        label=[]
        sql1="""select name,genre,imdb from movies_p where GENRE='HORROR'"""
        c.execute(sql1)
        row=c.fetchall()
        print(row)
        m=300
        for i in range(len(row)):
            print(i)
            l=200
            k=1
            for j in range(len(row[i])):
                a=row[i]
                lb=Label(window,text=a[j],font=("Courier New Bold", 15))
                #lb.grid(column=5+j*2,row=20+i*2)
                lb.place(x=440+j*300,y=400+i*50)
                label.append(lb)
                #labele=Label(window,text=" ")
                #labele.grid(column=5+j*2+1,row=20+i*2)
                k=k+1
        f2=tkFont.Font(family="Courier New Bold",size=20)
        lab1=Label(window,text="NAME",fg="Dark Orange",font=(f2))
        lab1.place(x=440,y=350)
        label.append(lab1)
        lab2=Label(window,text="GENRE",fg="Dark Orange",font=(f2))
        lab2.place(x=745,y=350)
        label.append(lab2)
        lab3=Label(window,text="IMDB",fg="Dark Orange",font=(f2))
        lab3.place(x=1030,y=350)
        label.append(lab3)
        lab4=Label(window,text="-----------------------------------------------------------------------------------------------------------------------------------")
        lab4.place(x=440,y=380)
        label.append(lab4)
        
     
    #lbl.configure(text=" You are searching for Movies in Prime")
    #lbl.grid(column=0, row=6)
    conn = cx_Oracle.connect('scott/hari@//localhost:1521/HARI')
    c = conn.cursor()
    #sql_create="""CREATE TABLE movies_p(NAME VARCHAR2(25),ID NUMBER,MID NUMBER,GENRE VARCHAR2(25),IMDB NUMBER(2,1))"""
    #c.execute(sql_create)
    #print('TABLE CREATED')
    #sql_insert="""insert into movies_p values(:1,:2,:3,:4,:5)"""
    #data=[('MASTER',1,1,'DRAMA',7.3),('TRANCE',1,2,'DRAMA',7.3),('RANGASTHALAM',1,3,'ACTION',8.4),('BIGIL',1,4,'ACTION',6.7),('JAANU',1,5,'ROMANCE',6.9),('FIDAA',1,6,'ROMANCE',7.5),('HIT',1,7,'THRILLER',7.7),('U-TURN',1,8,'THRILLER',7.0),('BHOOT',1,9,'HORROR',5.4),('LIGHTS-OUT',1,10,'HORROR',6.3)]
    #c.executemany(sql_insert,data)
    #conn.commit()
    #print('Inserted')
    #sql="""select * from movies_p"""
    #c.execute(sql)
    #row=c.fetchall()
    #print(row)
    b1 = Button(window, text="Romance",  bg="Teal", fg="White", font=("Courier New Bold", 15), command=romance_pm)
    b1.place(x=504,y=700)
    b2 = Button(window, text="Drama",  bg="Teal", fg="White", font=("Courier New Bold", 15), command=drama_pm)
    b2.place(x=609,y=700)
    b3 = Button(window, text="Action",  bg="Teal", fg="White", font=("Courier New Bold", 15), command=action_pm)
    b3.place(x=690,y=700)
    b4 = Button(window, text="Thriller",  bg="Teal", fg="White", font=("Courier New Bold", 15), command=thriller_pm)
    b4.place(x=783,y=700)
    b5 = Button(window, text="Horror",  bg="Teal", fg="White", font=("Courier New Bold", 15), command=horror_pm)
    b5.place(x=900,y=700)
    b5 = Button(window, text="Clear",  bg="Orange4", fg="White", font=("Courier New Bold", 15), command=clear)
    b5.place(x=1000,y=700)
    labele=Label(window,text="")
    labele.grid(column=0,row=7)
    labele1=Label(window,text="")
    labele1.grid(column=0,row=8)
    
    
    


def clicktvshows_prime():
    def clear():
        for i in range(len(label)):
            label[i].place_forget()
    def comedy_pt():
        global label
        global lab1
        global lab2
        global lab3
        label=[]
        sql1="""select name,genre,seasons from tvshows_p where GENRE='COMEDY'"""
        c.execute(sql1)
        row=c.fetchall()
        print(row)
        m=300
        for i in range(len(row)):
            print(i)
            l=200
            k=1
            for j in range(len(row[i])):
                a=row[i]
                lb=Label(window,text=a[j],font=("Courier New Bold", 15))
                #lb.grid(column=5+j*2,row=20+i*2)
                lb.place(x=440+j*300,y=400+i*50)
                label.append(lb)
                #labele=Label(window,text=" ")
                #labele.grid(column=5+j*2+1,row=20+i*2)
                k=k+1
        f2=tkFont.Font(family="Courier New Bold",size=20)
        lab1=Label(window,text="NAME",fg="Dark Orange",font=(f2))
        lab1.place(x=440,y=350)
        label.append(lab1)
        lab2=Label(window,text="GENRE",fg="Dark Orange",font=(f2))
        lab2.place(x=745,y=350)
        label.append(lab2)
        lab3=Label(window,text="SEASONS",fg="Dark Orange",font=(f2))
        lab3.place(x=1030,y=350)
        label.append(lab3)
        lab4=Label(window,text="-----------------------------------------------------------------------------------------------------------------------------------")
        lab4.place(x=440,y=380)
        label.append(lab4)
        
    def drama_pt():
        global label
        global lab1
        global lab2
        global lab3
        label=[]
        sql1="""select name,genre,seasons from tvshows_p where GENRE='DRAMA'"""
        c.execute(sql1)
        row=c.fetchall()
        print(row)
        m=300
        for i in range(len(row)):
            print(i)
            l=200
            k=1
            for j in range(len(row[i])):
                a=row[i]
                lb=Label(window,text=a[j],font=("Courier New Bold", 15))
                #lb.grid(column=5+j*2,row=20+i*2)
                lb.place(x=440+j*300,y=400+i*50)
                label.append(lb)
                #labele=Label(window,text=" ")
                #labele.grid(column=5+j*2+1,row=20+i*2)
                k=k+1
        f2=tkFont.Font(family="Courier New Bold",size=20)
        lab1=Label(window,text="NAME",fg="Dark Orange",font=(f2))
        lab1.place(x=440,y=350)
        label.append(lab1)
        lab2=Label(window,text="GENRE",fg="Dark Orange",font=(f2))
        lab2.place(x=745,y=350)
        label.append(lab2)
        lab3=Label(window,text="SEASONS",fg="Dark Orange",font=(f2))
        lab3.place(x=1030,y=350)
        label.append(lab3)
        lab4=Label(window,text="-----------------------------------------------------------------------------------------------------------------------------------")
        lab4.place(x=440,y=380)
        label.append(lab4)
        
    def action_pt():
        global label
        global lab1
        global lab2
        global lab3
        label=[]
        sql1="""select name,genre,seasons from tvshows_p where GENRE='ACTION'"""
        c.execute(sql1)
        row=c.fetchall()
        print(row)
        m=300
        for i in range(len(row)):
            print(i)
            l=200
            k=1
            for j in range(len(row[i])):
                a=row[i]
                lb=Label(window,text=a[j],font=("Courier New Bold", 15))
                #lb.grid(column=5+j*2,row=20+i*2)
                lb.place(x=440+j*300,y=400+i*50)
                label.append(lb)
                #labele=Label(window,text=" ")
                #labele.grid(column=5+j*2+1,row=20+i*2)
                k=k+1
        f2=tkFont.Font(family="Courier New Bold",size=20)
        lab1=Label(window,text="NAME",fg="Dark Orange",font=(f2))
        lab1.place(x=440,y=350)
        label.append(lab1)
        lab2=Label(window,text="GENRE",fg="Dark Orange",font=(f2))
        lab2.place(x=745,y=350)
        label.append(lab2)
        lab3=Label(window,text="SEASONS",fg="Dark Orange",font=(f2))
        lab3.place(x=1030,y=350)
        label.append(lab3)
        lab4=Label(window,text="-----------------------------------------------------------------------------------------------------------------------------------")
        lab4.place(x=440,y=380)
        label.append(lab4)

    def thriller_pt():
        global label
        global lab1
        global lab2
        global lab3
        label=[]
        sql1="""select name,genre,seasons from tvshows_p where GENRE='THRILLER'"""
        c.execute(sql1)
        row=c.fetchall()
        print(row)
        m=300
        for i in range(len(row)):
            print(i)
            l=200
            k=1
            for j in range(len(row[i])):
                a=row[i]
                lb=Label(window,text=a[j],font=("Courier New Bold", 15))
                #lb.grid(column=5+j*2,row=20+i*2)
                lb.place(x=440+j*300,y=400+i*50)
                label.append(lb)
                #labele=Label(window,text=" ")
                #labele.grid(column=5+j*2+1,row=20+i*2)
                k=k+1
        f2=tkFont.Font(family="Courier New Bold",size=20)
        lab1=Label(window,text="NAME",fg="Dark Orange",font=(f2))
        lab1.place(x=440,y=350)
        label.append(lab1)
        lab2=Label(window,text="GENRE",fg="Dark Orange",font=(f2))
        lab2.place(x=745,y=350)
        label.append(lab2)
        lab3=Label(window,text="SEASONS",fg="Dark Orange",font=(f2))
        lab3.place(x=1030,y=350)
        label.append(lab3)
        lab4=Label(window,text="-----------------------------------------------------------------------------------------------------------------------------------")
        lab4.place(x=440,y=380)
        label.append(lab4)

    def horror_pt():
        global label
        global lab1
        global lab2
        global lab3
        label=[]
        sql1="""select name,genre,seasons from tvshows_p where GENRE='HORROR'"""
        c.execute(sql1)
        row=c.fetchall()
        print(row)
        m=300
        for i in range(len(row)):
            print(i)
            l=200
            k=1
            for j in range(len(row[i])):
                a=row[i]
                lb=Label(window,text=a[j],font=("Courier New Bold", 15))
                #lb.grid(column=5+j*2,row=20+i*2)
                lb.place(x=440+j*300,y=400+i*50)
                label.append(lb)
                #labele=Label(window,text=" ")
                #labele.grid(column=5+j*2+1,row=20+i*2)
                k=k+1
        f2=tkFont.Font(family="Courier New Bold",size=20)
        lab1=Label(window,text="NAME",fg="Dark Orange",font=(f2))
        lab1.place(x=440,y=350)
        label.append(lab1)
        lab2=Label(window,text="GENRE",fg="Dark Orange",font=(f2))
        lab2.place(x=745,y=350)
        label.append(lab2)
        lab3=Label(window,text="SEASONS",fg="Dark Orange",font=(f2))
        lab3.place(x=1030,y=350)
        label.append(lab3)
        lab4=Label(window,text="-----------------------------------------------------------------------------------------------------------------------------------")
        lab4.place(x=440,y=380)
        label.append(lab4)
        
    #lbl.configure(text=" You are searching for TV-Shows in Prime")
    #lbl.grid(column=0, row=6)
    conn = cx_Oracle.connect('scott/hari@//localhost:1521/HARI')
    c = conn.cursor()
    #sql_create="""CREATE TABLE tvshows_p(NAME VARCHAR2(25),ID NUMBER,TVID NUMBER,GENRE VARCHAR2(25),SEASONS NUMBER)"""
    #c.execute(sql_create)
    #print('TABLE CREATED')
    #sql_insert="""insert into tvshows_p values(:1,:2,:3,:4,:5)"""
    #data=[('MIRZAPUR',1,1,'DRAMA',2),('BREATHE',1,2,'DRAMA',2),('PANCHAYAT',1,3,'COMEDY',1),('UNDONE',1,4,'COMEDY',1),('PAATAL LOK',1,5,'THRILLER',1),('JACK RYAN',1,6,'THRILLER',2),('THE FAMILY MAN',1,7,'ACTION',1),('THE PURGE',1,8,'ACTION',2),('THE TERROR',1,9,'HORROR',2),('LORE',1,10,'HORROR',2)]
    #c.executemany(sql_insert,data)
    #conn.commit()
    #print('Inserted')
    #sql="""select * from tvshows_p"""
    #c.execute(sql)
    #row=c.fetchall()
    #print(row)
    b1 = Button(window, text="Comedy ",  bg="Teal", fg="White", font=("Courier New Bold", 15), command=comedy_pt)
    b1.place(x=504,y=700)
    b2 = Button(window, text="Drama",  bg="Teal", fg="White", font=("Courier New Bold", 15), command=drama_pt)
    b2.place(x=609,y=700)
    b3 = Button(window, text="Action",  bg="Teal", fg="White", font=("Courier New Bold", 15), command=action_pt)
    b3.place(x=690,y=700)
    b4 = Button(window, text="Thriller",  bg="Teal", fg="White", font=("Courier New Bold", 15), command=thriller_pt)
    b4.place(x=783,y=700)
    b5 = Button(window, text="Horror",  bg="Teal", fg="White", font=("Courier New Bold", 15), command=horror_pt)
    b5.place(x=900,y=700)
    b6 = Button(window, text="Clear",  bg="Orange4", fg="White", font=("Courier New Bold", 15), command=clear)
    b6.place(x=1000,y=700)
    
    
    

#----------------------------------------------------------------------------------------#NETFLIX

def clickmovies_netflix():
    def clear():
        for i in range(len(label)):
            label[i].place_forget()
    def romance_nm():
        global label
        global lab1
        global lab2
        global lab3
        label=[]
        sql1="""select name,genre,imdb from movies_n where GENRE='ROMANCE'"""
        c.execute(sql1)
        row=c.fetchall()
        print(row)
        m=300
        for i in range(len(row)):
            print(i)
            l=200
            k=1
            for j in range(len(row[i])):
                a=row[i]
                lb=Label(window,text=a[j],font=("Courier New Bold", 15))
                #lb.grid(column=5+j*2,row=20+i*2)
                lb.place(x=440+j*300,y=400+i*50)
                label.append(lb)
                #labele=Label(window,text=" ")
                #labele.grid(column=5+j*2+1,row=20+i*2)
                k=k+1
        f2=tkFont.Font(family="Courier New Bold",size=20)
        lab1=Label(window,text="NAME",fg="Dark Orange",font=(f2))
        lab1.place(x=440,y=350)
        label.append(lab1)
        lab2=Label(window,text="GENRE",fg="Dark Orange",font=(f2))
        lab2.place(x=745,y=350)
        label.append(lab2)
        lab3=Label(window,text="IMDB",fg="Dark Orange",font=(f2))
        lab3.place(x=1030,y=350)
        label.append(lab3)
        lab4=Label(window,text="-----------------------------------------------------------------------------------------------------------------------------------")
        lab4.place(x=440,y=380)
        label.append(lab4)

    def drama_nm():
        global label
        global lab1
        global lab2
        global lab3
        label=[]
        sql1="""select name,genre,imdb from movies_n where GENRE='DRAMA'"""
        c.execute(sql1)
        row=c.fetchall()
        print(row)
        m=300
        for i in range(len(row)):
            print(i)
            l=200
            k=1
            for j in range(len(row[i])):
                a=row[i]
                lb=Label(window,text=a[j],font=("Courier New Bold", 15))
                #lb.grid(column=5+j*2,row=20+i*2)
                lb.place(x=440+j*300,y=400+i*50)
                label.append(lb)
                #labele=Label(window,text=" ")
                #labele.grid(column=5+j*2+1,row=20+i*2)
                k=k+1
        f2=tkFont.Font(family="Courier New Bold",size=20)
        lab1=Label(window,text="NAME",fg="Dark Orange",font=(f2))
        lab1.place(x=440,y=350)
        label.append(lab1)
        lab2=Label(window,text="GENRE",fg="Dark Orange",font=(f2))
        lab2.place(x=745,y=350)
        label.append(lab2)
        lab3=Label(window,text="IMDB",fg="Dark Orange",font=(f2))
        lab3.place(x=1030,y=350)
        label.append(lab3)
        lab4=Label(window,text="-----------------------------------------------------------------------------------------------------------------------------------")
        lab4.place(x=440,y=380)
        label.append(lab4)

    def action_nm():
        global label
        global lab1
        global lab2
        global lab3
        label=[]
        sql1="""select name,genre,imdb from movies_n where GENRE='ACTION'"""
        c.execute(sql1)
        row=c.fetchall()
        print(row)
        m=300
        for i in range(len(row)):
            print(i)
            l=200
            k=1
            for j in range(len(row[i])):
                a=row[i]
                lb=Label(window,text=a[j],font=("Courier New Bold", 15))
                #lb.grid(column=5+j*2,row=20+i*2)
                lb.place(x=440+j*300,y=400+i*50)
                label.append(lb)
                #labele=Label(window,text=" ")
                #labele.grid(column=5+j*2+1,row=20+i*2)
                k=k+1
        f2=tkFont.Font(family="Courier New Bold",size=20)
        lab1=Label(window,text="NAME",fg="Dark Orange",font=(f2))
        lab1.place(x=440,y=350)
        label.append(lab1)
        lab2=Label(window,text="GENRE",fg="Dark Orange",font=(f2))
        lab2.place(x=745,y=350)
        label.append(lab2)
        lab3=Label(window,text="IMDB",fg="Dark Orange",font=(f2))
        lab3.place(x=1030,y=350)
        label.append(lab3)
        lab4=Label(window,text="-----------------------------------------------------------------------------------------------------------------------------------")
        lab4.place(x=440,y=380)
        label.append(lab4)
        

    def thriller_nm():
        global label
        global lab1
        global lab2
        global lab3
        label=[]
        sql1="""select name,genre,imdb from movies_n where GENRE='THRILLER'"""
        c.execute(sql1)
        row=c.fetchall()
        print(row)
        m=300
        for i in range(len(row)):
            print(i)
            l=200
            k=1
            for j in range(len(row[i])):
                a=row[i]
                lb=Label(window,text=a[j],font=("Courier New Bold", 15))
                #lb.grid(column=5+j*2,row=20+i*2)
                lb.place(x=440+j*300,y=400+i*50)
                label.append(lb)
                #labele=Label(window,text=" ")
                #labele.grid(column=5+j*2+1,row=20+i*2)
                k=k+1
        f2=tkFont.Font(family="Courier New Bold",size=20)
        lab1=Label(window,text="NAME",fg="Dark Orange",font=(f2))
        lab1.place(x=440,y=350)
        label.append(lab1)
        lab2=Label(window,text="GENRE",fg="Dark Orange",font=(f2))
        lab2.place(x=745,y=350)
        label.append(lab2)
        lab3=Label(window,text="IMDB",fg="Dark Orange",font=(f2))
        lab3.place(x=1030,y=350)
        label.append(lab3)
        lab4=Label(window,text="-----------------------------------------------------------------------------------------------------------------------------------")
        lab4.place(x=440,y=380)
        label.append(lab4)
        

    def horror_nm():
        global label
        global lab1
        global lab2
        global lab3
        label=[]
        sql1="""select name,genre,imdb from movies_n where GENRE='HORROR'"""
        c.execute(sql1)
        row=c.fetchall()
        print(row)
        m=300
        for i in range(len(row)):
            print(i)
            l=200
            k=1
            for j in range(len(row[i])):
                a=row[i]
                lb=Label(window,text=a[j],font=("Courier New Bold", 15))
                #lb.grid(column=5+j*2,row=20+i*2)
                lb.place(x=440+j*300,y=400+i*50)
                label.append(lb)
                #labele=Label(window,text=" ")
                #labele.grid(column=5+j*2+1,row=20+i*2)
                k=k+1
        f2=tkFont.Font(family="Courier New Bold",size=20)
        lab1=Label(window,text="NAME",fg="Dark Orange",font=(f2))
        lab1.place(x=440,y=350)
        label.append(lab1)
        lab2=Label(window,text="GENRE",fg="Dark Orange",font=(f2))
        lab2.place(x=745,y=350)
        label.append(lab2)
        lab3=Label(window,text="IMDB",fg="Dark Orange",font=(f2))
        lab3.place(x=1030,y=350)
        label.append(lab3)
        lab4=Label(window,text="-----------------------------------------------------------------------------------------------------------------------------------")
        lab4.place(x=440,y=380)
        label.append(lab4)
        
    #lbl.configure(text=" You are searching for Movies in Netflix")
    #lbl.grid(column=0, row=6)
    conn = cx_Oracle.connect('scott/hari@//localhost:1521/HARI')
    c = conn.cursor()
    #sql_create="""CREATE TABLE movies_n(NAME VARCHAR2(25),ID NUMBER,MID NUMBER,GENRE VARCHAR2(25),IMDB NUMBER(2,1))"""
    #c.execute(sql_create)
    #print('TABLE CREATED')
    #sql_insert="""insert into movies_n values(:1,:2,:3,:4,:5)"""
    #data=[('BHEESHMA',2,1,'ROMANCE',6.5),('LUDO',2,2,'ACTION',7.6),('PETTA',2,3,'ACTION',7.2),('SARKAR',2,4,'DRAMA',6.8),('MALLESHAM',2,5,'DRAMA',8.5),('GUNA369',2,6,'ROMANCE',6.1),('GAMEOVER',2,7,'THRILLER',7.1),('KHAIDHI',2,8,'THRILLER',8.5),('SINISTER',2,9,'HORROR',6.8),('HUSH',2,10,'HORROR',6.6)]
    #c.executemany(sql_insert,data)
    #conn.commit()
    #print('Inserted')
    #sql="""select * from movies_n"""
    #c.execute(sql)
    #row=c.fetchall()
    #print(row)
    b1 = Button(window, text="Romance",  bg="Floral White", fg="Red2", font=("Courier New Bold", 15), command=romance_nm)
    b1.place(x=504,y=700)
    b2 = Button(window, text="Drama",  bg="Floral White", fg="Red2", font=("Courier New Bold", 15), command=drama_nm)
    b2.place(x=609,y=700)
    b3 = Button(window, text="Action",  bg="Floral White", fg="Red2", font=("Courier New Bold", 15), command=action_nm)
    b3.place(x=690,y=700)
    b4 = Button(window, text="Thriller",  bg="Floral White", fg="Red2", font=("Courier New Bold", 15), command=thriller_nm)
    b4.place(x=783,y=700)
    b5 = Button(window, text="Horror",  bg="Floral White", fg="Red2", font=("Courier New Bold", 15), command=horror_nm)
    b5.place(x=900,y=700)
    b6 = Button(window, text="Clear",  bg="Orange4", fg="White", font=("Courier New Bold", 15), command=clear)
    b6.place(x=1000,y=700)



    

    
def clicktvshows_netflix():
    def clear():
        for i in range(len(label)):
            label[i].place_forget()
        
    def comedy_nt():
        global label
        global lab1
        global lab2
        global lab3
        label=[]
        sql1="""select name,genre,seasons from tvshows_n where GENRE='COMEDY'"""
        c.execute(sql1)
        row=c.fetchall()
        print(row)
        m=300
        for i in range(len(row)):
            print(i)
            l=200
            k=1
            for j in range(len(row[i])):
                a=row[i]
                lb=Label(window,text=a[j],font=("Courier New Bold", 15))
                #lb.grid(column=5+j*2,row=20+i*2)
                lb.place(x=440+j*300,y=400+i*50)
                label.append(lb)
                #labele=Label(window,text=" ")
                #labele.grid(column=5+j*2+1,row=20+i*2)
                k=k+1
        f2=tkFont.Font(family="Courier New Bold",size=20)
        lab1=Label(window,text="NAME",fg="Dark Orange",font=(f2))
        lab1.place(x=440,y=350)
        label.append(lab1)
        lab2=Label(window,text="GENRE",fg="Dark Orange",font=(f2))
        lab2.place(x=745,y=350)
        label.append(lab2)
        lab3=Label(window,text="SEASONS",fg="Dark Orange",font=(f2))
        lab3.place(x=1030,y=350)
        label.append(lab3)
        lab4=Label(window,text="-----------------------------------------------------------------------------------------------------------------------------------")
        lab4.place(x=440,y=380)
        label.append(lab4)

    def drama_nt():
        global label
        global lab1
        global lab2
        global lab3
        label=[]
        sql1="""select name,genre,seasons from tvshows_n where GENRE='DRAMA'"""
        c.execute(sql1)
        row=c.fetchall()
        print(row)
        m=300
        for i in range(len(row)):
            print(i)
            l=200
            k=1
            for j in range(len(row[i])):
                a=row[i]
                lb=Label(window,text=a[j],font=("Courier New Bold", 15))
                #lb.grid(column=5+j*2,row=20+i*2)
                lb.place(x=440+j*300,y=400+i*50)
                label.append(lb)
                #labele=Label(window,text=" ")
                #labele.grid(column=5+j*2+1,row=20+i*2)
                k=k+1
        f2=tkFont.Font(family="Courier New Bold",size=20)
        lab1=Label(window,text="NAME",fg="Dark Orange",font=(f2))
        lab1.place(x=440,y=350)
        label.append(lab1)
        lab2=Label(window,text="GENRE",fg="Dark Orange",font=(f2))
        lab2.place(x=745,y=350)
        label.append(lab2)
        lab3=Label(window,text="SEASONS",fg="Dark Orange",font=(f2))
        lab3.place(x=1030,y=350)
        label.append(lab3)
        lab4=Label(window,text="-----------------------------------------------------------------------------------------------------------------------------------")
        lab4.place(x=440,y=380)
        label.append(lab4)

    def action_nt():
        global label
        global lab1
        global lab2
        global lab3
        label=[]
        sql1="""select name,genre,seasons from tvshows_n where GENRE='ACTION'"""
        c.execute(sql1)
        row=c.fetchall()
        print(row)
        m=300
        for i in range(len(row)):
            print(i)
            l=200
            k=1
            for j in range(len(row[i])):
                a=row[i]
                lb=Label(window,text=a[j],font=("Courier New Bold", 15))
                #lb.grid(column=5+j*2,row=20+i*2)
                lb.place(x=440+j*300,y=400+i*50)
                label.append(lb)
                #labele=Label(window,text=" ")
                #labele.grid(column=5+j*2+1,row=20+i*2)
                k=k+1
        f2=tkFont.Font(family="Courier New Bold",size=20)
        lab1=Label(window,text="NAME",fg="Dark Orange",font=(f2))
        lab1.place(x=440,y=350)
        label.append(lab1)
        lab2=Label(window,text="GENRE",fg="Dark Orange",font=(f2))
        lab2.place(x=745,y=350)
        label.append(lab2)
        lab3=Label(window,text="SEASONS",fg="Dark Orange",font=(f2))
        lab3.place(x=1030,y=350)
        label.append(lab3)
        lab4=Label(window,text="-----------------------------------------------------------------------------------------------------------------------------------")
        lab4.place(x=440,y=380)
        label.append(lab4)
        

    def thriller_nt():
        global label
        global lab1
        global lab2
        global lab3
        label=[]
        sql1="""select name,genre,seasons from tvshows_n where GENRE='THRILLER'"""
        c.execute(sql1)
        row=c.fetchall()
        print(row)
        m=300
        for i in range(len(row)):
            print(i)
            l=200
            k=1
            for j in range(len(row[i])):
                a=row[i]
                lb=Label(window,text=a[j],font=("Courier New Bold", 15))
                #lb.grid(column=5+j*2,row=20+i*2)
                lb.place(x=440+j*300,y=400+i*50)
                label.append(lb)
                #labele=Label(window,text=" ")
                #labele.grid(column=5+j*2+1,row=20+i*2)
                k=k+1
        f2=tkFont.Font(family="Courier New Bold",size=20)
        lab1=Label(window,text="NAME",fg="Dark Orange",font=(f2))
        lab1.place(x=440,y=350)
        label.append(lab1)
        lab2=Label(window,text="GENRE",fg="Dark Orange",font=(f2))
        lab2.place(x=745,y=350)
        label.append(lab2)
        lab3=Label(window,text="SEASONS",fg="Dark Orange",font=(f2))
        lab3.place(x=1030,y=350)
        label.append(lab3)
        lab4=Label(window,text="-----------------------------------------------------------------------------------------------------------------------------------")
        lab4.place(x=440,y=380)
        label.append(lab4)
        

    def horror_nt():
        global label
        global lab1
        global lab2
        global lab3
        label=[]
        sql1="""select name,genre,seasons from tvshows_n where GENRE='HORROR'"""
        c.execute(sql1)
        row=c.fetchall()
        print(row)
        m=300
        for i in range(len(row)):
            print(i)
            l=200
            k=1
            for j in range(len(row[i])):
                a=row[i]
                lb=Label(window,text=a[j],font=("Courier New Bold", 15))
                #lb.grid(column=5+j*2,row=20+i*2)
                lb.place(x=440+j*300,y=400+i*50)
                label.append(lb)
                #labele=Label(window,text=" ")
                #labele.grid(column=5+j*2+1,row=20+i*2)
                k=k+1
        f2=tkFont.Font(family="Courier New Bold",size=20)
        lab1=Label(window,text="NAME",fg="Dark Orange",font=(f2))
        lab1.place(x=440,y=350)
        label.append(lab1)
        lab2=Label(window,text="GENRE",fg="Dark Orange",font=(f2))
        lab2.place(x=745,y=350)
        label.append(lab2)
        lab3=Label(window,text="SEASONS",fg="Dark Orange",font=(f2))
        lab3.place(x=1030,y=350)
        label.append(lab3)
        lab4=Label(window,text="-----------------------------------------------------------------------------------------------------------------------------------")
        lab4.place(x=440,y=380)
        label.append(lab4)
        
    #lbl.configure(text=" You are searching for TV-Shows in Netflix")
    #lbl.grid(column=0, row=6)
    conn = cx_Oracle.connect('scott/hari@//localhost:1521/HARI')
    c = conn.cursor()
    #sql_create="""CREATE TABLE tvshows_n(NAME VARCHAR2(25),ID NUMBER,TVID NUMBER,GENRE VARCHAR2(25),SEASONS NUMBER)"""
    #c.execute(sql_create)
    #print('TABLE CREATED')
    #sql_insert="""insert into tvshows_n values(:1,:2,:3,:4,:5)"""
    #data=[('GOTHAM',2,1,'DRAMA',5),('LUPIN',2,2,'DRAMA',1),('BROOKLYN NINE-NINE',2,3,'COMEDY',6),('F.R.I.E.N.D.S',2,4,'COMEDY',10),('NARCOS',2,5,'THRILLER',3),('BREAKING BAD',2,6,'THRILLER',5),('ARROW',2,7,'ACTION',8),('DAREDEVIL',2,8,'ACTION',3),('SCREAM',2,9,'HORROR',2),('VAN HELSING',2,10,'HORROR',4)]
    #c.executemany(sql_insert,data)
    #conn.commit()
    #print('Inserted')
    #sql="""select * from tvshows_n"""
    #sql="""drop table tvshows_n"""
    #c.execute(sql)
    #row=c.fetchall()
    #print(row)
    b1 = Button(window, text="Comedy ",  bg="Floral White", fg="Red2", font=("Courier New Bold", 15), command=comedy_nt)
    b1.place(x=504,y=700)
    b2 = Button(window, text="Drama",  bg="Floral White", fg="Red2", font=("Courier New Bold", 15), command=drama_nt)
    b2.place(x=609,y=700)
    b3 = Button(window, text="Action",  bg="Floral White", fg="Red2", font=("Courier New Bold", 15), command=action_nt)
    b3.place(x=690,y=700)
    b4 = Button(window, text="Thriller",  bg="Floral White", fg="Red2", font=("Courier New Bold", 15), command=thriller_nt)
    b4.place(x=783,y=700)
    b5 = Button(window, text="Horror",  bg="Floral White", fg="Red2", font=("Courier New Bold", 15), command=horror_nt)
    b5.place(x=900,y=700)
    b6 = Button(window, text="Clear",  bg="Orange4", fg="White", font=("Courier New Bold", 15), command=clear)
    b6.place(x=1000,y=700)

btn = Button(window, text="Amazon Prime",  bg="Teal", fg="white", font=("Courier New Bold", 20), command=clickprime)
btn.place(x=200,y=150)
btn = Button(window, text="Netflix",  bg="Floral White", fg="Red2", font=("Courier New Bold", 20), command=clicknetflix)
btn.place(x=1100,y=150)


# ---------------------------------input

window.mainloop()
