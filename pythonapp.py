import urllib.request as urllib
import tkinter as tk
from tkinter import messagebox

def main():
    url = text_entry.get()
    response = urllib.urlopen(url)
    code = response.getcode()
    if code >= 200 and code  <=299:
        messagebox.showinfo(code , "Successful responses")
    elif code  >= 100 and code  <=199:
        messagebox.showinfo(code , "Informational responses")
    elif code  >= 300 and code  <=399:
        messagebox.showinfo(code , "Redirection messages")
    elif code  >= 400 and code  <=499:
        messagebox.showinfo(code , "Client error responses")
    elif code  >= 500 and code  <=599:
        messagebox.showinfo(code , "Server error responses")
    else:
        messagebox.showinfo(code , "Response unknown")

window = tk.Tk()
window.title("Site connectivity check")
text_label = tk.Label(window, text="Input url of the site: ")
text_label.pack()
text_entry = tk.Entry(window, width=50)
text_entry.pack()
button = tk.Button(window, text="CHECK", command=main)
button.pack()
window.mainloop()