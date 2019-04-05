import random
import sys
from urllib.request import urlopen

WORD_LIST = []
TEXT_URL = input("Paste in exact webpage url here: ")

STUDY_CARDS = {
    "def &&&(@@@)": "define a method called &&& that takes @@@ parameters",

    "class %%%(%%%):": "Create a class called %%% that is-a %%%.",

    "class %%%(object): def__init__self,&&&)": "class %%% has-a __init__ that takes self and @@@ parameters.",

    "class %%%(object): def &&&(self, @@@)": "class %%% has-a function &&& that takes self and parameters.",

    "&&& = %%%()": "Set &&& to an instance of class %%%.",

    "&&&.&&&(@@@)": "From &&& get the &&& function, call it with parameters self, @@@.",

    "&&&.&&& = '&&&'": "From &&& get the &&& attribute and set it to '&&&'."
}

print("Start study session. Type: flip at any time to reverse the flash cards.")

# Choose Order of Question Prompt
if len(sys.argv) == 2 and sys.argv[1] == "flip":
    Q_KEY_FIRST = True
else:
    Q_KEY_FIRST = False

for word in urlopen(TEXT_URL).readlines():
    WORD_LIST.append(str(word.strip(), encoding="utf-8"))

def convert(key, keyline):
    """Function converts list items to replace new strings with dictionary keys."""
    # For classes
    upper_case_words = [w.capitalize() for w in random.sample(WORD_LIST, key.count("%%%"))]
    # For non-classes
    lower_case_words = random.sample(WORD_LIST, key.count("&&&"))
    result_list = []
    parameters_names = []

    for i in range(0, key.count("@@@")):
        parameter_count = random.randint(1,3)
        parameters_names.append(', '.join(
            random.sample(WORD_LIST, parameter_count)))

    # Slice & replace() words in questions with dictionary keys
    for sentence in key, key_line:
        conv_result = sentence[:]

        for word in upper_case_words:
            conv_result = conv_result.replace("%%%", word, 1)

        for word in lower_case_words:
            conv_result = conv_result.replace("&&&", word, 1)

        for word in parameters_names:
            conv_result = conv_result.replace("@@@", word, 1)

        result_list.append(conv_result)

    return result_list

while True:

    question_keys = list(STUDY_CARDS.keys())

    random.shuffle(question_keys)

    # Create question List of QUESTIONS keys, make strings
    for key in question_keys:
        key_line = STUDY_CARDS[key]
        question, answer = convert(key,key_line)
        if Q_KEY_FIRST:
            question, answer = answer, question

        print(question)
        input("Type answer: ")
        print(f"Answer: {answer}\n\n")


