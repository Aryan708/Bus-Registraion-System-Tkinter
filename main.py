import tkinter as tk

# Create a tkinter window
root = tk.Tk()
root.title("Bus Registration Form")

# Create form labels
label_name = tk.Label(root, text="Name:")
label_age = tk.Label(root, text="Age:")
label_gender = tk.Label(root, text="Gender:")
label_address = tk.Label(root, text="Address:")
label_phone = tk.Label(root, text="Phone:")

# Create form fields
entry_name = tk.Entry(root)
entry_age = tk.Entry(root)
entry_gender = tk.Entry(root)
entry_address = tk.Entry(root)
entry_phone = tk.Entry(root)

# Add form elements to grid
label_name.grid(row=0, column=0)
label_age.grid(row=1, column=0)
label_gender.grid(row=2, column=0)
label_address.grid(row=3, column=0)
label_phone.grid(row=4, column=0)

entry_name.grid(row=0, column=1)
entry_age.grid(row=1, column=1)
entry_gender.grid(row=2, column=1)
entry_address.grid(row=3, column=1)
entry_phone.grid(row=4, column=1)

# Create a submit button
def submit():
    name = entry_name.get()
    age = entry_age.get()
    gender = entry_gender.get()
    address = entry_address.get()
    phone = entry_phone.get()

    # Process the form data here...

    # Clear the form fields after submission
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_gender.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

button_submit = tk.Button(root, text="Submit", command=submit)
button_submit.grid(row=5, column=1)

# Start the tkinter event loop
root.mainloop()
