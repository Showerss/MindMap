#mindmap program by Phillip Banky
#This program is a simple mindmap program that allows the user to create a mindmap

import tkinter as tk


class MindmapCanvas(tk.Canvas): #mindmap class that inherits from tk.Canvas
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        #set the background color of the canvas
        self.configure(background='white')


        #
        self.scan_mark_x = 0 #since im inside tk.Canvas all i need to do instead is do a self.scan or self.bind
        self.scan_mark_y = 0

        #bind events to the mouse to allow the user to move the canvas around
        self.bind('<ButtonPress-1>', self.start_pan)
        self.bind('<B1-Motion>', self.pan)
        self.bind('<MouseWheel>', self.zoom)


        #initial scale factor of zoom
        self.scale_factor = 1.0

    #create my methods for moving around the canvas
    #track where the mouse is when the user clicks
    def start_pan(self, event):
        self.scan_mark_x = event.x
        self.scan_mark_y = event.y

    #move the canvas around by tracking the mouse movement distance
    def pan(self, event):
        pass

    #zoom in and out of the canvas using mousewheel inputs
    def zoom(self, event):
        pass

############# Functions #############
def how_to_popup():
    how_to_window = tk.Tk()
    how_to_window.title('How to use Mindmap')
    how_to_window.geometry('800x600')
    how_to_window.mainloop()


def create_map():
    #small popup window to ask if you have a file to import or are you starting fresh
    create_window = tk.Tk()
    create_window.title('Create Mindmap')
    create_window.geometry('200x100')

    starting_fresh_label = tk.Label(create_window, text='You can either start a new custom mindmap or a notes file that we will scan and assign nodes according to frequency and overall theme.')
    starting_fresh_label.pack()

    import_button = tk.Button(create_window, text='Import File')
    import_button.pack()

    new_map_button = tk.Button(create_window, text='New Custom Map')
    new_map_button.pack()


def show_contact_window():
    contact_window = tk.Tk()
    contact_window.title('Contact Us')
    contact_window.geometry('800x600')
    contact_window.mainloop()
    #add github link
    #add email

def exit_program():
    #make a popup window to ask if the user is sure they want to exit and stop inputs to any other window
    exit_window = tk.Tk()
    exit_window.title('Exit Program')
    exit_window.geometry('200x100')
    window.destroy()


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
newButton = tk.Button(buttons_frame, bg='light blue', text='New')
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

#exit button
exitButton = tk.Button(buttons_frame, text='Exit')
exitButton.pack(side='bottom', anchor='se')
exitButton.config(command=exit_program)


mindmap_canvas = MindmapCanvas(output_frame, width=600, height=600, bg='white')
mindmap_canvas.pack(fill='both', expand=True)


#TODO: Refine the Canvas Class:

# Implement the panning (start_pan and pan) and zoom (zoom) methods with simple functionality.
# Test the canvas separately with simple shapes to verify panning and zooming works.
# Design the Mindmap Data Model:
#
# Define a class or data structure for nodes and edges (e.g., each node has an ID, label, position, and maybe a weight or frequency).
# Decide how you will store the hierarchy and relationships between nodes.
# Integrate File Import and Data Processing:
#
# Implement the basic UI for the “Create Map” function to prompt the user for file input or a new map.
# Write a parser (or plan to use one) that can analyze a .docx file (if needed) and extract the hierarchy and word frequencies.
# Consider abstracting heavy computations (like frequency counting or layout calculations) into a C function. Write a small prototype in C and integrate it using ctypes or Cython.
# Develop the GUI Layout:
#
# Finalize the layout of your main window with frames for buttons and the mindmap canvas.
# Ensure buttons trigger the intended functions (e.g., “New,” “How to Use,” “Contact Us,” “Exit”).
# Testing and Debugging:
#
# Test each component separately (unit testing if possible).
# Ensure event bindings on the canvas work correctly.
# Check the performance impact when dealing with many nodes; if it becomes sluggish, identify bottlenecks.
# Enhance Interactivity:
#
# Add features like node selection, drag-and-drop to reposition nodes, or context menus for editing node properties.
# Implement smooth zoom and pan, possibly by refining the event handling methods.
# Documentation and Future Improvements:
#
# Document the code and design decisions.
# Outline future features (e.g., saving/loading mindmaps, more complex layout algorithms, integration with external libraries for visualization).
# C Integration (Optional, as needed):
#
# Identify which functions are most memory/CPU intensive.
# Create prototypes in C for those functions.
#     Learn how to build and import C extensions using Cython or ctypes.
# Test the integrated C functions in the Python environment.

#display the window
window.mainloop()


#Question: how do I create a mindmap?


