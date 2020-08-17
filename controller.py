import gui as G
import backend as web


class Controller():
    """ Manage: GUI vs Back-End code """

    def __init__(self):
        self.add_flag = self.del_flag = self.open_flag = False
        self.browser = web.Browser("websites_saved.json")
        self.browser.load_links()
        self.GUI = G.MainGUI(self)
        self.GUI.window.mainloop()
        
    def display_Add_GUI(self):
        """ Display GUI: Add link """
        self.add_flag = True
        self.GUI.destroy_main_widgets()
        self.GUI.add_link_GUI()

    def finalize_add(self):
        """ Finalize: Add link """
        # -- GET User INPUT/ ADD New LINK -- #
        topic_input = self.GUI.topic_txt.get("1.0", "end-1c")
        link_input = self.GUI.link_txt.get("1.0", "end-1c")
        value = self.browser.add_new_link(topic_input, link_input)

        self.GUI.destroy_main_add_widgets()
        # -- Display a SUCCESS or ERROR message -- #
        if value:
            self.GUI.display_message(True, "add")
        else:
            self.GUI.display_message(False, "add")

        self.add_flag = False

    def display_Del_GUI(self):
        """ Display GUI: Remove link """
        self.del_flag = True
        self.GUI.destroy_main_widgets()
        self.GUI.del_link_GUI()

        
    def finalize_del(self):
        """ Finalize the deletion of the link """
        # -- Get user input and add new link -- #
        link = self.GUI.link_txt.get("1.0", "end-1c")
        value = self.browser.remove_link(link)

        self.GUI.destroy_main_del_widgets()
        # -- Display SUCCESS or ERROR message -- #
        if value:
            self.GUI.display_message(True, "del")
        else:
            self.GUI.display_message(False, "del")

        self.del_flag = False

    def open_Browser_GUI(self):
        """ Display: Browser GUI """
        self.open_flag = True
        self.GUI.destroy_main_widgets()

        topics = set(self.browser.get_topics())
        topics.add('Select')
        
        self.GUI.open_brow_GUI(topics)

    def finalize_opening(self, *args):
        """ Finally open the browser """
        self.GUI.destroy_main_open_widgets()

        topic = self.GUI.tkvar.get()
        status = self.browser.open_browser_GUI(topic)

        if status:
            self.GUI.display_message(True, "Open")
        else:
            self.GUI.display_message(False, "Open")

        self.open_flag = False

    def close_program(self):
        """ END PROGRAM """
        exit(0)

    def go_back_main_menu(self):
        """ Display: Main menu. """
        if self.add_flag:
            self.GUI.destroy_add_widgets()
        elif self.del_flag:
            self.GUI.destroy_del_widgets()
        else:
            self.GUI.destroy_open_widgets()

        self.GUI.display_menu()
