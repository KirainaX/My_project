# Prompt the user for input to fill in the blanks of a short story template.
noun = input("Noun (plural): ")
adj = input("Adjective: ")
verb = input("Verb (past tense): ")
adverb = input("Adverb: ")
color = input("Color: ")
animal = input("Animal: ")
number = input("Number: ")

# Construct and print a whimsical short story using the user-provided inputs.
print("Once upon a time, in a land filled with {}, there lived a {} and {} group of {} wolves. One day, as they {} by the river, a mysterious {} appeared.\nThe wolf spoke in {} different languages and shared tales of its adventures.\nThe wolves were amazed and decided to join the wolf on a journey to explore the {} unknown. And so, their {} adventure began, filled with laughter, surprises, and {}.\nThe end.".format(noun, adj, adverb, color, verb, animal, number, adverb, adj, noun))
