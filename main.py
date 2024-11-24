
import tkinter as tk
from tkinter import *
import qrcode 
from io import BytesIO
from PIL import Image, ImageTk, ImageDraw,ImageFont
from tkinter import messagebox
from tkinter.filedialog import askdirectory,asksaveasfile


root= Tk()
root.geometry('550x650')
root.title('Qrcode Generator')
root.config(bg='#00AFEF')
root.resizable(False,False)

def window():
    def messagebox(message):
        frame1=tk.Frame(root,bg="white",highlightbackground='red',highlightthickness=3)
        frame1.place(x=190,y=200,height=120,width=350)
        tk.Label(frame1,width=400,bg='red',height=2).pack(side='top',fill='x')
        tk.Label(frame1,text=message,bg='white',
                 fg='red',font=('newtimesroman',15,'bold'),justify='center').pack()
        tk.Button(frame1,text='X',bg='red',fg='white',
                font=('newtimesroman',12,'bold'),bd=0,command=lambda:cancle(can=frame1)).place(x=320,y=4)

                  
    def generate():
        if input_l.get() !='' :   
                qr= qrcode.QRCode(version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_H,
                        box_size=10, border=4)
                qr.add_data(input_l.get())
                qr.make(fit=True)
                img=qr.make_image(fill_color='black',back_color='white')
                qr_image=ImageTk.PhotoImage(img)
                pic_p.config(image=qr_image)
                pic_p.image=qr_image
                pic_p.pack()
        else:
            messagebox(message='''⚠ ERROR
INPUT YOUR URL OR TEXT''')
                     
    def cancle(can):
            can.destroy()    
    def reset(des):
            des.destroy()
            pic_p.config(image='')
            pic_p.image=''
            input_l.delete(0,'end')
               
    def message():
            massge=tk.Frame(root,bg='cyan',highlightbackground="blue",highlightthickness=3)
            massge.place(x=150,y=300,width=290,height=150)
            Label(massge,text='',bg='blue').pack(side='top',fill='x')
            Label(massge,text='''congratulation!!!
Your qr_code is now in your
directory ''',justify='center', 
                  font=('bold',15),bg='cyan',fg='black').pack()
            tk.Button(massge,text='OK',bg='gray',fg='black',font=('bold',10),
            command=lambda:reset(des=massge)).place(x=110,y=100,width=50)
    def save():
        qr= qrcode.QRCode(version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10, border=4)
        qr.add_data(input_l.get())
        qr.make(fit=True)
        img=qr.make_image(fill_color='black',back_color='white')
        qr_image=(img)
               
        file =asksaveasfile(mode='w', defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file:
                qr_image.save(file.name)
        message()  
    def clear_f():
            pic_p.config(image='')
            pic_p.image=''
            input_l.delete(0,'end')
              
             
        #for click in save:
        #qr_image.save(f'/{}.png')

                
        
        

    tk.Label(root,text='QR Code Generator', font=('arial',24),
            bg='#00AFEF',fg='white').place(x=150,y=15)

    tk.Label(root,text='Enter your Url/Text', font=('book antiqua',12),
            bg='#00AFEF',fg='black').place(x=190,y=55)
    input_l=tk.Entry(root,bd=0,font=('microsoft himalaya',21))
    input_l.place(x=120,y=80,width=350)
    tk.Button(root,text='Generate',bg='magenta',
            fg='white', font=('century gothic',17),bd=0,command=generate).place(x=340,y=110)

    tk.Button(root,text='Save',bg='purple',
            fg='white', font=('News706 bt',20),bd=0,command=save).place(x=120,y=520)

    tk.Button(root,text='Clear',bg='magenta',
            fg='white', font=('News706 bt ',17),bd=0,
            command=clear_f).place(x=380,y=520)

    image_fm=tk.Frame(root,bg='white',bd=0)
    image_fm.place(x=80,y=160,height=350,width=400)
    
    tk.Label(root,text='This is magnitudo project, pls rate us.\n it help us alot',
             font=('book antiqua',16,'bold'),
            bg='#00AFEF',fg='yellow').place(x=90,y=585)
    pic_p= tk.Label(image_fm,image='')
    pic_p.pack()
        
           
window()
root.mainloop()