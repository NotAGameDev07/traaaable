import json
import random

print('INIT: jokes library and functions')

with open('jokes.json', 'r') as f:
	jokes = json.load(f)

def random_joke():
	return random.choice(jokes)