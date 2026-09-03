import tkinter  as tk
# Create main window
mainWindow = tk.Tk()
mainWindow.title("Simple Login Form")
mainWindow.geometry("500x400")
mainWindow.resizable(False,False)

#username label
label_user=tk.Label(text="username", font=("Arial",15, "bold"), bg="light green")
label_user.pack()

#username entry
entry_user=tk.Entry()
entry_user.pack(pady="12")

#password label
label_user=tk.Label(text="Password", font=("Arial", 15, "bold"), bg="light green")
label_user.pack(pady="12")

#password entry
entry_user=tk.Entry()
entry_user.pack(pady="12", fill="x")

#submit Button
btn_submit = tk.Button(mainWindow, text="submit", font=("Arial", 12, "bold"), bg="light blue",fg="green",)
btn_submit.pack(fill="y")


mainWindow.mainloop()