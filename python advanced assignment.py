import tkinter

screen = tkinter.Tk()
screen.configure(bg='green')
screen.title('INPUT')

screen.geometry('300x300')

screen = tkinter.Label(screen, text = 'Name').place(x=30, y=50)
email = tkinter.Label(screen, text = 'Email').place(x=30, y=90)
name_entry = tkinter.Entry(screen).place(x=80, y=50)
email_entry = tkinter.Entry(screen).place(x=80, y=90)


screen.mainloop()