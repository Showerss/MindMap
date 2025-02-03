#mindmap program by Phillip Banky
#This program is a simple mindmap program that allows the user to create a mindmap

import tkinter as tk


class MindmapCanvas(tk.Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        #set the background color of the canvas
        self.configure(background='white')

        #create a canvas object to display the mindmap
        self.canvas = tk.Canvas(window, width=600, height=600, bg='white')
        self.canvas.pack(side='right')

        #
        self.scan_mark_x = 0
        self.scan_mark_y = 0

        #bind events to the mouse to allow the user to move the canvas around
        self.canvas.bind('<ButtonPress-1>', self.start_pan)
        self.canvas.bind('<B1-Motion>', self.pan)
        self.canvas.bind('<MouseWheel>', self.zoom)


        #initial scale factor of zoom
        self.scale_factor = 1.0

    #create my methods for moving around the canvas
    def start_pan(self, event):
        pass

    def pan(self, event):
        pass

    def zoom(self, event):
        pass

############# Functions #############
def how_to_popup():
    how_to_window = tk.Tk()
    how_to_window.title('How to use Mindmap')
    how_to_window.geometry('800x600')
    how_to_window.mainloop()


def create_map():
    pass


def show_contact_window():
    contact_window = tk.Tk()
    contact_window.title('Contact Us')
    contact_window.geometry('800x600')
    contact_window.mainloop()


############# Main Program Window #############

# Create a window object
window = tk.Tk()

# Set the window title
window.title('Safri Mindmap')

# Set the window size
window.geometry('800x600')

#set window color
window.configure(bg='light blue')

# create an output frame on the right 2/3 of the window
output_frame = tk.Frame(window, width=600, height=600, bg='white')
output_frame.pack(side='right')

#buttons frame on the left 1/3 of the window
buttons_frame = tk.Frame(window, width=200, height=600, bg='light blue')
buttons_frame.pack(side='left')

#display some buttons to generate a blank page, anchor it to the buttons_frame
newButton = tk.Button(buttons_frame, text='New')
newButton.pack(side='top', anchor='nw')

#how-to button located at the bottom right of the window, to the left of the contact button
howToButton = tk.Button(buttons_frame, text='How to use')
# howToButton.pack(side='bottom', anchor='se')
howToButton.config(command=how_to_popup)

#create button
createButton = tk.Button(buttons_frame, text='Create')
# createButton.grid(row=0, column=0, sticky='nw')
createButton.config(command=create_map)


#contact button
contactButton = tk.Button(buttons_frame, text='Contact Us')
contactButton.pack(side='bottom', anchor='sw')
contactButton.config(command=show_contact_window)


mindmap_canvas = MindmapCanvas(output_frame, width=600, height=600, bg='white')
mindmap_canvas.pack(fill='both', expand=True)


#TODO: create a canvas object to display the mindmap
#TODO: create an import button that allows you to bring in a .docx file and convert it to a mindmap
#TODO: have the user create the central idea of the mindmap so that we know what to build off of in the imported file 
#TODO: create a function to read over the .docx file and either count the spacing or the bullet points to determine the hierarchy of the mindmap,


#display the window
window.mainloop()


#Question: how do I create a mindmap?


