#import gui functionality from the tkinter module
from tkinter import *

############# Functions #############
def how_to_popup():
    how_to_window = Tk()
    how_to_window.title('How to use Mindmap')
    how_to_window.geometry('800x600')
    how_to_window.mainloop()


def create_map():
    pass


def show_contact_window():
    contact_window = Tk()
    contact_window.title('Contact Us')
    contact_window.geometry('800x600')
    contact_window.mainloop()



############# Main Program Window #############

# Create a window object
window = Tk()

# Set the window title
window.title('MainWindow')

# Set the window size
window.geometry('800x600')


#display some buttons to generate a blank page on the right hand side of the window
newButton = Button(window, text='New')
newButton.grid(column=1, row=0)

#how-to button
howToButton = Button(window, text='How to use')
howToButton.grid(column=1, row=1)
howToButton.config(command=how_to_popup)

#create button
createButton = Button(window, text='Create')
createButton.grid(column=1, row=2)
createButton.config(command=create_map)


#contact button
contactButton = Button(window, text='Contact Us')
contactButton.grid(column=1, row=3)
contactButton.config(command=show_contact_window)





#display the window
window.mainloop()

