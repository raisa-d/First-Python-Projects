#using an f string
greeting = input("Greeting: ")
adj1 = input("Adjective: ")
verb1 = input("Verb: ")
color = input("Color: ")
verb2 = input("Verb: ")

fairy_story = f'''I looked in the garden and saw a fairy hiding under a mushroom cap.
I went over and said {greeting}! She was so {adj1} it made me {verb1}. Her wings were {color}
and they {verb2} in the sun.'''

time_of_day = input("Time of day: ")
noun1 = input("Noun: ")
noun2 = input("Noun: ")
body_parts = input("Body parts: ")

mermaid_story = f'''I woke up this {time_of_day} and hopped in the {noun1}. As soon as the {noun2} hit my head, I fell down
and a tail emerged where there used to be {body_parts}! I couldn't believe my eyes. '''

story_choice = input("Which do you prefer? A story about fairies (F) or mermaids? (M): ").upper()
if story_choice == "F":
    print(fairy_story)
else:
    print(mermaid_story)