from tkinter import *
import math
import tkinter.messagebox

root= Tk() #create a window function
root.title("Custom scientific calculator")
root.configure(background='#f04861')
root.resizable(height=False,width=False)
root.geometry("454x612+0+0")

calculator=Frame(root) #created a frame
calculator.grid()

class Calc():
    def __init__(self):
        self.arithmetic_Operator=""
        self.result=False
        self.check_sum=False
        self.total=0
        self.current = ""
        self.input_value=True

    def numberEnter(self,num):
        self.result=False
        firstnum=inputbox.get()
        secondnum=str(num)
        if self.input_value:
            self.current=secondnum
            self.input_value=False
        else:
            if secondnum=='.':
                if secondnum in firstnum:
                    return
            self.current=firstnum+secondnum
        self.display(self.current) 

    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.valid_function()
        else:
            self.total=float(inputbox.get())

    def valid_function(self):
        if self.arithmetic_Operator=="add":
            self.total+=self.current
        if self.arithmetic_Operator=="sub":
            self.total-=self.current
        if self.arithmetic_Operator=="multi":
            self.total*=self.current
        if self.arithmetic_Operator=="div":
            self.total/=self.current
        if self.arithmetic_Operator=="mod":
            self.total%=self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)

    def display(self,value):
        inputbox.delete(0,END)
        inputbox.insert(0,value)

    def operation(self,op):
        self.current=float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.arithmetic_Operator=op
        self.result=False

    def clear_entry(self):
        self.result=False
        self.current="0"
        self.display(0)
        self.input_value=True

    def Clear_all_entry(self):
        self.clear_entry()
        self.total="0"

    def mathspm(self):
        self.result=False
        self.current= -(float(inputbox.get()))
        self.display(self.current)

    def sqrt(self):
        self.result=False
        self.current= math.sqrt(float(inputbox.get()))
        self.display(self.current) 

    def pi(self):
        self.result=False
        self.current=math.pi
        self.display(self.current) 
    
    def twopi(self):
        self.result=False
        self.current=2*math.pi
        self.display(self.current) 
    
    def cos(self):
        self.result=False
        self.current=math.cos(math.radians(float(inputbox.get())))
        self.display(self.current) 

    def sin(self):
        self.result=False
        self.current=math.sin(math.radians(float(inputbox.get())))
        self.display(self.current)

    def tan(self):
        self.result=False
        self.current=math.tan(math.radians(float(inputbox.get())))
        self.display(self.current)  

    def cosh(self):
        self.result=False
        self.current=math.cosh(math.radians(float(inputbox.get())))
        self.display(self.current) 

    def sinh(self):
        self.result=False
        self.current=math.cos(math.radians(float(inputbox.get())))
        self.display(self.current) 

    def tanh(self):
        self.result=False
        self.current=math.cos(math.radians(float(inputbox.get())))
        self.display(self.current)  

    def acosh(self):
        self.result=False
        self.current=math.acosh(math.radians(float(inputbox.get())))
        self.display(self.current) 

    def asinh(self):
        self.result=False
        self.current=math.asinh(math.radians(float(inputbox.get())))
        self.display(self.current)   

    def deg(self):
        self.result=False
        self.current=math.degrees(float(inputbox.get()))
        self.display(self.current)   

    def log(self):
        self.result=False
        self.current=math.log(float(inputbox.get()))
        self.display(self.current)

    def exp(self):
        self.result=False
        self.current= math.exp(float(inputbox.get()))
        self.display(self.current) 

    def log10(self):
        self.result=False
        self.current= math.log10(float(inputbox.get()))
        self.display(self.current) 

    def log1p(self):
        self.result=False
        self.current= math.log1p(float(inputbox.get()))
        self.display(self.current) 

    def expm1(self):
        self.result=False
        self.current= math.expm1(float(inputbox.get()))
        self.display(self.current)

    def lgamma(self):
        self.result=False
        self.current= math.lgamma(float(inputbox.get()))
        self.display(self.current)

    def log2(self):
        self.result=False
        self.current=math.log2(float(inputbox.get()))
        self.display(self.current)    

    def e(self):
        self.result=False
        self.current=math.e
        self.display(self.current)
        

added_value= Calc()

inputbox=Entry(calculator,font=("arial",25,"bold"), bg="white",bd=5,width=24,justify=RIGHT)
inputbox.grid(row=0,column=0,columnspan=4,pady=4)
inputbox.insert(0,"0.0")

numbers="789456123"
i=0
button=[]

for a in range(2,5): #rows 2-5
    for b in range(3): #columns 0-3
        button.append(Button(calculator,width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,text=numbers[i]))
        button[i].grid(row=a,column=b,pady=1)
        button[i]["command"]=lambda x = numbers [i]: added_value.numberEnter(x)
        i+=1

clearbutton=Button(calculator,text="C",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=added_value.clear_entry)
clearbutton.grid(row=1,column=0,pady=1)

clearallbutton=Button(calculator,text="CE",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=added_value.Clear_all_entry)
clearallbutton.grid(row=1,column=1,pady=1)

