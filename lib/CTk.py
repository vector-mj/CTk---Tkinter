import tkinter as tk
from pyautogui import position

from pystray import MenuItem as item
import pystray
from PIL import Image, ImageTk

# import ctypes
# try:
#     ctypes.windll.shcore.SetProcessDpiAwareness(1) # if your windows version >= 8.1
# except:
#     ctypes.windll.user32.SetProcessDPIAware() # win 8.0 or less 

class CTk(tk.Tk):
   def __init__(self,title,*args,**kwargs):
      tk.Tk.__init__(self,*args,**kwargs)
      self.overrideredirect(True)
      # self.title("Hello World")
      self.geometry("300x300+800+300")
      self.resizable(True,True)
      self.grid_columnconfigure(0,weight=1)
      self.maximize = False
      self.title = title
      self.protocol('WM_DELETE_WINDOW',self.minwin)
      self.minsize(300, 300)
      self.maxsize(600,600)
      # self.grid_rowconfigure(0,weight=1)

      self.topBar = tk.Frame(self,background="#242424",highlightthickness=0,borderwidth=0,bd=0)
      self.topBar.grid_rowconfigure(0, weight=1)
      self.topBar.grid_columnconfigure(0, weight=1)

      self.topBar_btns = tk.Frame(self.topBar,background="gold",highlightthickness=0,borderwidth=0,bd=0)
      self.topBar_title = tk.Label(self.topBar,text=self.title,background="#242424",fg="white")


      self.topBar_close = tk.Frame(self.topBar_btns,background="white",highlightthickness=0,borderwidth=0,relief="solid")
      self.topBar_maximize = tk.Frame(self.topBar_btns,background="white",highlightthickness=0,borderwidth=0,relief="solid")
      self.topBar_minimize = tk.Frame(self.topBar_btns,background="white",highlightthickness=0,borderwidth=0,relief="solid")

      self.topBar.bind("<Button-1>",self.getPos)
      self.topBar.bind("<B1-Motion>",self.moveApp)

      self.topBar.grid(sticky="wen",column=0,row=0)

      self.topBar_btns.grid(column=4,row=0,sticky="ens")
      self.topBar_title.grid(column=0,row=0,sticky="wns")


      self.topBar_close.grid(column=3,row=0,sticky="sn")
      self.topBar_maximize.grid(column=2,row=0,rowspan=20,sticky="e")
      self.topBar_minimize.grid(column=1,row=0,rowspan=20,sticky="e")





      self.grip=tk.ttk.Sizegrip()
      self.grip.place(relx=1.0, rely=1.0, anchor="se")

      self.grip.bind("<B1-Motion>", self.moveMouseButton)

      self.closeBtn = tk.Button(self.topBar_close,text="❌",background="gold",fg="black",command=self.destroy,relief="solid",bd=-2,width=3).grid()
      self.maxBtn = tk.Button(self.topBar_maximize,text="¯",background="lightgreen",fg="black",command=self.maxwin,relief="solid",bd=-2,width=3).grid()
      self.minBtn = tk.Button(self.topBar_minimize,text="_",background="lightblue",fg="black",command=self.minwin,relief="solid",bd=-2,width=3).grid()

   def title(self):
      pass
   def maxwin(self):
      if not self.maximize:
         self.maxsize(10000,10000)
         self.overrideredirect(False)
         self.attributes('-fullscreen',True)
         self.maximize = not self.maximize
      else:
         self.maximize = not self.maximize
         self.attributes('-fullscreen',False)
         self.overrideredirect(True)
         self.geometry("300x300")

   def minwin(self):
      self.withdraw()
      self.image=Image.open("thor.jpg")
      self.menu=(item('Quit',self.quit_window), item('Show',self.show_window))
      self.icon=pystray.Icon("name",self.image, "title",self.menu)
      self.icon.run()

   def show_window(self,icon, item):
      icon.stop()
      self.after(0,self.deiconify())

   def quit_window(self,icon, item):
      icon.stop()
      self.destroy()

   def moveMouseButton(self,e):
      self.x1 = self.winfo_pointerx()
      self.y1 = self.winfo_pointery()
      self.x0 = self.winfo_rootx()
      self.y0 = self.winfo_rooty()
      try:
         self.geometry(f"{self.x1-self.x0}x{self.y1-self.y0}")
      except:pass

   def getPos(self,e):
      self.xwin = self.winfo_x()
      self.ywin = self.winfo_y()

      self.startx = e.x_root
      self.starty = e.y_root

      self.xwin = self.xwin - self.startx
      self.ywin = self.ywin - self.starty

      self.startx = e.x_root
      self.starty = e.y_root

   def moveApp(self,e):
      self.geometry(f"+{e.x_root+self.xwin}+{e.y_root+self.ywin}")

