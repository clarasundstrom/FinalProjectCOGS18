class Person():

    def create_person(self, name, age):
        """ Creates a ne person

              Parameters
              ------------
              name: string
                string comes from TextInput-widget for name in app
              age: int
                int comes from TextInput-widget for age in app

              Output
              ------------
              new_person: Person
                returns the newly created person 
              """
        new_person = Person()
        new_person.name = name
        new_person.age = age

        return new_person