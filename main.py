"""
projekt_1.py: první projekt do Engeto Online Datový analytik s Pythonem

author: Aneta Pípalová
email: anetaneub@seznam.cz
"""

TEXTS = [
    """Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.""",
    """At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.""",
    """The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.""",
]

registered = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

separator = "-" * 30
username = input("Username:")
password = input("Password:")
print(separator)

if username in registered and registered[username] == password:
    print(
        f"Welcome to the app, {username} \n"
        f"We have {len(TEXTS)} texts to be analyzed."
    )
    print(separator)
else:
    print(
        f"""
         username:{username}
         password:{password}
         unregistered user, terminating the program..
          """
    )
    exit()

choice = input("Enter a number btw. 1 and 3 to select:")
print(separator)


if not choice.isdigit() or int(choice) < 1 or int(choice) > len(TEXTS):
    print("Invalid choice")
    exit()

selected_text = TEXTS[int(choice) - 1]
words = selected_text.split()

#  Statistiky
words_count = len(words)
tittlecase_words = sum(1 for word in words if word.istitle())
uppercase_words = sum(1 for word in words if word.isupper() and word.isalpha())
lowercase_words = sum(1 for word in words if word.islower())
numbers = [word for word in words if word.isdigit()]
numeric_string = len(numbers)
numbers_sum = sum(int(num) for num in numbers)

#  Výstup
print(
    f"There are {words_count} words in the selected text.\n"
    f"There are {tittlecase_words} titlecase words.\n"
    f"There are {uppercase_words} uppercase words.\n"
    f"There are {lowercase_words} lowercase words.\n"
    f"There are {numeric_string} numeric strings.\n"
    f"The sum of all numbers is {numbers_sum}.\n"
    f"{separator}"
)

#  Tabulka s délkami slov
word_lengths = {}

for word in words:
    length = len(word)
    if length in word_lengths:
        word_lengths[length] += 1
    else:
        word_lengths[length] = 1

print("LEN| OCCURENCES  |NR.")
print(separator)

for length in sorted(word_lengths):
    print(f"{length:>3}|{'*' * word_lengths[length]:<13}|{word_lengths[length]}")
