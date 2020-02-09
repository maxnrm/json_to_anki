import json

cards_dict = {}

with open('cards.json', 'r+') as f:
    cards = json.load(f)

newcards = []
for card in cards['back']:
    card = card.replace('\n', ' ')
    newcards.append(card)

cards['back'] = newcards

for i in range(0, len(cards['front'])):
    cards_dict[cards['front'][i]] = cards['back'][i]

with open('dict.json', 'w+') as f:
    json.dump(cards_dict, f)
