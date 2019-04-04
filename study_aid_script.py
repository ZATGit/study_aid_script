import random
import sys
from sys import argv

# Run 'python scriptFileName.py word_bank.txt'
script, text_file = argv

WORD_LIST = []

STUDY_CARDS = {
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

# Function for converting WORD_LIST items to strings
#and replacing words in questions with dictionary keys
def convert()

while True:

    question_keys = list(STUDY_CARDS.keys())

    random.shuffle(question_keys)

    # Create question List of QUESTIONS keys, make strings
    for key in question_keys:
        key_line = STUDY_CARDS[key]
        question, answer = answer, question

        print(question)
        print(input(f"Type your answer here: {answer}\n"))

