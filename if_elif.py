#!/usr/bin/python\
score = raw_input("Enter score")

score = float(score)

if	score >= 1.0:

elif score >= 0.9:

	Grade = 'A'

elif	score >= 0.8:

	Grade = 'B'

elif	score >= 0.7:

	Grade = 'C'

elif	score >= 0.6:

	Grade = 'D'

elif	score < 0.6:

	Grade = 'E'

else:

	print "invalid score"


print Grade
