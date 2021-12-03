#GUI related imports
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout


#Imports from same directory
from Classes.person import Person

#Imports
import random

#Defining screens
Window.size = (1920, 1080)

class StartPage(GridLayout):
    kv = Builder.load_file("GUI/cogs_game.kv") #Designating the .kv design file

    welcome_lbl = ObjectProperty(None)
    create_character_lbl = ObjectProperty(None)
    set_name_lbl = ObjectProperty(None)
    set_name_input = ObjectProperty(None)
    set_age_lbl = ObjectProperty(None)
    set_age_input = ObjectProperty(None)
    create_person_btn = ObjectProperty(None)
    conversation_lbl = ObjectProperty(None)
    conversation_options = ObjectProperty(None)
    chatbox_history_lbl = ObjectProperty(None)
    scroll_to_lbl = ObjectProperty(None)
    message_input = ObjectProperty(None)
    send_btn = ObjectProperty(None)

    def __init__(self, **kwargs):  # defining an init method....LOOK UP WHY THIS IS NEEDED
       super().__init__(**kwargs)

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
        print(new_person.name, ' ', new_person.age)

    def check_age(self, age):
        #options = []
        warning = ""

        if int(age) < 18:
            self.ids.conversation_options.values = ["parent", "sibling"]
            #options = ["child", "sibling"]
        elif int(age) > 18:
            self.ids.conversation_options.values = ["parent", "partner", "child", "sibling"]
            #options = ["parent", "partner", "child", "sibling"]
        else:
            warning = "Please select a number for age"
        print(self.ids.conversation_options.values)
        #return options

    def matching_phrases(self, convo_premise):
        """ DOCSTRING

              Parameters
              ------------

              Output
              ------------
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
                "You're the June to my Johnny"
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
        #print(answer + "print")
        return answer

    #From Assignmet 3
    def is_greeting(self, input_list):
        answer = ""
        greeting_input = ["hi", "hello"]
        conversation_starter = ["Hello!", "Yo", "Hi", "Hey!", "Where have you been?", "Good to hear from you!", "Hello my favorite person <3"]

        for val in input_list:
            if val in greeting_input:
                answer = random.choice(conversation_starter)
                print(answer + " bobob")
            else:
                answer = None

        return answer

    def make_input_list(self, input):
        out_list = []

        temp_string = input.lower()
        temp_string = temp_string.split(' ')

        for x in temp_string:
            out_list.append(x)

        return out_list

    #Functions below are from xxx's youtube series on kivy (link: xxx)
    def send_message(self):
        sender = self.set_name_input.text
        message = self.message_input.text

        self.chatbox_history_lbl.text = (f"{sender} :  {message}")
        self.message_input.text = ""

    def focus_on_input(self):
        self.ids.message_input.focus = True

    def family_member_response(self):
        put = self.update_chat_history_lbl(f"[color = 20dd20]{self.ids.conversation_options.text}[/color] > {self.talk()}")
        return put

    def update_chat_history_lbl(self):
        sender = self.set_name_input.text
        message = self.message_input.text

        self.chatbox_history_lbl.text = (f"{sender} :  {message}")
        self.message_input.text = ""

        label_content = self.ids.chatbox_history_lbl.text

        label_content += "\n" + message + "\n it works indeed"

        self.ids.chatbox_layout.height = self.ids.chatbox_history_lbl.texture_size[1] + 15
        self.ids.chatbox_history_lbl.height = self.ids.chatbox_history_lbl.texture_size[1]

    def on_key_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 40:
            self.send_message()

    #From Assignment 3
    def talk(self):
        """The function that runs the family conversation"""
        #self.update_chat_history_lbl(f"[color = dd2020]{self.ids.set_name_input.text}[/color] > {self.ids.message_input.text}")

        conversation = True

        while conversation:
            new_input = self.ids.message_input.text
            print(new_input + " is the input")
            family_output = ""

            player_input = self.make_input_list(new_input)
            family_output = self.is_greeting(player_input)
            family_output = self.matching_phrases(self.ids.conversation_options.text)
            #self.update_chat_history_lbl(f"[color = 20dd20]{self.ids.conversation_options.text}[/color] > {family_output}")

            print(family_output + " is printed from talk()")
            return family_output

#Setting up app
class COGSGameApp(App):
    def build(self):
        App.title = "COGS Game"
        Window.size = (1080, 720)
        return StartPage()

if __name__ == "__main__":
    COGSGameApp().run()





