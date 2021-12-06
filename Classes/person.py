class Person():

    def create_person(self, name, age):
        """ Method that creates an object of type Person

              Parameters
              ------------
              name: string

                string comes from TextInput-widget for name in app
              age: int
                int comes from TextInput-widget for age in app

              Return
              ------------
              new_person: Person
                returns an object of type Person

              """
        new_person = Person()
        new_person.name = name
        new_person.age = age

        return new_person