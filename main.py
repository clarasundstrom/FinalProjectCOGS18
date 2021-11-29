#GUI related imports
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

#Imports from same directory
from Classes.person import Person

#Defining screens
Window.size = (1920, 1080)

class StartPage(GridLayout):
    kv = Builder.load_file("GUI/cogs_game.kv") #Designating the .kv design file

    def __init__(self, **kwargs):  # defining an init method....LOOK UP WHY THIS IS NEEDED
       super().__init__(**kwargs)

    def create_person(self, name, age):
        """ DOCSTRING

              Parameters
              ------------

              Output
              ------------
              """
        new_person = Person()
        new_person.name = name
        new_person.age = age
        print(new_person.name, ' ', new_person.age)

    def check_age(self, age):
        #options = []
        warning = ""

        if int(age) < 18:
            self.ids.conversation_options.values = ["child", "sibling"]
            #options = ["child", "sibling"]
        elif int(age) > 18:
            self.ids.conversation_options.values = ["parent", "partner", "child", "sibling"]
            #options = ["parent", "partner", "child", "sibling"]
        else:
            warning = "Please select a number for age"
        print( self.ids.conversation_options.values)
        #return options

#Setting up app
class COGSGameApp(App):
    def build(self):
        App.title = "COGS Game"
        Window.size = (1080, 720)
        return StartPage()

if __name__ == "__main__":
    COGSGameApp().run()


#Create relations - remove l8r
#print(test_person.possible_relations(test_person2))




