#GUI imports
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

#Imports from same directory

class FamilyConversation():

    def pick_player(alter_ego):
        """ DOCSTRING

        Parameters
        ------------

        Output
        ------------
        """
        family_relationships = alter_ego.roles.keys

        return family_relationships #these will then go into a spinner



    def pick_family_member(alter_ego, picked_member):
        """ DOCSTRING

              Parameters
              ------------

              Output
              ------------
              """

        convo_premise = alter_ego.roles[picked_member]

        return convo_premise


    def talk(convo_premise):
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

#GUI related code
class FamilyConversationPage(Screen):
    kv = Builder.load_file("GUI/cogs_game.kv") #Designating the .kv design file

    def __init__(self, **kwargs):  # defining an init method....LOOK UP WHY THIS IS NEEDED
        super().__init__(**kwargs)


    #def get_player_options(self, family):
        #return family.members