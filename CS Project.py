import tkinter

root = tkinter.Tk()

homePage = tkinter.Frame(root, bg="blue", height=400, width=300)
homePage.grid_propagate(False)
homePage.grid(row=0, column=0, sticky="nsew")


pageOne = tkinter.Frame(root, bg="green")
pageOne.grid(row=0, column=0, sticky="nsew")
pageTwo = tkinter.Frame(root, bg="orange")
pageTwo.grid(row=0, column=0, sticky="nsew")
pageThree= tkinter.Frame(root, bg="red")
pageThree.grid(row=0, column=0, sticky="nsew")
homePage.tkraise()

def showHome():
    homePage.tkraise()

def showPageOne():
    pageOne.tkraise()


def showPageTwo():
    pageTwo.tkraise()


def showPageThree():
    pageThree.tkraise()


#putting the widgets on and arranging the home page
Label1= tkinter.Label(homePage, text=" WELCOME TO WATCH THIS!!", font= "Bold")
Label1.grid(row=0, sticky="e")
goToOne = tkinter.Button(homePage, text="START", font="bold", fg="red", command=showPageOne)
goToOne.grid(row=2, sticky="ew")



#putting the widgets on and arranging pageOne
Label2=tkinter.Label(pageOne, text= "WHAT DO YOU PREFER?",font="bold")
Label2.grid(row=0)
Label3= tkinter.Label(pageOne, text=" CHOOSE TWO:", font= "grey")
Label3.grid(row=1)
Done= tkinter.Button(pageOne, text="DONE", font="bold", command=showPageTwo)
Done.grid(row=3, sticky="nsew")


goHomee= tkinter.Button(pageThree, text="got to Home", fg= "black", command=showHome)
goHomee.grid(row=0, column=0, sticky="nsew")



#putting the widgets on and arranging pageTwo
label1 = tkinter.Label(pageTwo, text="Recommended")
label1.grid(row=0, column=0)

goHome = tkinter.Button(pageTwo, text="RESTART", fg="brown", width=10, command=showHome)
goHome.grid(row=1, column=0)


root.mainloop()
