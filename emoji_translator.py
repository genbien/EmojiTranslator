#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

positive_emojis = {'happy':u'😀','smile':u'😀','lol':u'😂','laugh':u'😂','cry':u'😂'}

if (len(sys.argv) != 2):
	print "Usage: emoji_translator.py \"string\""
	sys.exit()
phrase = sys.argv[1]
phrase = phrase.split()
translated = []
for word in phrase:
	if (word in positive_emojis.keys()):
		translated.append(positive_emojis[word])
	else:
		translated.append(word)
print " ".join(translated)