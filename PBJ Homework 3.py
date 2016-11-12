Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> bread = 7
>>> pb = 4
>>> jelly = 4
>>> if (pb >= 1) and (jelly >= 1) and (bread >=2):
	sandwiches = bread/2
	if (pb <= sandwiches):
		sandwiches = pb
	if (jelly <= sandwiches):
		sandwiches = jelly
	print "you can make {0} sandwiches".format(sandwiches)
	if bread % 2 == 1:
		print "you can make an open faced sandwich"

		
you can make 3 sandwiches
you can make an open faced sandwich
>>> 
