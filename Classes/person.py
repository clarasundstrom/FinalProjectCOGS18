#GUI imports
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


class Person():

    def __init__(self):
        self.name = ""
        self.age = ""
        self.last_name = ""
        self.roles = {}

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

        return new_person.name

    def change_name(self, new_name):
        """ DOCSTRING

              Parameters
              ------------

              Output
              ------------
              """
        self.name = new_name

    def possible_relations(self, family_member):
        """ DOCSTRING

              Parameters
              ------------

              Output
              ------------
              """
        options = []
        if self.age > 18 and family_member.age < 18:
            options = ["Sibling", "Parent"]
        elif self.age > 18 and family_member.age > 18:
            options = ["Partner", "Sibling", "Child", "Parent"]
        elif self.age < 18 and family_member.age < 18:
            options = ["Sibling"]
        elif self.age < 18 and family_member.age > 18:
            options = ["Sibling" "Child"]

        return options


    def set_relation(self, fam_member_name, selected_option):
        """ DOCSTRING

              Parameters
              ------------

              Output
              ------------
              """
        self.roles[fam_member_name] = selected_option


#GUI related code
class CreatePersonPage(Screen):
    kv = Builder.load_file("GUI/cogs_game.kv") #Designating the .kv design file

    def __init__(self, **kwargs):  # defining an init method....LOOK UP WHY THIS IS NEEDED
        super().__init__(**kwargs)

    def spinner_clicked(self, value):
        self.ids.set_rel_lbl.text = f'You selected: {value}'