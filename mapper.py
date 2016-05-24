#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import re
import sys
from string import punctuation
from stop_words import get_stop_words

exclude = set(punctuation)
stop_words = (list(
	set(get_stop_words('arabic'))
	| set(get_stop_words('catalan'))
	| set(get_stop_words('danish'))
	| set(get_stop_words('dutch'))
	| set(get_stop_words('english'))
	| set(get_stop_words('finnish'))
	| set(get_stop_words('french'))
	| set(get_stop_words('german'))
	| set(get_stop_words('hungarian'))
	| set(get_stop_words('italian'))
	| set(get_stop_words('norwegian'))
	| set(get_stop_words('portuguese'))
	| set(get_stop_words('romanian'))
	| set(get_stop_words('russian'))
	| set(get_stop_words('spanish'))
	| set(get_stop_words('swedish'))
	| set(get_stop_words('turkish'))
	| set(get_stop_words('ukrainian'))))

key_words = ({'amd' : ['amd'], 
			'nvidia': ['nvidia'], 
			'vr': ['vr', 'virtual-reality', 'virtual' 'reality', 'virtualreality'], 
			'polaris': ['polaris'],
			'vega': ['vega'],
			'maxwell': ['maxwell'],
			'pascal': ['pascal'],
			'dp': ['dp', 'deep-learning', 'deep', 'learning', 'deeplearning'],
			'gddr5x' : ['gddr5x'],
			'hbm2' : ['hbm2'],
			'driver': ['drivers', 'driver']})

def main():
	for line in sys.stdin:

		tweet = ''
		tweet_message = ''

		word_found = ({'amd' : False, 
				'nvidia': False, 
				'vr': False, 
				'polaris': False,
				'vega': False,
				'maxwell': False,
				'pascal': False,
				'dp': False,
				'gddr5x' : False,
				'hbm2' : False,
				'driver': False})

	        try:
	            tweet = json.loads(line)
	        except ValueError as detail:
	            sys.stderr.write(detail.__str__() + "\n")
	            continue

		if 'text' in tweet:
			tweet_message = tweet['text'].encode('utf-8')
			tweet_message = tweet_message.lower()

			tweet_message = re.sub(r"(^rt |https?\://\S+)", "", tweet_message)

			tweet_message = ''.join(ch for ch in tweet_message if ch not in exclude)

			for word in [w for w in tweet_message.split() if w != stop_words]:
				for key, value in key_words.iteritems():
					if word in value:
						word_found[key] = True

			if(word_found['amd']):
				print key_words['amd'][0],
				print_categories(word_found)
			elif(word_found['nvidia']):
				print key_words['nvidia'][0],
				print_categories(word_found)
			elif found_any_category(word_found):
					print 'undefined',
					print_categories(word_found)

def found_any_category(word_found):
	found = False
	for key, value in word_found.iteritems():
		if value and (key != key_words['amd'][0] and key != key_words['nvidia'][0]):
			found = True
			break

	return found

def print_categories(word_found):
	for key, value in word_found.iteritems():
		if value and (key != key_words['amd'][0] and key != key_words['nvidia'][0]):
			print key_words[key][0],
	print ''

if __name__ == "__main__":
	main()
