import math
import tkinter as tk
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

        # Create a text entry field for the display
        self.display = tk.Entry(master, width=40, justify='right', font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Create buttons for each of the calculator functions
        self.create_button('(', 1, 0)
        self.create_button(')', 1, 1)
        self.create_button('C', 1, 2)
        self.create_button('CE', 1, 3)
        self.create_button('7', 2, 0)
        self.create_button('8', 2, 1)
        self.create_button('9', 2, 2)
        self.create_button('/', 2, 3)
        self.create_button('4', 3, 0)
        self.create_button('5', 3, 1)
        self.create_button('6', 3, 2)
        self.create_button('*', 3, 3)
        self.create_button('1', 4, 0)
        self.create_button('2', 4, 1)
        self.create_button('3', 4, 2)
        self.create_button('-', 4, 3)
        self.create_button('0', 5, 0)
        self.create_button('.', 5, 1)
        self.create_button('π', 5, 2)
        self.create_button('+', 5, 3)
        self.create_button('sin', 2, 4)
        self.create_button('cos', 3, 4)
        self.create_button('tan', 4, 4)
        self.create_button('^', 5, 4)
        self.create_button('sqrt', 2, 5)
        self.create_button('log', 3, 5)
        self.create_button('exp', 4, 5)
        self.create_button('=', 5, 5)

    # Create a button with the specified text, row, and column
    # Bind the button to a lambda function that passes the button text as an argument to button_click
    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, width=7, height=2, command=lambda: self.button_click(text))
        button.grid(row=row, column=column, padx=5, pady=5)

    # Handle button clicks based on the text of the clicked button
    def button_click(self, text):
        # If the user clicked the 'C' button, then the content of the display entry is deleted.
        if text == 'C':
            self.display.delete(0, tk.END)
        # If the user clicked the 'CE' button, then the last character in the display entry is deleted.
        elif text == 'CE':
            self.display.delete(len(self.display.get()) - 1, tk.END)
        # If the user clicked the '=' button, then the content of the display entry is evaluated
        # and the result is displayed. If the evaluation fails, then an error message is displayed.
        elif text == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        # If the user clicked the 'π' button, then the value of pi is inserted into the display entry.
        elif text == 'π':
            self.display.insert(tk.END, str(math.pi))
        # If the user clicked the 'sqrt' button, then the string "sqrt(" is inserted into the display entry.
        elif text == 'sqrt':
            self.display.insert(tk.END, "sqrt(")
        # If the user clicked the 'log' button, then the string "log(" is inserted into the display entry.
        elif text == 'log':
            self.display.insert(tk.END, "log(")
        # If the user clicked the 'exp' button, then the string "exp(" is inserted into the display entry.
        elif text == 'exp':
            self.display.insert(tk.END, "exp(")
        # If the user clicked any of the 'sin', 'cos', 'tan' buttons, then the corresponding function
        # name is inserted into the display entry followed by a '('.
        elif text in ['sin', 'cos', 'tan']:
            self.display.insert(tk.END, text + "(")
        # If the user clicked any of the other buttons,
        # then the corresponding character is inserted into the display entry.
        else:
            self.display.insert(tk.END, text)

# Create an instance of the Tk class from the tkinter module and assigns it to the variable "root"
# Then, an instance of the Calculator class is created and passed "root" as an argument to its constructor,
# which initializes the calculator GUI. Finally, the main event loop is started by calling
# the mainloop() method of "root". This method listens for events such as button clicks and
# updates the GUI accordingly, and it keeps running until the user closes the window.
root = tk.Tk()
calc = Calculator(root)
root.mainloop()
