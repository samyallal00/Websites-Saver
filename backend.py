import webbrowser
import os
import json


class Browser():
    """ Browser of all links """
    def __init__(self, file):
        self.file = file
        self.data = {}

    def load_links(self):
        """ Load links from a json file """
        if os.path.exists(self.file):
            with open(self.file) as json_file:
                self.data = json.load(json_file)    

    def add_new_link(self, topic, link):
        """ Add new link to the disctionnary data """
        if topic in self.data.keys():
            self.data[topic].append(link)
            print('Successfully added link to existing topic.')
        else:
            self.data[topic] = [link]
            print('Successfuly added a new topic and the link.')

        self._update_file()
        return True
    
    def remove_link(self, link):
        """ Remove existing link from dictionnary """
        flag = 0
        for topic in self.data.keys():
            if link not in self.data[topic]:
                print('Link non existent.')
            else:
                self.data[topic].remove(link)
                flag = 1
                print('Link removed from file.')
                if len(self.data[topic]) == 0:
                    print('No more links for' + topic + ". Erased.")
                    new_data = {k:v for k,v in self.data.items() if v}
                    self.data = new_data
                
        self._update_file()

        if(flag):
            return True
        else:
            return False

    def _update_file(self):
        """ Update the json file """
        if os.path.exists(self.file):
            os.remove(self.file)
        else:
            print("The file does not exist.")

        with open(self.file, 'w') as f:
            json.dump(self.data, f)

        
    def display_menu(self):
        """ Display menu of topics for the user """
        topic_id = 0
        print('Add new topic? Enter -1')
        print('Remove existing topic? Enter -2\nOr..')
        print('Choose the topic you have already saved:')
        for topic in self.data.keys():
            print(str(topic_id) + " - " + topic)
            topic_id += 1

    def get_topics(self):
        """ Return the keys of the dictionnary """
        return list(self.data.keys())

    def get_links(self, topic):
        """ Return links specific to topic """
        return list(self.data[topic])

    def open_browser_GUI(self, topic):
        """ Open the browser for the GUI version """
        websites = self.data[topic]
        try:
            os.system("/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome")
            for web in websites:
                webbrowser.get(using='chrome').open(web, new=2)
                
                print('Successfully opened your saved websites.')
            return True
        except:
            return False

    def open_browser(self, option):
        """ Open browser of links """
        i = 0
        websites = []
        for item in self.data.keys():
            if i == option:
                websites = self.data[item]
            i += 1

        os.system("/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome")
        for web in websites:
            webbrowser.get(using='chrome').open(web, new=2)
            
        print('Successfully opened your saved websites.')
        exit(0)



def process_input(browser):
    """ Read input from the user and act on it """
    choice = input("\nEnter your choice: ")
    read = int(choice)

    topic = link = ""
    if read == -1:
        while(topic != "STOP" or link != "STOP"):
            topic = input('Enter topic first: ')
            link = input('Enter the link now: ')
            if topic != "STOP" or link != "STOP":
                browser.add_new_link(topic, link)
    elif read == -2:
        link = input('Enter link to delete: ')
        browser.remove_link(link)
    else:
        browser.open_browser(read)



""" THIS IS THE TERMINAL VERSION NOT THE GUI """
""" THE GUI VERSION IS SUPERIOR. SEPARATE FILE """
def launch():
    """ Launch the websites """
    file = "websites_saved.json"
    browser = Browser(file)

    browser.load_links()
    browser.display_menu()
    process_input(browser)
    
