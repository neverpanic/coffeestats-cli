#!/usr/bin/env python

import sys
import json

result = json.load(sys.stdin)

success = result['success']
if not success:
	if 'error' in result:
		for error in result['error']:
			print >> sys.stderr, "Error: %s" % error
if 'warning' in result:
	for warning in result['warning']:
		print >> sys.stderr, "Warning: %s" % warning
if success:
	if sys.argv[1] == "coffee":
		print "It's done! Enjoy your delicious coffee!"
	elif sys.argv[1] == "mate":
		print "It's done! Aah! A refreshing bottle of mate!"
	else:
		print "It's done!"
else:
	print >> sys.stderr, "Submission failed."
