#GUI related imports
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

#Imports from same directory
from Classes.person import Person
from Classes.family import Family

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
#kv = Builder.load_file('GUI/cogs_game.kv')

#class COGSGameApp(App):
    #def build(self):
        #return kv

#if __name__ == "__main__":
    #COGSGameApp().run()

#Testing

#Create a family
test_family = Family("McGill")
assert test_family.last_name == "McGill"

#Create a person
test_person = Person("Jill", 43)
assert test_person.name == "Jill" and test_person.age == 43

test_person2 = Person("Jill", 2)
assert test_person2.name == "Jill" and test_person2.age == 2

#Add person to family
test_family.add_member(test_person)
assert test_family.members == ["Jill"]

#Try to add person with existing name
test_family.add_member(test_person2)
print(test_family.members)

#Check family size
print(test_family.check_size())

#Change name of person
#NOTE name will JUST change name in object - not in test_family.members i.e.
# It's ok as it won't be possible to add person with same name.
# You can only change name when fail to add to family bc of same name.

#test_person.change_name("Lola")
#print(test_person.name)

#Create relations
print(test_person.relations(test_person2))




