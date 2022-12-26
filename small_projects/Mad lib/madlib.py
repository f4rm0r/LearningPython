profession = str(input("insert a profession here: "))

need_help = input(str(f"""Welcome to this madlib! This one is named "A visit to the {profession}".

To play this game you nned to know what 'Adjectives', 'Nouns', etc are.
Do you need an explanation of what these definitions are?
Answer 'Y' or 'y' if needed: """))

need_help = str(need_help).lower()

print(need_help)

if need_help == "y":
    print("Verb: a word used to describe an action, state, or occurrence, and forming the main part of the predicate of a sentence, such as hear, become, happen.")
    print("Adjective: a word naming an attribute of a noun, such as sweet, red, or technical.")
    print("Noun: A noun is a word that represents a person, thing, concept, or place (e.g., “John,” “house,” “affinity,” “river”)")


Plural_noun0 = str(input("Plural Noun: "))
Person_in_room = str(input("Person in room(lastname): "))
Adjective0 = str(input("Adjective: "))
Noun0 = str(input("Noun: "))
Noun1 = str(input("Noun: "))
part_of_the_body = str(input("A part of your body: "))
Plural_noun1 = str(input("Plural nount: "))
Noun2 = str(input("Noun: "))
Noun3 = str(input("Noun: "))
Noun4 = str(input("Noun: "))
Verb0 = str(input("Verb: "))
Adjective1 = str(input("Adjective: "))
Noun5 = str(input("Noun: "))

input(" You have now entered everything needed to fill in the blanks in this story. Press enter to your masterpiece.")

print(f""" A visit to the {profession}. 
A one-act play to be performed by two {Plural_noun0} in this room.

Patient: Thank you so very much for seeing me, {profession} {Person_in_room}, on such {Adjective0} notice.

{profession}: What is your problem, young {Noun0}?

Patient: I have a pain in my upper {Noun1}, which is giving me a severe {part_of_the_body} ache.

{profession}: Let me take a look. Open your {part_of_the_body} wide.
Good, Now I'm going to tap your {Plural_noun1} with my {Noun2}.

Patient: Shouldn't you give me a {Noun1} killer?

{profession}: It's not necessary yet. I think I see a {Noun4} in your upper {Noun1}.

Patient: Are you ging to pull my {Noun1} out?

{profession}: No.I'm going to {Verb0} your {part_of_the_body} and put in a temporary {Noun1}.

Patient: When do 1 come back for the {Adjective1} filling?

{profession}: A day after I cash your {Noun5}.

""")