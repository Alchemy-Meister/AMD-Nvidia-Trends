#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import re
import sys
from string import punctuation
from stop_words import get_stop_words

exclude = set(punctuation)
stop_words = (list(set(['rt', 'fav'])
	| set(get_stop_words('arabic'))
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

for line in sys.stdin:

	tweet = ''
	tweet_message = ''

        try:
            tweet = json.loads(line)
        except ValueError as detail:
            sys.stderr.write(detail.__str__() + "\n")
            continue

	if 'text' in tweet:
		tweet_message = tweet['text'].encode('utf-8')
		tweet_message = tweet_message.lower()

		print tweet_message

		tweet_message = re.sub(r"(^rt |https?\://\S+)", "", tweet_message)

		tweet_message = ''.join(ch for ch in tweet_message if ch not in exclude)

		print tweet_message

		for word in [w for w in tweet_message.split() if w not in stop_words]:
			print '\t ' + word