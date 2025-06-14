from tkinter import *
import math as m

def click(val):
    ex= entry.get()
    ans=''

    try:

        if val=='C':
            ex= ex[0:len(ex)-1]            #'C' - to delete last digit
            entry.delete(0,END)
            entry.insert(0,ex)
            return

        elif val=='CE':
            entry.delete(0,END)

        elif val=='√':
            ans=m.sqrt(eval(ex))            #'eval'- evaluate val into int or float if in string
    
        elif val=='π':
            ans=m.pi

        elif val=='2π':
            ans=2*m.pi

        elif val=='cosθ':
            ans=m.cos(m.radians(eval(ex)))      #eval into int/flo than into radiance

        elif val=='tanθ':
            ans=m.tan(m.radians(eval(ex)))

        elif val=='sinθ':
            ans=m.sin(m.radians(eval(ex)))

        elif val=='cosh':
            ans=m.cosh(m.radians(eval(ex)))      #eval into int/flo than into radiance

        elif val=='tanh':
            ans=m.tanh(m.radians(eval(ex)))
            
        elif val=='sinh':
            ans=m.sinh(m.radians(eval(ex)))

        elif val=='chr(8731)':                     #cube root
            ans=(eval(ex))**(1/3)

        elif val=='x\u02b8':                       #x to the power y
            entry.insert(END,'**')
            return

        elif val=='x\u00B3':                       #cube
            ans=(eval(ex))**3

        elif val=='x\u00B2':                       #square
            ans=eval(ex)**2

        elif val== 'ln':
            ans=m.log2(eval(ex))

        elif val== 'deg':
            ans=m.degrees(eval(ex))

        elif val =='rad':
            ans=m.radians(eval(ex))

        elif val=="e":
            ans=m.e

        elif val=='log10':
            ans=m.log10(eval(ex))

        elif val=='x!':
            ans=m.factorial(eval(ex))

        elif val=='/':                     
            entry.insert(END,"/")
            return

        elif val=='=':
            ans= eval(ex)

        else:
            entry.insert(END,val)
            return
        
        entry.delete(0,END)
        entry.insert(0,ans)
      
    except SyntaxError:
        pass

root = Tk()
root.title("Scientific calculator")
root.config(bg="grey")
root.geometry('680x486+100+100')

entry= Entry(root,font=("arial",20,"bold"),bg='black',fg='white',bd=10,relief= SUNKEN,width=30)
entry.grid(row=0,column=0,columnspan=8)

button_list=["C","CE","√","+","π","cosθ","tanθ","sinθ",
             "1","2","3","-","2π","cosh","tanh","sinh",
             "4","5","6","*","chr(8731)","x\u02b8","x\u00B3","x\u00B2",
             "7","8","9","/","ln","deg","rad","e",
             "0",".","%","=","log10","(",")","x!"]

rowval=1
colval=0

for i in button_list:
    button=Button(root,width=5,height=2,bd=2,text=i,bg='black',fg='white',relief=SUNKEN,command=lambda button=i: click(button),
                  font=('arial',18,'bold'))
    button.grid(row=rowval,column=colval)
    colval+=1
    if colval>7:
        rowval+=1
        colval=0

root.mainloop()
