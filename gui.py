import tkinter as tk
import open_web as web

class MainGUI():
    """ Create and design the GUI """
    def __init__(self):
        self.window = tk.Tk()
        self.display_menu()
        self.browser = web.Browser("websites_saved.json")
        self.browser.load_links()
        self.add_flag= self.del_flag=0
        self.window.mainloop()

    def display_menu(self):
        """ Display the menu of commands """
        add = "Add new link?"
        delt =  "Remove topic?"
        openl = "Open browser."
        
        self.add_button = tk.Button(self.window,
                                    text=add,
                                    height = 5, 
                                    width = 30,
                                    command=self._add_link)

        self.del_button = tk.Button(self.window,
                                    text=delt,
                                    height = 5,
                                    width = 30,
                                    command=self._del_link)

        #self.open_button = tk.Button(self.window, text=openl, command=self._open_brow)
        
        self.add_button.pack()
        self.del_button.pack()
        #self.open_browser.pack()

    
    def _add_link(self):
        """ Function called when add button is clicked """
        self.add_button.destroy()
        self.del_button.destroy()
        #self.open_button.pack_forget()

        self.add_flag = 1
        # -- Label for topic entry -- #
        self.topic_lbl = tk.Label(self.window,
                                  text="Topic: ",
                                  height = 2, 
                                  width = 10)
        self.topic_lbl.grid(row=0)

        # -- Text entry for topic -- #
        self.topic_txt = tk.Text(self.window, height=2, width=80)
        self.topic_txt.grid(row=0, column=1)


        # -- Label for link entry -- #
        self.link_lbl = tk.Label(self.window,
                                 text="Link: ",
                                 height = 2,
                                 width = 10)
        self.link_lbl.grid(row=1)
        
        # -- Text entry for link -- #
        self.link_txt = tk.Text(self.window, height=2, width=80)
        self.link_txt.grid(row=1, column=1)

        # -- OK button to finalize the add functionnality -- #
        self.ok_btn = tk.Button(self.window,
                                text="OK",
                                height=2,
                                width=10,
                                command=self._finalize_add)
        
        self.ok_btn.grid(row=3)

        
    def _finalize_add(self):
        """ When OK button pressed get user imput and add the new link """
        # -- Get user input and add new link -- #
        topic_input = self.topic_txt.get("1.0","end-1c")
        link_input = self.link_txt.get("1.0","end-1c")
        
        self.browser.add_new_link(topic_input, link_input)

        self._destroy_main_widgets()

        # -- Display a Success message -- #
        self.success_lbl = tk.Label(self.window,
                                    text="Successfully added the new link.",
                                    height=3,
                                    width=50)

        self.exit_btn = tk.Button(self.window,
                                  text="Exit",
                                  height=3,
                                  width=10,
                                  command=lambda: exit(0))

        self.back_btn = tk.Button(self.window,
                                  text="Back",
                                  height=3,
                                  width=10,
                                  command=self._go_back_main_menu)
        
        self.success_lbl.grid(row=0)
        self.exit_btn.grid(row=1, column=0)
        self.back_btn.grid(row=1, column=1)
        

    def _go_back_main_menu(self):
        """ Display the main menu again """
        if self.add_flag:
            self._destroy_add_widgets()
        elif self.del_flag:
            self._destroy_del_widgets()
            
        self.display_menu()
        
    def _destroy_main_widgets(self):
        """ Simply remove the main widgets from the window """
        self.topic_lbl.destroy()
        self.link_lbl.destroy()
        self.topic_txt.destroy()
        self.link_txt.destroy()
        self.ok_btn.destroy()
        
    def _destroy_add_widgets(self):
        """ Simply remove the widgets associated with the add operation """
        self.success_lbl.destroy()
        self.exit_btn.destroy()
        self.back_btn.destroy()


    def _del_link(self):
        """ Display the GUI for deleting a link """
        self.add_button.destroy()
        self.del_button.destroy()
        #self.open_button.pack_forget()                                                                     

        self.del_flag = 1
        # -- Label for link entry -- #
        self.link_lbl = tk.Label(self.window,
                                 text="Link: ",
                                 height = 2,
                                 width = 10)
        self.link_lbl.grid(row=0)
        
        # -- Text entry for link -- #
        self.link_txt = tk.Text(self.window, height=2, width=80)
        self.link_txt.grid(row=0, column=1)

        # -- OK button to finalize the add functionnality -- # 
        self.ok_btn = tk.Button(self.window,
                                text="OK",
                                height=2,
                                width=10,
                                command=self._finalize_del)

        self.ok_btn.grid(row=2)

    def _finalize_del(self):
        """ Finalize the deletion of the link """
        # -- Get user input and add new link -- # 
        link_input = self.link_txt.get("1.0","end-1c")
        value = self.browser.remove_link(link_input)

        self._destroy_main_del_widgets()
        
        # -- Display a Success message -- #
        if value:
            self.lbl = tk.Label(self.window,
                                text="Successfully deleted the link provided.",
                                height=3,
                                width=50)
            self.lbl.grid(row=0)
        else:
            self.lbl = tk.Label(self.window,
                                text="Non-existent link.",
                                height=3,
                                width=50)
            self.lbl.grid(row=0)
            
        self.exit_btn = tk.Button(self.window,
                                  text="Exit",
                                  height=3,
                                  width=10,
                                  command=lambda: exit(0))
    
        self.back_btn = tk.Button(self.window,
                                  text="Back",
                                  height=3,
                                  width=10,
                                  command=self._go_back_main_menu)

        self.exit_btn.grid(row=1, column=0)
        self.back_btn.grid(row=1, column=1)

    def _destroy_main_del_widgets(self):
        """ Simply remove the widgets associated with the add operation """
        self.link_lbl.destroy()
        self.link_txt.destroy()
        self.ok_btn.destroy()

    def _destroy_del_widgets(self):
        """ Simply remove the widgets associated with the add operation """
        self.lbl.destroy()
        self.exit_btn.destroy()
        self.back_btn.destroy()
