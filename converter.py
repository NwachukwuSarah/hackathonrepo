#importing...
import json
import yaml
import tkinter as tk


# function to convert the json file to yaml and store in the given location
def convert():
    filelocation=str(fileloc.get())
    with open(filelocation, 'r') as f:
        jsonfile=f.read()    
    jsonfile=str(jsonfile)
    savelocation=str(saveloc.get())
    python_dict=json.loads(jsonfile)
    save=open(savelocation,"w")
    yaml_string=yaml.dump(python_dict,save)
    confirm = tk.Label(master=frame, text="Your file has been saved go check it out!", fg="blue")
    confirm.pack()


#creating a tkinter gui for the input
window = tk.Tk()
window.configure(bg="white")
frame=tk.Frame()
frame.pack()
title = tk.Label(master=frame, text="JSON TO YAML CONVERTER", fg="blue")
title.pack()
title2 = tk.Label(master=frame, text="Type in the location of the file below", fg="blue")
title2.pack()
fileloc = tk.Entry(master=frame, fg="black", width=50)
fileloc.pack()
title3 = tk.Label(master=frame, text="Type in where you want the converted file saved below", fg="blue")
title3.pack()
saveloc = tk.Entry(master=frame, fg="black", width=50)
saveloc.pack()
button = tk.Button(text="SUBMIT", bg="blue",fg="white", command= convert)
button.pack()
window.mainloop()





