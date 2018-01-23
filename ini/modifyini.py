# coding:utf-8

import ini

fileName = "update111.ini"

iniFile = ini.IniFile()
iniFile.load(fileName)

# print type(iniFile)
# print iniFile['Version']['resver']

# for sec in iniFile:
# 	print "[",sec[0],"]\n"
# 	for k in sec[1]:
# 		print k[0], "=", k[1]
# 	print 

iniFile['Version']['bundleversion'] = "0.0.95"
iniFile['Url']['appurl'] = "www.duoyi.com"


iniFile.save()

# for i in iniFile:
# 	print 1


# print len(iniFile['MD5'])