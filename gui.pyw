import tkinter as tk
import scraper

def button_press():
    key = search.get()
    pat = path_.get()
    num = iter_.get()
    scraper.download(key,pat,int(num))
    search.set("")
    path_.set("")
    iter_.set("")


window = tk.Tk()

window.size = (300,200)
window.minsize(300,200)
window.maxsize(300,200)
window.title("Scraper")

search = tk.StringVar()
search_key = tk.Entry(textvariable=search)
search_key.place(relx=0.1,y=20,relwidth=0.8,height=20)
search_key.insert(0,"Write Search Key Here")

path_ = tk.StringVar()
path = tk.Entry(textvariable=path_)
path.place(relx=0.1,y=50,relwidth=0.8,height=20,)
path.insert(0,"Write Path Here")

iter_ = tk.StringVar()
iter = tk.Entry(textvariable=iter_)
iter.place(relx=0.1,y=80,relwidth=0.8,height=20,)
iter.insert(0,"Write Photo Count Here")


button = tk.Button(command=button_press,text="Start Process")
button.place(x=170,y=120,width=100,height=50)


window.mainloop()