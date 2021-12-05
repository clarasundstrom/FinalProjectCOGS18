from main import StartPage

class Tests():

    # Some tests
    def test_methods(self):

        # Create a person
        test_person = StartPage.create_person("Jill", 43)
        assert callable(StartPage.create_person)
        assert test_person.name == "Jill" and test_person.age == 43
        print("Tests are run!! 1")

        # Match phrases with family member
        test_phrase = StartPage.matching_phrases("sibling")
        assert callable(StartPage.matching_phrases)
        assert test_phrase ==  "You're so annoying." or "Get out of my room!" or "Hey that's my t-shirt!!" or "Hahahah mom is such a dork by the way"\
                            or "Did you eat all of my snacks?" or "I'm so glad you're my sibling" or "Us against mom and dad am I right?"\
                            or "I'll tell mom!!"

        print("Tests are run!! 2")

        #Say something as a result of user input
        test_age = StartPage.check_age("test")
        assert test_age == "Please select a number for age"

class RunTests():
    Tests.test_methods()


