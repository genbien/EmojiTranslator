#!/usr/bin/python
# -*- coding: UTF-8 -*-

# positive_emojis = {u'😀' : ['happy', 'smile'], u'😂' : ['lol', 'laugh', 'cry']}
positive_emojis = {'happy':u'😀','smile':u'😀','lol':u'😂','laugh':u'😂','cry':u'😂'}

phrase = "lol ur so funny cry"
phrase = phrase.split()


ret = []

for word in phrase:
	if (word in positive_emojis.keys()):
		ret.append(positive_emojis[word])
	else:
		ret.append(word)
print " ".join(ret)