import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class ResponseBox:
    def __init__(self):
        self.main_window = tk.Tk()

        #Configuration
        self.main_window.geometry('400x500')
        self.main_window.title('Response Form')

        #Now We want to get the Frames, and the Title going
            #create some frames for the top and bottom, these can be left or right, top or bottom, variation
        self.top_frame = tk.Frame(self.main_window)
        self.middle_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        #Adding a Title
        self.big_font = ("Helvetica", 20, "bold")
        self.big_title = tk.Label(self.main_window,text="Responsive Registration \n Form",font= self.big_font)


        #Packing the Title
        self.big_title.pack()

        #Creating the Imput Boxes, Email, Password, Re-Type Password
        self.email_entry = tk.Entry(self.top_frame, width= 20)
        self.email_entry.insert(0,"Email")

        self.password_entry = tk.Entry(self.top_frame, width= 20)
        self.password_entry.insert(0,"Password")

        self.re_type_entry = tk.Entry(self.top_frame, width= 20)
        self.re_type_entry.insert(0,"Re-Type Password")

        self.fname = tk.Entry(self.top_frame,width= 10)
        self.fname.insert(0,"First Name")

        self.lname = tk.Entry(self.top_frame,width= 10)
        self.lname.insert(0,"Last Name")


        #Pack the Entries
        self.email_entry.pack(pady=5)
        self.password_entry.pack(pady=5)    
        self.re_type_entry.pack(pady=5)
        self.fname.pack(side="left", pady=5)
        self.lname.pack(side="right", pady=5)

        #Create an INTVar object that is used with radio button
        self.radio_var = tk.IntVar()

        #Set the INTVar to 1
        self.radio_var.set(0)
        
        #Create the Radio Buttons for male and female
        self.male = tk.Radiobutton(self.middle_frame,
                                       text="Male",
                                       variable=self.radio_var,
                                       value=1)
        self.female = tk.Radiobutton(self.middle_frame,
                                       text="Female",
                                       variable=self.radio_var,
                                       value=2)
        
        #Pack the radio buttons
        self.male.pack(side="left",pady= 10)
        self.female.pack(side="right",pady= 10)

        # Define the list of countries with "Select a Country" as the default
        countries = ["Select a Country", "USA", "Canada", "UK", "Australia", "Germany"]

        # Create a dropdown box
        country_var = tk.StringVar()
        country_dropdown = ttk.Combobox(self.bottom_frame, textvariable=country_var, values=countries)
        country_dropdown.pack(pady=10)

        # Set "Select a Country" as the default value for the dropdown
        country_var.set("Select a Country")

        #Create an INTVar object that is used with Check Boxes
        self.cb_var1 = tk.BooleanVar()
        self.cb_var2 = tk.BooleanVar()

        #Create the Checkboxes
        self.cb1 = tk.Checkbutton(self.bottom_frame,
                                       text="I agree to the Terms and Conditions",
                                       variable=self.cb_var1)
        self.cb2 = tk.Checkbutton(self.bottom_frame,
                                       text="I want to receive emails",
                                       variable=self.cb_var2)

        #pack the Check Boxes
        #Anchor can be used like Side= but to left or right align information. w stands for west
        self.cb1.pack(anchor=tk.W)
        self.cb2.pack(anchor=tk.W)

        #Packing The Frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        #Create a Colored Registration Button to Submit the Information
        self.register_button = tk.Button(self.bottom_frame,text="Register",bg= "Blue", fg="White",height= 3, width=15, command=self.register)
        self.register_button.pack(pady= 20)
    
        tk.mainloop()

    def register(self):
        password = self.password_entry.get()
        retype = self.re_type_entry.get()
        terms = self.cb_var1.get()
        emails = self.cb_var2.get()
        gender = self.radio_var.get()

        if password == retype and gender and terms and emails:
            tk.messagebox.showinfo('Registration','Successcul Registration')
        else:
            if  not (terms and emails):
                tk.messagebox.showinfo('Registration Error', 'You have not slected both checkboxes')

            elif not gender:
                tk.messagebox.showinfo('Registration Error', 'You have not selected a gender')   
                
            elif password != retype:
                tk.messagebox.showinfo('Registration Error','Passwords do not match')
            else:
                tk.messagebox.showinfo('Registration Error', 'You have not filled in all required fields')


response = ResponseBox()