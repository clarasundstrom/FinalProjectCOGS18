#GUI imports
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

#Import
from random import random

class FamilyConversation():


    def check_question(input_list):
        output = False

        if '?' in input_list[-1]:
            output = True

        return output

    def select_output(input_list, check_list, return_list):
        output = None

        for x in input_list:
            if x in check_list:
                output = random.choice(return_list)
                break
        return output

