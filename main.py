""" Main module with all methods and initialization of app"""

# GUI related imports
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty, Clock
from kivy.uix.gridlayout import GridLayout
from functools import partial

# Imports from same directory
from Classes.person import Person

# Other imports
import random

class StartPage(GridLayout):
    kv = Builder.load_file("GUI/cogs_game.kv") #Designating the .kv design file

    # Creating properties for all objects in application to be able to communicate between Kivy and Python.
    welcome_lbl = ObjectProperty(None)
    create_character_lbl = ObjectProperty(None)
    set_name_lbl = ObjectProperty(None)
    set_name_input = ObjectProperty(None)
    set_age_lbl = ObjectProperty(None)
    set_age_input = ObjectProperty(None)
    create_person_btn = ObjectProperty(None)
    conversation_lbl = ObjectProperty(None)
    conversation_options = ObjectProperty(None)
    chatbox_history_layout = ObjectProperty(None)
    chatbox_history_lbl = ObjectProperty(None)
    message_input = ObjectProperty(None)
    send_btn = ObjectProperty(None)


    def create_person(self, name, age):
        """ This method takes name and age as parameters and creates a person for the player to be in the conversation.

              Parameters
              ----------
              name: string
                comes from the TextInput-widget for name in the app
              age: int
                comes from the TextInput-widget for age in the app

              Returns
              ----------
              - None

        """

        new_person = Person()
        new_person.name = name
        new_person.age = age

        return new_person


    def check_age(self, age):
        """ Checks if person is a child or not and determines what relations are possible. The possible relations
            become values in the drop-down menu.

                Parameters
                ----------
                age: int
                    comes from the TextInput-widget for age in the app

                Returns
                ----------
                - None

        """
        warning = ""

        if int(age) < 18:
            self.ids.conversation_options.values = ["parent", "sibling"]
        elif int(age) > 18:
            self.ids.conversation_options.values = ["parent", "partner", "child", "sibling"]
        else:
           return warning


    def matching_phrases(self, convo_premise):
        """ Based on who user chose to converse with, this method decide on
            fitting phrases for the chat bot responses.

              Parameters
              ----------
              convo_premise: string
                comes from the Spinner-widget (dropdown menu) for family members in the app

              Returns
              ----------
              answer: string
                returns a randomly picked phrase from list of possible answers that
                match with the role of the family member (conve_premise)
        """
        possible_answers = []

        if convo_premise == "parent":
            possible_answers = [
                "It's time for you to brush your teeth!",
                "Sleep tight my treasure <3",
                "Go to your room!",
                "As long as you're under my roof, you live by my rules!",
                "Your room looks like a cyclone ran through it.",
                "Talking to you is like talking to a brick wall.",
                "Let's play the quiet game.",
                "I'm so proud of you!",
                "Have you called granny recently?",
                "I'll make pancakes for dinner tonight",
                "I got a call from your teacher today...",
                "Where are your manners - were you raised by wolves?"
            ]
        elif convo_premise == "child":
            possible_answers = [
                "Are we there yet?",
                "I want ice cream",
                "Daniel's mom lets us eat ice cream on Tuesdays!",
                "I don't want to do homework!!!",
                "Can I play with Daniel after school tomorrow?",
                "Can you read me a bedtime story?",
                "I want to be an astronaut when I grow up",
                "I want to go to Disneyland"
            ]
        elif convo_premise == "partner":
            possible_answers = [
                "Honey...",
                "I told you this already!",
                "I love you",
                "I'm so happy it's you and I babe",
                "Do you want me to put on our song?",
                "You mean the world to me",
                "Let's have take out for dinner",
                "You're the June to my Johnny",
                "All I want for christmas is you",
                "Yes!",
                "Nah"
            ]
        elif convo_premise == "sibling":
            possible_answers = [
                "You're so annoying.",
                "Get out of my room!",
                "Hey that's my t-shirt!!",
                "Hahahah mom is such a dork by the way",
                "Did you eat all of my snacks?",
                "I'm so glad you're my sibling",
                "Us against mom and dad am I right?",
                "I'll tell mom!!"
            ]
        answer = random.choice(possible_answers)

        return answer


    # Following code is from Assignment 3
    def make_input_list(self, input):
        """ Makes the user input a list

                Parameters
                ----------
                input: string
                    comes from the TextInput-widget for chatbox in the app

                Returns
                ----------
                out_list: list
                    returns a list form of the input, where input has been split after every space
        """
        out_list = []

        temp_string = input.lower()
        temp_string = temp_string.split(' ')

        for x in temp_string:
            out_list.append(x)

        return out_list


    # Following code is from Assignmet 3
    def is_greeting(self, input_list):
        """ Determines if user input is a greeting or not, and returns a greeting if yes.

                Parameters
                ----------
                input_list: list
                    user input from the TextInput-widget for the chatbox in app, but in list form

                Returns
                ----------
                answer: string or None
                    returns a greeting if input_list contains greeting, if not: returns None
        """
        answer = ""
        greeting_input = ["hi", "hello", "hey"]
        conversation_starter = ["Hello! ", "Yo! ", "Hi! ", "Hey! ", "Where have you been? ", "Good to hear from you! ", "Hello my favorite person <3 "]

        for val in input_list:
            if val in greeting_input:
                answer = random.choice(conversation_starter)
                break
            else:
                answer = None

        return answer


    # Code below is inspired by sentdex's youtube series on kivy:
    # link: https://www.youtube.com/playlist?list=PLQVvvaa0QuDfwnDTZWw8H3hN_VRQfq8rF
    # specifically videos: "Chat Application Page - Kivy Mobile and Desktop App Dev w/ Python"
    # and "Finishing Chat Application - Kivy Mobile and Desktop App Dev w/ Python"
    def send_message(self):
        """ Takes user's input and put it in a label in the GUI. Clears the input box and calls on the
            function that prints the response in the same box.

                Parameters
                ----------
                - no parameters except "self"

                Returns
                ----------
                - None

          """
        sender = self.set_name_input.text
        message = self.message_input.text

        self.chatbox_history_lbl.text += (f"\n {sender} :  {message}")
        self.message_input.text = ""
        self.chatbox_history_layout.height = 100
        Clock.schedule_once(partial(self.family_member_response, message), 0.5) #>use Clock so that the family response will come 0.5 seconds later

    # Inspired by sentdex's youtube series on kivy
    def family_member_response(self, input, time_delay):
        """ Calls on talk() to print a response in the chatbox_history_lbl in GUI.
         Adds sender before message (e.g "parent: {message}")

                Parameters
                ----------
                input: string
                    string comes from the send_message method
                time_delay: float
                    the amount of time to wait to execute this method after it's been called

                Returns
                ----------
                - None

        """
        sender = self.conversation_options.text
        message = self.talk(input)
        self.chatbox_history_lbl.text += (f"\n {sender} :  {message}")


    # Following code is inspired by the talk method from Assignment 3
    def talk(self, input):
        """The function that runs the family conversation

                Parameters
                ----------
                input: string
                    comes from the TextInput-widget for chatbox in the app
                Returns
                ----------
                family_output: string
                    returns the phrase to be printed in chatbox label in the app
        """
        conversation = True

        while conversation:
            new_input = input
            family_output = ""
            player_input = self.make_input_list(new_input)

            if self.is_greeting(player_input):
                family_output += self.is_greeting(player_input)
                family_output += self.matching_phrases(self.ids.conversation_options.text)
            else:
                family_output = self.matching_phrases(self.ids.conversation_options.text)

            return family_output


# Setting up app - I figured this out when researching on several threads
# at stackoverflow.com and videos on Youtube
class COGSGameApp(App):
    def build(self):
        """ Initializes the application.

                Parameters
                ----------
                - no parameters except "self"

                Returns
                ----------
                StartPage: class
                    returns the StartPage window in the app

          """
        App.title = "COGS Game"
        Window.size = (1080, 720)

        return StartPage()

if __name__ == "__main__":
    COGSGameApp().run()





