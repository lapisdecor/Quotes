import json
import random

with open("unique_quotes.json", "r") as read_file:
    data = json.load(read_file)

better_data = data["data"]

choices = []

for dados in better_data:
    my_string = ""
    if dados['quote']:
        my_string += "\n"
        my_string += dados['quote'] + "\n"
    if dados['author']:
        my_string += "~~ " + dados['author'] + "\n\n"
        choices.append(my_string)

print(random.choice(choices))