sqrootbutton=Button(calculator,text="√",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=added_value.sqrt)
sqrootbutton.grid(row=1,column=2,pady=1)

addbutton=Button(calculator,text="+",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=lambda: added_value.operation("add"))
addbutton.grid(row=1,column=3,pady=1)

subbutton=Button(calculator,text="-",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=lambda: added_value.operation("sub"))
subbutton.grid(row=2,column=3,pady=1)

divbutton=Button(calculator,text="/",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=lambda: added_value.operation("div"))
divbutton.grid(row=3,column=3,pady=1)

mulbutton=Button(calculator,text="*",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=lambda: added_value.operation("multi"))
mulbutton.grid(row=4,column=3,pady=1)

dotbutton=Button(calculator,text=".",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command= lambda : added_value.numberEnter("."))
dotbutton.grid(row=5,column=0,pady=1)

zerobutton=Button(calculator,text="0",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,command=lambda : added_value.numberEnter(0))
zerobutton.grid(row=5,column=1,pady=1)

pmbutton=Button(calculator,text=chr(177),width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=added_value.mathspm)
pmbutton.grid(row=5,column=2,pady=1)

equalbutton=Button(calculator,text="=",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command= added_value.sum_of_total)
equalbutton.grid(row=5,column=3,pady=1)


#Scientific calculator:

pi=Button(calculator,text="π",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=added_value.pi)
pi.grid(row=1,column=4,pady=1)

cos=Button(calculator,text="cos",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=added_value.cos)
cos.grid(row=1,column=5,pady=1)

sin=Button(calculator,text="sin",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=added_value.sin)
sin.grid(row=1,column=6,pady=1)

tan=Button(calculator,text="tan",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=added_value.tan)
tan.grid(row=1,column=7,pady=1)

twopi=Button(calculator,text="2π",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=added_value.twopi)
twopi.grid(row=2,column=4,pady=1)

cosh=Button(calculator,text="cosh",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=added_value.cosh)
cosh.grid(row=2,column=5,pady=1)

sinh=Button(calculator,text="sinh",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=added_value.sinh)
sinh.grid(row=2,column=6,pady=1)

tanh=Button(calculator,text="tanh",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=added_value.tanh)
tanh.grid(row=2,column=7,pady=1)

log=Button(calculator,text="log",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=added_value.log)
log.grid(row=3,column=4,pady=1)

mod=Button(calculator,text="%",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=lambda: added_value.operation("mod"))
mod.grid(row=3,column=5,pady=1)

exp=Button(calculator,text="Exp",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=added_value.exp)
exp.grid(row=3,column=6,pady=1)

e=Button(calculator,text="e",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=added_value.e)
e.grid(row=3,column=7,pady=1)

log2=Button(calculator,text="log2",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=added_value.log2)
log2.grid(row=4,column=4,pady=1)

deg=Button(calculator,text="deg",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=added_value.deg)
deg.grid(row=4,column=5,pady=1)

acosh=Button(calculator,text="acosh",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=added_value.acosh)
acosh.grid(row=4,column=6,pady=1)

asinh=Button(calculator,text="asinh",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=added_value.asinh)
asinh.grid(row=4,column=7,pady=1)

log10=Button(calculator,text="log10",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=added_value.log10)
log10.grid(row=5,column=4,pady=1)

Cos=Button(calculator,text="log1p",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=added_value.log1p)
Cos.grid(row=5,column=5,pady=1)

expm1=Button(calculator,text="expm1",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=added_value.expm1)
expm1.grid(row=5,column=6,pady=1)

lgamma=Button(calculator,text="lgamma",width=5,height=2,font=("arial",25,"bold"),activebackground="#24eaed",activeforeground="white",bd=4,bg="#f04861",command=added_value.lgamma)
lgamma.grid(row=5,column=7,pady=1)

label_scientific=Label(calculator,text='Scientific Calculator',font=("arial",28,"bold"),justify=CENTER)
label_scientific.grid(row=0,column=4,columnspan=4)


#================MENU and functions=======================

def exitfunc():
    exit=tkinter.messagebox.askyesno("Calculator","Do you want to exit?")
    if exit>0:
        root.destroy()
        return

def scientificcalc():
    root.resizable(height=False,width=False)
    root.geometry("913x612+0+0")

def simplecalc():
    root.resizable(height=False,width=False)
    root.geometry("454x612+0+0")  

menubar=Menu(calculator) #create a menubar

filemenu=Menu(menubar, tearoff=0, activebackground="#69ffeb") #file option in menubar
menubar.add_cascade(label= "File",menu=filemenu) 
filemenu.add_command(label='Standard calculator',command=simplecalc)
filemenu.add_command(label='Scientific calculator',command=scientificcalc)
filemenu.add_separator()
filemenu.add_command(label='Quit', command=exitfunc)

editmenu=Menu(menubar, tearoff=0, activebackground="#69ffeb") #file option in menubar
menubar.add_cascade(label= "Edit",menu=editmenu) 
editmenu.add_command(label='Cut')
editmenu.add_command(label='Copy')
editmenu.add_command(label='Paste')

root.config(menu=menubar)
root.mainloop()
