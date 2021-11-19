from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


#Defining screens
class StartPage(Screen):
    pass

class CreateFamilyPage(Screen):
    pass

class FamilyInfoPage(Screen):
    pass

class CreatePersonPage(Screen):
    pass

class FamilyConversationPage(Screen):
    pass

class PageManager(ScreenManager):
    pass

#Designating the .kv design file
kv = Builder.load_file('GUI/cogs_game.kv')

class COGSGameApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    COGSGameApp().run()

