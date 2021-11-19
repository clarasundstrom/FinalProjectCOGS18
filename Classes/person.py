class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.last_name = ""
        self.roles = {}


    def change_name(self, new_name):
        self.name = new_name


    def relations(self, family_member):
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



