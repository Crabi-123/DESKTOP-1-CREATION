import tkinter  as tk
root = tk.Tk()
root.title("Simple Interest calculator")
root.geometry("400x300")
root.resizable(False,False)
# Lable

label_user = tk.Label(root, text="Principal:", font=("Arial",12))
label_user.pack(pady=(20,5))
# Entry

entry_user = tk.Entry(root, font=("Arial", 12))
entry_user.pack()
# Lable

label_user = tk.Label(root, text="Rate (in decimal):", font=("Arial",12))
label_user.pack(pady=(20,5))
# Entry
entry_user = tk.Entry(root, font=("Arial", 12))
entry_user.pack()
# Lable

label_user = tk.Label(root, text="Time (in years):", font=("Arial",12))
label_user.pack(pady=(20,5))

# Entry
entry_user = tk.Entry(root, font=("Arial", 12))
entry_user.pack()


root.mainloop()
