import random
import sys
from sys import argv

# Run 'python scriptFileName.py word_bank.txt'
script, text_file = argv

print(f"Start Study Session for {script}")

WORD_LIST = []

STUDY_CARDS = {
    "def &&&(@@@)": "define a method called &&& that takes @@@ parameters",

    "class %%%(%%%):": "Create a class called %%% that is-a %%%.",

    "class %%%(object): def__init__self,&&&)": "class %%% has-a __init__ that takes self and @@@ parameters.",

    "class %%%(object): def &&&(self, @@@)": "class %%% has-a function &&& that takes self and parameters.",

    "&&& = %%%()": "Set &&& to an instance of class %%%.",

    "&&&.&&&(@@@)": "From &&& get the &&& function, call it with parameters self, @@@.",

    "&&&.&&& = '&&&'": "From &&& get the &&& attribute an set it to '&&&'."
}

# Choose Order of Question Prompt
if len(sys.argv) == 2 and sys.argv[1] == "flip":
    Q_KEY_FIRST = True
else:
    Q_KEY_FIRST = False

# Copy Words From text_file to List
# Need to convert from string to list for readlines()
for word in text_file.readlines():
    WORD_LIST.append(str(word.strip(), encoding="utf-8"))

def convert(key, keyline):
    """Function converts list items to replace new strings with dictionary keys."""
    # For non-classes
    lower_case_words = random.sample(WORD_LIST, key.count("&&&"))
    # For classes
    upper_case_words = [w.capitalize() for w in random.sample(WORDS_LIST, key.count("%%%"))]
    master_list = []
    parameters_names = []

    for i in range(0, key.count("@@@")):
        parameter_count = random.randint(1,3)
        parameter_names.append(', '.join(
            random.sample(WORDS_LIST, parameter_count)))

    # Slice & replace() words in questions with dictionary keys
    for sentence in key, key_line:
        master_list = sentence[:]

        for word in upper_case_words:
            master_list = master_list.replace("%%%", word, 1)

        for word in lower_case_words:
            master_list = master_list.replace("&&&", word, 1)

        for word in parameters_names:
            master_list = master_list.replace("@@@", word, 1)

    master_list.append(master_list)

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
        print(input(f"Type your answer here: {answer}\n"))

