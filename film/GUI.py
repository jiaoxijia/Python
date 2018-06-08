from Tkinter import *
def on_click():
    label['text'] = 'no way out'
root= Tk(className='bitunion')
label = Label(root)
label['text'] = 'zhe ge shi wen ben'
label.pack()
text = StringVar()
text.set('change to what?')
entry = Entry(root)
entry['textvariable'] = text
entry.pack()
button = Button(root)
button['text'] = 'change it'
button['command'] = on_click
button = Button(root)
button['text'] = 'zhe ge shi an niu'
button.pack()
root.mainloop()

__author__ = 'fyby'

