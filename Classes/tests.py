from family import Family
from person import Person
from familyconversation import FamilyConversation

class Tests():
    # Testing

    # Create a family DON'T KNOW HOW TO TEST DO YET
    def test_
    test_family = Family("McGill")
    assert callable(test_family)
    assert test_family.last_name == "McGill"

    # Create a person - DON'T KNOW HOW TO TEST DO YET
    test_person = Person("Jill", 43)
    assert test_person.name == "Jill" and test_person.age == 43

    test_person2 = Person("Jill", 2)
    assert test_person2.name == "Jill" and test_person2.age == 2

    # Add person to family
    def test_add_member():
        assert callable(add_member)

    test_family.add_member(test_person)
    assert test_family.members == ["Jill"]

    # Try to add person with existing name
    test_family.add_member(test_person2)
    print(test_family.members)

    # Check family size
    print(test_family.check_size())

    # Change name of person
    # NOTE name will JUST change name in object - not in test_family.members i.e.
    # It's ok as it won't be possible to add person with same name.
    # You can only change name when fail to add to family bc of same name.

    # test_person.change_name("Lola")
    # print(test_person.name)
