# --------------------------------------------------------------
# -- File:       MiniCalc.py
# -- Class:      CIS-1400 Summer 20XX
# -- Chapter:    Chapter 15
# -- Purpose:    GUI Calculator Program
# --------------------------------------------------------------

import tkinter
from tkinter import messagebox


# Main window class for calculator
class MyGui:

    # Constructor - builds the calculator window
    def __init__(self):
        # Create the window
        self.main_window = tkinter.Tk()

        # Set the title bar for the window
        self.main_window.wm_title('Mini Calculator')

        ##############################
        # Row #1 : the label
        self.frm_label = tkinter.Frame(self.main_window)  # Create the frame
        self.lbl_header = tkinter.Label(self.frm_label, text='Mini Calculator', font=('Arial', 32))  # Create the label
        self.lbl_header.pack(side='top', pady=[20, 0])  # Add the label to the frame
        self.frm_label.pack()  # Add the frame to the window

        ##############################
        # Row #2 : Entry and buttons
        self.frm_input1 = tkinter.Frame(self.main_window)  # Create the frame

        # Add first Entry field
        self.ety_value1 = tkinter.Entry(self.frm_input1, font=('Arial', 22), width=5)
        self.ety_value1.pack(side='left')

        # Add button for addition
        self.btn_add = tkinter.Button(self.frm_input1, text='+', font=('Arial', 22), width=3,
                                      command=self.btn_add_click)
        self.btn_add.pack(side='left', padx=20, pady=10)

        # Add button for multiplication
        self.btn_multiply = tkinter.Button(self.frm_input1, text='X', font=('Arial', 22), width=3,
                                           command=self.btn_multiply_click)
        self.btn_multiply.pack(side='left')

        self.frm_input1.pack()  # Add the frame to the window

        ##############################
        # Row #3 : Entry and buttons
        self.frm_input2 = tkinter.Frame(self.main_window)  # Create the frame

        # Add second Entry field
        self.ety_value2 = tkinter.Entry(self.frm_input2, font=('Arial', 22), width=5)
        self.ety_value2.pack(side='left')

        # Add button for subtraction
        self.btn_subtract = tkinter.Button(self.frm_input2, text='-', font=('Arial', 22), width=3,
                                           command=self.btn_subtract_click)
        self.btn_subtract.pack(side='left', padx=20, pady=10)

        # Add button for divide
        self.btn_divide = tkinter.Button(self.frm_input2, text='/', font=('Arial', 22), width=3,
                                         command=self.btn_divide_click)
        self.btn_divide.pack(side='left')

        self.frm_input2.pack()  # Add the frame to the window

        ##############################
        # Row #4 : Text for results
        self.frm_output = tkinter.Frame(self.main_window)  # Create the frame

        # Add Text for results
        self.txt_result = tkinter.Text(self.frm_output, state='disabled', width=40, height=20, font=('Arial', 12))
        self.txt_result.pack(side='left', padx=20)

        self.frm_output.pack()  # Add the frame to the window

        ##############################
        # Row #5 : Final buttons
        self.frm_bottom = tkinter.Frame(self.main_window)  # Create the frame

        # Add button for clear
        self.btn_clear = tkinter.Button(self.frm_bottom, text='Clear', font=('Arial', 12), command=self.btn_clear_click)
        self.btn_clear.pack(side='left', padx=10, pady=20)

        # Add button for about
        self.btn_about = tkinter.Button(self.frm_bottom, text='About', font=('Arial', 12), command=self.btn_about_click)
        self.btn_about.pack(side='left', padx=10, pady=20)

        self.frm_bottom.pack()  # Add the frame to the window

        # Move cursor to first Entry field
        self.ety_value1.focus()

        # Require to keep the window open
        tkinter.mainloop()

    # Event handler for the addition button
    def btn_add_click(self):

        # Defensive programming - make sure the both entries are valid numbers
        if not self.validate_numbers():
            return

        # Calculate the result
        value1 = float(self.ety_value1.get())
        value2 = float(self.ety_value2.get())
        answer = value1 + value2
        message = str(value1) + ' plus ' + str(value2) + ' equals ' + str(answer) + '\n'

        # tkinter.messagebox.showinfo('Result', message)  # Display the answer as a message box

        # Add the result message to the first line to the result Text box
        self.txt_result.configure(state='normal')
        self.txt_result.insert('0.0', message)
        self.txt_result.configure(state='disabled')

    # Event handler for the subtraction button
    def btn_subtract_click(self):

        # Defensive programming - make sure the both entries are valid numbers
        if not self.validate_numbers():
            return

        # Calculate the result
        value1 = float(self.ety_value1.get())
        value2 = float(self.ety_value2.get())
        answer = value1 - value2
        message = str(value1) + ' minus ' + str(value2) + ' equals ' + str(answer) + '\n'

        # tkinter.messagebox.showinfo('Result', message)  # Display the answer as a message box

        # Add the result message to the first line to the result Text box
        self.txt_result.configure(state='normal')
        self.txt_result.insert('0.0', message)
        self.txt_result.configure(state='disabled')

    # Event handler for the multiplication button
    def btn_multiply_click(self):

        # Defensive programming - make sure the both entries are valid numbers
        if not self.validate_numbers():
            return

        # Calculate the result
        # value1 = float(self.ety_value1.get())
        value1 = float(self.ety_value1.get())
        value2 = float(self.ety_value2.get())
        answer = value1 * value2
        message = str(value1) + ' times ' + str(value2) + ' equals ' + str(answer) + '\n'

        # tkinter.messagebox.showinfo('Result', message)  # Display the answer as a message box

        # Add the result message to the first line to the result Text box
        self.txt_result.configure(state='normal')
        self.txt_result.insert('0.0', message)
        self.txt_result.configure(state='disabled')

    # Event handler for the divide button
    def btn_divide_click(self):

        # Defensive programming - make sure the both entries are valid numbers
        if not self.validate_numbers():
            return

        # Calculate the result
        value1 = float(self.ety_value1.get())
        value2 = float(self.ety_value2.get())

        # Defensive programming - make sure the second number is not zero
        if value2 == 0:
            tkinter.messagebox.showerror('Error', 'Can not divide a number by zero')
            self.ety_value2.focus()
            return

        # Calculate the result
        answer = value1 / value2
        message = str(value1) + ' divided by ' + str(value2) + ' equals ' + str(answer) + '\n'

        # tkinter.messagebox.showinfo('Result', message)  # Display the answer as a message box

        # Add the result message to the first line to the result Text box
        self.txt_result.configure(state='normal')
        self.txt_result.insert('0.0', message)
        self.txt_result.configure(state='disabled')

    # Event handler for the about button
    def btn_about_click(self):
        # Display the message box
        tkinter.messagebox.showinfo('About', 'Mini Calculator\n\n(c)2017 College of DuPage\nAll Rights Reserved')

    # Event handler for the clear button
    def btn_clear_click(self):
        # Clear the three controls
        self.ety_value1.delete(0, 'end')
        self.ety_value2.delete(0, 'end')
        self.txt_result.configure(state='normal')
        self.txt_result.delete('0.0', 'end')
        self.txt_result.configure(state='disabled')
        self.ety_value1.focus()

    # Defensive programming - make sure both Entry fields contain valid numbers
    def validate_numbers(self):

        # Display error if first Entry not a valid number
        if not self.is_float(self.ety_value1.get()):
            tkinter.messagebox.showerror('Error', 'The first value must be a valid number')
            self.ety_value1.focus()
            return False

        # Display error if second Entry not a valid number
        if not self.is_float(self.ety_value2.get()):
            tkinter.messagebox.showerror('Error', 'The second value must be a valid number')
            self.ety_value2.focus()
            return False

        return True  # Both entries are valid numbers

    # Determines if a string represents a floating point number
    @staticmethod
    def is_float(string):
        try:
            float(string)
            return True
        except ValueError:
            return False


# Start the calculator window
myGui = MyGui()
