from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Image Viewer")
root.geometry("500x500")
root.configure(background = "black")

display_image = Label(root, bg = "white", highlightthickness= 5)
display_image.place(relx = 0.5, rely = 0.5, anchor = CENTER)
img_path = ""

def OpenImage():
    global name
    img_path = filedialog.askopenfilename(title = "Open Image File", filetypes = [("Image Files", "*.jpg;*.gif;*.jpg;;*.png;*text")])
    img = ImageTk.PhotoImage(Image.open(img_path))
    display_image["image"] = img
    display_image.close()
    
open_img = Button(root, text = "Open Image", font = "Calibri", bg = "white", fg = "black", relief = SOLID, padx = 10, pady = 5, command = OpenImage)
open_img.place(relx = 0.5, rely = 0.2, anchor = CENTER)

root.mainloop()