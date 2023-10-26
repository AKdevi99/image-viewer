from tkinter import *
from PIL import ImageTk,Image


win=Tk()
win.config(background="black")
win.geometry("500x300")
win.title("image viewer")
win.iconbitmap("C:\\Users\\abhij\\AppData\\Roaming\\JetBrains\\PyCharmCE2023.1\\scratches\\images\\icon_1.ico")
#loading images
img_1=ImageTk.PhotoImage(Image.open("images\\cartoon.jpeg"))
img_2=ImageTk.PhotoImage(Image.open("images\\cat.jpeg"))
img_3=ImageTk.PhotoImage(Image.open("images\\duck.jpeg"))
img_4=ImageTk.PhotoImage(Image.open("images\\fox.jpeg"))
img_5=ImageTk.PhotoImage(Image.open("images\\giraf.jpeg"))
#working stuff
current_image=0
img_list=[img_1,img_2,img_3,img_4,img_5]

def update():
    img_holder.config(image=img_list[current_image])
    img_holder.image = img_list[current_image]



def forward():
     global current_image
     if(current_image==4):
         current_image=0
     else:
         current_image+=1
     update()



def previous():
    global current_image
    if(current_image==0):
        current_image=4

    else:
        current_image-=1
    update()

#creating stuffs
img_holder = Label(bg="black", width=490, height=230, image=img_list[current_image], borderwidth=5, relief="ridge")
exit_button=Button(text="exit application",width=30,height=2,bg="black",fg="white", borderwidth=10, highlightbackground="white", highlightcolor="white",command=win.quit)
next_button=Button(text=">>",padx=20,pady=10,bg="black",fg="white", borderwidth=10, highlightbackground="white", highlightcolor="white",command=forward)
previous_button = Button(text="<<", padx=20, pady=10, bg="black", fg="white", borderwidth=10, highlightbackground="white", highlightcolor="white",command=previous)


#sorting stuff

img_holder.grid(row=0,column=0,columnspan=5)
exit_button.grid(row=2,column=1,columnspan=3)
previous_button.grid(row=2,column=0)
next_button.grid(row=2,column=4)

update()

win.mainloop()