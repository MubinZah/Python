# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 21:08:07 2026

@author: Zahin
"""
'''
import random
import re
STORY_POOL = [
    "One day a lonely [noun] decided to [verb] for love. So started to search for it.",
    "To watch [adjective] movies, anyone have to [verb] it and stick to the stereo type.",
    "No one can [verb] life untill [pronoun] decide to live through it. you must [verb2] differtly."
    ]
def play_mad_libs():
    print("--- Welcome to the Dynamic Mad Libs Generator! ---\n")
    story = random.choice(STORY_POOL)
    placeholders = re.findall(r'\[(.*?)\]', story)
    user_inputs = {}
    for placeholder in placeholders:
        if placeholder[0].lower() in "aeiou":
            article = "an"
        else:
            article = "a"
        user_word = input(f"Enter {article} {placeholder} ").strip()
        if not user_word:
            user_word = f"[you didnt type]"
            
        user_inputs[placeholder] = user_word



    final_story = story
    for placeholder, word in user_inputs.items():
        final_story = final_story.replace(f"[{placeholder}]", word, 1)
   
    print("\n--- Here is your masterpiece! ---")
    print(final_story)
    print("----------------")
if __name__ == "__main__":
    play_mad_libs()
    '''
import random
import re

STORY_POOL = [
    "I once [Transitive Verb] a [Common Noun]. He [Auxiliary verb] very kind. He [Intransitive verb]",
    "I am [Action verb] because I want to [Transitive verb] my life. So that I can [Intransitive verb]",
    "In this world, It's very important to [Intranstive verb]. Because Everyone can't enjoy [Abstract Noun]"
     ]
def play_mad_libs():
    print("Welocome to Life building tasks")
    story = random.choice(STORY_POOL)
    definedplaces = re.findall(r"\[(.*?)\]", story)
    user_entry = {}
    for definedplace in definedplaces:
        if definedplace[0].lower() in "aeiou":
            article = "a"
        else:
            article = "an"
        user_typed = input(f"Enter {article} {definedplace} : ").strip()
        if not user_typed:
            user_typed = f"[Madarchod tui ekta]"
        
        user_entry[definedplace] = user_typed    
        
        
    final_story = story    
    for definedplace, word in user_entry.items():
        final_story = final_story.replace(f"[{definedplace}]", word, 1)
        
    print("Hello, with own trying. let's explain")
    print(final_story)
    print("Finished")
    
    
if __name__ == "__main__":
   play_mad_libs()    
   
'''
Variables: story, definedplaces, user_typed, final_story
Strings: Characters, f string list where it tells Python to look into the curly braces and replace it with inputted words
Lists: Story_POOL
Functions: def_mad_libs is a function
Loop:for loop, it runs as many times as it met the condition. in this code the condition is finding the curly braces in the selectec story.
'''
    
   
   
   
    



