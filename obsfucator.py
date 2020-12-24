import base64
import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
class root(tkinter.Tk):
    def __init__(self):
        super().__init__()
        tkinter.Label(self,text="Python File Obsfucation System").grid(column=1,row=0)
        Content= tkinter.Frame(self)
        Content.grid(column=1,row=1)
        tkinter.Label(Content,text="Python File To Obsfucate:").grid(column=0,row=0)
        ObsButton = tkinter.Button(Content,text="Select File...",command=self.ObsHandle)
        ObsButton.grid(column=1,row=0)
        tkinter.Label(Content,text="Python File To Deobsfucate:").grid(column=0,row=1)
        DeObsButton = tkinter.Button(Content,text="Select File..",command=self.DeObsHandle)
        DeObsButton.grid(column=1,row=1)
    def encode(self,file):
        message = open(file).read()
        message_bytes = message.encode('utf-8')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = "import base64;exec(base64.b64decode('"+base64_bytes.decode('utf-8')+"'.encode('utf-8')).decode('utf-8'))"
        open(file,"w+").write(base64_message)

    def decode(self,file):
        base64_message = open(file).read()
        li = list(base64_message)
        for x in range(0,37):
            del li[0]
        for x in range(0,35):
            del li[len(li)-1]
        base64_message = ''.join(x for x in li)
        base64_bytes = base64_message.encode('utf-8')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('utf-8')
        open(file,"w+").write(message)
    def ObsHandle(self):
        selectedPath = filedialog.askopenfilename()
        if selectedPath == "":
            messagebox.showerror("Error","Operation Cancelled. Invalid file provided")
        else:
            self.encode(selectedPath)
            messagebox.showinfo("Info","Task Completed")
    def DeObsHandle(self):
        selectedPath = filedialog.askopenfilename()
        if selectedPath == "":
            messagebox.showerror("Error","Operation Cancelled. Invalid file provided")
        else:
            self.decode(selectedPath)
            messagebox.showinfo("Info","Task Completed")
window = root()
window.mainloop()