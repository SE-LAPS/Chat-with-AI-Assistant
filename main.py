from tkinter import *

#Gui
root = Tk()
root.title("Chat-With-LapZ")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

#Send Function
def send():
    send = "You --->" + e.get()
    txt.insert(END, "\n" + send)

    user = e.get().lower()

    if (user == "hi" or user == "hii" or user =="hiii"):
        txt.insert(END, "\n" + "Happiness ---> Yes who is this..." "\n")

    elif(user == "oh hey it is me lapz"):
        txt.insert(END, "\n" + "Happiness ---> ohh where did u get my number?" "\n")

    elif(user == "from your daddy😂")
        txt.insert(END, "\n" + "Happiness ---> C'mon don't be such cunny" "\n")

    elif (user == "i got your number from your friend"):
        txt.insert(END, "\n" + "Happiness ---> My friend?" "\n")

    elif (user == "yes your friend"):
        txt.insert(END, "\n" + "Happiness --->  But how?" "\n")

    elif (user == "we are friends😎"):
        txt.insert(END, "\n" + "Happiness ---> From when?" "\n")

    elif (user == "two weeks ago"):
        txt.insert(END, "\n" + "Happiness ---> Where n how? " "\n")

    elif (user == "we make friends on facebook and i ask your number😂"):
        txt.insert(END, "\n" + "Happiness ---> Are you sure?" "\n")

    elif (user == "yes i'm true"):
        txt.insert(END, "\n" + "Happiness ---> oky" "\n")

    elif (user == "anyway i'm sorry for texting you,without your permission"):
        txt.insert(END, "\n" + "Happiness ---> It's ok dear I don't mind" "\n")

    elif (user == "wow that's so sweet💚"):
        txt.insert(END, "\n" + "Happiness ---> Yes but please don't give my number to anyone okay.." "\n")

    elif (user == "okay don't worry,i'll not give"):
        txt.insert(END, "\n" + "Happiness ---> Good boy😍" "\n")

    else:
        txt.insert(END, "\n" + "Happiness ---> Sorry! I didn't got you..." "\n")

    e.delete(0, END)

label1 = Label(root, bg="#180046" , fg=TEXT_COLOR , text="Chat With CodeShow LapZ" , font=FONT_BOLD, pady=10,width=28,height=3).grid(row=0,columnspan=2)

txt = Text(root, fg="#00ffea" , font=FONT,width=60,bg="#A00075")
txt.grid(row=1,column=0,columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1,relx=100.974)

e = Entry(root, bg="#C5FF00",fg="#000000" , font=FONT ,width=50)
e.grid(row=2, column=0)

send = Button(root, text="Send" , font=FONT_BOLD, bg=BG_GRAY,command=send,width=20).grid(row=2,column=1)


root.mainloop()








