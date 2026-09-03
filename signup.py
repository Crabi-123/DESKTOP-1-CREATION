import tkinter  as tk
# Create main window
mainWindow = tk.Tk()
mainWindow.title("Signup Form")
mainWindow.geometry("500x700")
mainWindow.resizable(False,False)
#creating another window inside the window
main_frame=tk.Frame(mainWindow, bg="MediumSpringGreen", padx=10, pady=10) #should be packed inside the mainwindow
main_frame.pack(padx=30,pady=30, fill="both", expand=True)

#username label
label_user=tk.Label(main_frame, text="Username", font=("Arial", 15, "bold"), bg="light green")
label_user.pack(pady="4")

#username entry
entry_user=tk.Entry(main_frame)
entry_user.pack(pady="4", fill="x")

#password label
label_pass=tk.Label(main_frame, text="Password", font=("Arial", 15, "bold"), bg="light green")
label_pass.pack(pady="4")

#password entry
entry_pass=tk.Entry(main_frame)
entry_pass.pack(pady="4", fill="x")

#submit Button
btn_submit = tk.Button(mainWindow, text="Submit", font=("Arial", 12, "bold"), bg="light blue", fg="green")
btn_submit.pack(pady="4")
#creating another window inside the window
main_frame=tk.Frame(mainWindow, bg="LightGreen", padx=10, pady=10) #should be packed inside the mainwindow
main_frame.pack(padx=10,pady=10, fill="both", expand=True)

#username label
label_user=tk.Label(main_frame, text="Email", font=("Arial", 15, "bold"), bg="light green")
label_user.pack(pady="12")
#username entry
entry_user=tk.Entry(main_frame)
entry_user.pack(pady="4", fill="x")

#password label
label_pass=tk.Label(main_frame, text="Password", font=("Arial", 15, "bold"), bg="light green")
label_pass.pack(pady="4")

#password entry
entry_pass=tk.Entry(main_frame)
entry_pass.pack(pady="4", fill="x")

#submit Button
btn_submit = tk.Button(main_frame, text="Submit", font=("Arial", 12, "bold"), bg="light blue", fg="green")
btn_submit.pack(pady="4")

mainWindow.mainloop()