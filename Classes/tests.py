""" Test file containing tests for some methods in the project"""
from main import StartPage
import pytest

class Tests():

    # Some tests
    def test_create_person(self):
        """ Test to create a person """
        test_person = StartPage.create_person("Jill", 43)
        assert callable(StartPage.create_person)
        assert test_person.name == "Jill" and test_person.age == 43
        print("Tests run!! 1")


    def test_matching_phrases(self):
        """ Test to match phrases with family member """
        test_phrase = StartPage.matching_phrases("sibling")
        assert callable(StartPage.matching_phrases)
        assert test_phrase ==  "You're so annoying." or "Get out of my room!" or "Hey that's my t-shirt!!" or "Hahahah mom is such a dork by the way"\
                            or "Did you eat all of my snacks?" or "I'm so glad you're my sibling" or "Us against mom and dad am I right?"\
                            or "I'll tell mom!!"

        print("Tests run!! 2")


    def test_check_age(self):
        """Test to check if age input is valid """
        test_age = StartPage.check_age("test")
        assert test_age == "Please select a number for age"
        print("Test run 3!!!")

    def run_all_tests(self):
        """Runs all test methods"""
        self.test_create_person()
        self.test_matching_phrases()
        self.test_check_age()
