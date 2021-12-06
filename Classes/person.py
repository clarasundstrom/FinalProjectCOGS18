class Person():

    def create_person(self, name, age):
        """ Method that creates an object of type Person

              Parameters
              ------------
              name: string
                input from the create_person method in main
              age: int
                input from the create_person method in main

              Return
              ------------
              new_person: Person
                returns an object of type Person
              """
        new_person = Person()
        new_person.name = name
        new_person.age = age

        return new_person