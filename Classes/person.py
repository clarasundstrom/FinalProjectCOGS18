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

