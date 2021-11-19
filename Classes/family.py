class Family():

    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []
        self.members_total = 0


    #Adds a member to the family
    def add_member(self, new_member):
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
       members_total = len(self.members)

       return members_total
