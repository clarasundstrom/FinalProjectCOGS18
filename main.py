#GUI related imports
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.spinner import Spinner
from Classes.family import FamilyInfoPage
from Classes.person import CreatePersonPage
from Classes.familyconversation import FamilyConversationPage

#Imports from same directory
from Classes.person import Person
from Classes.family import Family

#Defining screens
class PageManager(ScreenManager):
    pass

class StartPage(Screen):
    kv = Builder.load_file("GUI/cogs_game.kv") #Designating the .kv design file

    def __init__(self, **kwargs):  # defining an init method....LOOK UP WHY THIS IS NEEDED
        super().__init__(**kwargs)

class CreateFamilyPage(Screen):
    kv = Builder.load_file("GUI/cogs_game.kv") #Designating the .kv design file

    def __init__(self, **kwargs):  # defining an init method....LOOK UP WHY THIS IS NEEDED
        super().__init__(**kwargs)

    def create_family(self, name):
        new_family = Family()
        new_family.last_name = name

        return new_family.last_name

#Setting up app
pm = PageManager()

screens = [StartPage(name = "start_page"), CreateFamilyPage(name = "create_family_page"),
           FamilyInfoPage(name = "family_info_page"), CreatePersonPage(name = "create_person_page"),
           FamilyConversationPage(name = "family_conversation_page")]

for screen in screens:
    pm.add_widget(screen)

pm.current = "start_page"

class COGSGameApp(App):
    def build(self):
        App.title = "COGS Game"
        Window.size = (1080, 720)
        return pm

if __name__ == "__main__":
    COGSGameApp().run()


#Create relations - remove l8r
#print(test_person.possible_relations(test_person2))




