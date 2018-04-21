from pprint import pprint
import json

quotes: dict = []
final: dict = []

level: int = 0

with open("./quotes.txt") as file:
    for line in file:
        if len(line) > 1:
            quotes.append(line)

for i in quotes:
    if len(i) < 5:
        print("i")

quote: str = ''
level = 0
for i in quotes:
    try:
        if level == 0:
            quote = i
            level = 1
        else:
            final.append({"quote": quote, "author": i.split('-')[-1]})
            level = 0
            quote = ''
    except Exception as e:
        print(f"error {level}")

with open('result.json', 'w') as fp:
    json.dump(final, fp)

level = 0
for i in final:
    level +=1
#    print(f"{i['author']}  {level}")


