import tkinter as tk
import controller as MVC


class MainGUI():
    """ Create and design the GUI """

    def __init__(self, mvc):
        self.window = tk.Tk()
        self.MVC = mvc
        self.display_menu()

    def display_menu(self):
        """ Display the menu of commands """
        self.add_button = tk.Button(self.window,
                                    text="Topic->Link: Add?",
                                    height=5,
                                    width=30,
                                    command=self.MVC.display_Add_GUI)

        self.del_button = tk.Button(self.window,
                                    text="Link: Remove?",
                                    height=5,
                                    width=30,
                                    command=self.MVC.display_Del_GUI)

        self.open_button = tk.Button(self.window,
                                     text="Link: Open?",
                                     height=5,
                                     width=30,
                                     command=self.MVC.open_Browser_GUI)
        self.add_button.pack()
        self.del_button.pack()
        self.open_button.pack()

    def destroy_main_widgets(self):
        """ Destroy: main page widgets """
        self.add_button.destroy()
        self.del_button.destroy()
        self.open_button.destroy()

    def add_link_GUI(self):
        """ Function called when add button is clicked """
        # -- LABEL for TOPIC/LINK Entry -- #
        self.topic_lbl = tk.Label(self.window,
                                  text="Topic: ",
                                  height=2,
                                  width=10)

        self.link_lbl = tk.Label(self.window,
                                 text="Link: ",
                                 height=2,
                                 width=10)

        self.link_lbl.grid(row=1)
        self.topic_lbl.grid(row=0)

        # -- TEXT Entry for TOPIC/LINK -- #
        self.topic_txt = tk.Text(self.window, height=2, width=80)
        self.topic_txt.grid(row=0, column=1)

        self.link_txt = tk.Text(self.window, height=2, width=80)
        self.link_txt.grid(row=1, column=1)

        # -- OK BUTTON: Finalize Add functionality -- #
        self.ok_btn = tk.Button(self.window,
                                text="OK",
                                height=2,
                                width=10,
                                command=self.MVC.finalize_add)

        self.ok_btn.grid(row=3)

    def destroy_main_add_widgets(self):
        """ Simply remove the main widgets from the window """
        self.topic_lbl.destroy()
        self.link_lbl.destroy()
        self.topic_txt.destroy()
        self.link_txt.destroy()
        self.ok_btn.destroy()

    def destroy_add_widgets(self):
        """ Simply remove the widgets associated with the add operation """
        self.lbl.destroy()
        self.exit_btn.destroy()
        self.back_btn.destroy()

    def del_link_GUI(self):
        """ Display the GUI for deleting a link """
        # -- LABEL for LINK Entry -- #
        self.link_lbl = tk.Label(self.window,
                                 text="Link: ",
                                 height=2,
                                 width=10)
        self.link_lbl.grid(row=0)

        # -- TEXT Entry for LINK -- #
        self.link_txt = tk.Text(self.window, height=2, width=80)
        self.link_txt.grid(row=0, column=1)

        # -- OK button to finalize the add functionnality -- #
        self.ok_btn = tk.Button(self.window,
                                text="OK",
                                height=2,
                                width=10,
                                command=self.MVC.finalize_del)

        self.ok_btn.grid(row=2)

    def destroy_main_del_widgets(self):
        """ Simply remove the widgets associated with the add operation """
        self.link_lbl.destroy()
        self.link_txt.destroy()
        self.ok_btn.destroy()

    def destroy_del_widgets(self):
        """ Simply remove the widgets associated with the add operation """
        self.lbl.destroy()
        self.exit_btn.destroy()
        self.back_btn.destroy()

    def open_brow_GUI(self, topics):
        """ GUI for dropdown menu to open """
        # Add a grid
        self.mainframe = tk.Frame(self.window)
        self.mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.pack(pady=100, padx=100)

        # Create a Tkinter variable
        self.tkvar = tk.StringVar(self.window)

        # Dictionary with options
        self.tkvar.set('Select')  # set the default option

        self.popupMenu = tk.OptionMenu(self.mainframe, self.tkvar, *topics)
        self.label = tk.Label(self.mainframe, text="Choose Topic: ")
        self.label.grid(row=1, column=1)
        self.popupMenu.grid(row=2, column=1)

        # link function to change dropdown
        self.tkvar.trace('w', self.MVC.finalize_opening)

    def destroy_main_open_widgets(self):
        """Destroy: Main Widgets of Open """
        self.popupMenu.destroy()
        self.label.destroy()
        self.mainframe.destroy()

    def destroy_open_widgets(self):
        """ Destroy the last widgets due to open """
        self.lbl.destroy()
        self.back_btn.destroy()
        self.exit_btn.destroy()

    def display_message(self, success, option):
        """ Display a success or error message based on flags """
        success_message = error_message = ""
        if option == "add":
            success_message = "Successfully added new link."
            error_message = "An error occured while adding new link."
        elif option == "del":
            success_message = "Successfully deleted link."
            error_message = "An error occured while deleting link"
        else:
            success_message = "Successfully opened browser."
            error_message = "An error occured while opening browser."

        if success:
            self.lbl = tk.Label(self.window,
                                text=success_message,
                                height=3,
                                width=50)
            self.lbl.grid(row=0)
        else:
            self.lbl = tk.Label(self.window,
                                text=error_message,
                                height=3,
                                width=50)
            self.lbl.grid(row=0)

        self.exit_btn = tk.Button(self.window,
                                  text="Exit",
                                  height=3,
                                  width=10,
                                  command=self.MVC.close_program)

        self.back_btn = tk.Button(self.window,
                                  text="Back",
                                  height=3,
                                  width=10,
                                  command=self.MVC.go_back_main_menu)

        self.exit_btn.grid(row=1, column=0)
        self.back_btn.grid(row=1, column=1)
