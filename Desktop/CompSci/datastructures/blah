from Tkinter import *
import tkMessageBox, random

class BattleShip(Frame):
    def __init__(self,master):
        self.btns=[]
        self.btn_loc={}
        self.btn_row=self.random_row()
        self.btn_col=self.random_col()
        self.createButtonPad()

    def createButtonPad(self):
        i=0
        for j in range(5):
            for k in range(5):
                self.btns.append(appBtn(width=5,height=2,text="O"))
                self.btn_loc[(j,k)]=i
                self.btns[i].grid(row=j,column=k)
                self.btns[i].command(j,k)
                i+=1

    def buttonPress(self,x,y):
        if self.btns[self.btn_loc[(x,y)]]["text"]=="O":
            if (x==self.btn_row and y==self.btn_col):
                tkMessageBox.showinfo("Congratulations!","Congratulations! You sank my battleship!")
                root.destroy()
            else:
                tkMessageBox.showinfo("Sorry!","You missed my battleship!")
                self.btns[self.btn_loc[(x,y)]]["text"]="X"
        else:
            tkMessageBox.showinfo("Sorry!","You guessed that one already!")

    def random_row(self):return random.randint(0,4)
    def random_col(self):return random.randint(0,4)

class appBtn(Button):
    def command(self,x,y):
        self["command"]=lambda:app.buttonPress(x,y)

if __name__=='__main__':
    root=Tk()
    root.title("Find The Battleship")
    app=BattleShip(root)
    root.mainloop()
