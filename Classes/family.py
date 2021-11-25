#GUI imports
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

class Family():

    def __init__(self):
        self.last_name = ""
        self.members = []
        self.members_total = 0


    #Adds a member to the family
    def add_member(self, new_member):
        """ DOCSTRING

              Parameters
              ------------

              Output
              ------------
              """
        if new_member.name not in self.members:
            self.members.append(new_member.name)
        else:
            print("A family member with this name already exists!")
            answer = input("Type “yes” to change name: ")

            test = True
            while test == True:
                if answer == "yes" or answer == "Yes":
                    changed = False
                    new_name = input("Change name to: ")
                    new_member.change_name(new_name)
                    changed = True

                    if changed:
                        self.add_member(new_member)

                    test = False
                    break

                else:
                    answer = input("Unvalid input! Type 'yes' or 'Yes': ")

    #Checks current size of family
    def check_size(self):
        """ DOCSTRING

              Parameters
              ------------

              Output
              ------------
              """
        members_total = len(self.members)

        return members_total


#GUI related code
class FamilyInfoPage(Screen):
    kv = Builder.load_file("GUI/cogs_game.kv") #Designating the .kv design file

    def __init__(self, **kwargs):  # defining an init method....LOOK UP WHY THIS IS NEEDED
        super().__init__(**kwargs)

    def load_info(self):
        """ The idea is to load the family name into the label in family info page :(
        """
        self.root.ids.lbl_family_title.text = f'{self.root.ids.l_name_input.text} family'


