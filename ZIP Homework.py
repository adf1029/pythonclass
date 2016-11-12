Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> studybuddy_1 = 'Alison McCauley, 1234 County Line Road, Skaneateles, NY 13152'
>>> studybuddy_2 = 'Dee Cater, 555 Bradford Pkwy, Syracuse, NY 13224'
>>> studybuddy_3 = 'Andrea Bianchi, 987 South St, Jamesville, NY 13078'
>>> studybuddy_4 = 'Kristen Link Logan, 264 Craig Street, Syracuse, NY 13211'
>>> studybuddy_5 = 'Nina Verity, 111 Bridge St, Solvey, NY 13209'
>>> a = studybuddy_1 [-5:]
>>> b = studybuddy_2 [-5:]
>>> c = studybuddy_3 [-5:]
>>> d = studybuddy_4 [-5:]
>>> e = studybuddy_5 [-5:]
>>> print "Our study group included people from these ZIP codes: {0}, {1}, {2}, {3}, {4}.".format(a,b,c,d,e)
Our study group included people from these ZIP codes: 13152, 13224, 13078, 13211, 13209.
>>> name_a=studybuddy_1.find(' ')
>>> name_b=studybuddy_2.find(' ')
>>> name_c=studybuddy_3.find(' ')
>>> name_d=studybuddy_4.find(' ')
>>> name_e=studybuddy_5.find(' ')
>>> print "{0} lives in {1}.".format(studybuddy_1[:name_a], a)
Alison lives in 13152.
>>> print "{0} lives in {1}.".format(studybuddy_2[:name_b], b)
Dee lives in 13224.
>>> print "{0} lives in {1}.".format(studybuddy_3[:name_c], c)
Andrea lives in 13078.
>>> print "{0} lives in {1}.".format(studybuddy_4[:name_d], d)
Kristen lives in 13211.
>>> print "{0} lives in {1}.".format(studybuddy_5[:name_e], e)
Nina lives in 13209.
>>> 
