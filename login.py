import tkinter  as tk
# Create main window
root = tk.Tk()
root.title("Simple Login Form")
root.geometry("300x200")
root.resizable(False,False)


# Username
label_user = tk.Label(root, text="Username:", font=("Arial",12))
label_user.pack(pady=(20,5))

entry_user = tk.Entry(root, font=("Arial", 12))
entry_user.pack()

#Password
label_pass = tk.Label(root, text="Password:",font=("Arial",12))
label_pass.pack(pady=(10, 5))

entry_pass = tk.Entry(root, font=("Arial", 12), width=25, show="*")
entry_pass.pack()

#login Button
btn_login = tk.Button(root, text="Login", font=("Arial", 12), bg="light blue", fg="green")
btn_login.pack()


root.mainloop()

