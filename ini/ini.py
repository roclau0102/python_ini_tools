# coding=utf-8

import os

class IniFile():
	"""ini file"""
	def __init__(self):
		self.sections = {}
		self.keys = []
		self.index = 0

	def load(self, sPath):
		self.path = sPath
		fileStream = open(sPath, 'rb')
		lines = fileStream.readlines()
		fileStream.close()
		for line in lines:
			# print line
			trimStart = line.strip()
			if len(trimStart):
				if trimStart[0] == '[':
					secEnd = trimStart.index(']')
					if secEnd > 0:
						sectionName = trimStart[1:secEnd].strip()
						# print sectionName
						section = IniSection()
						self.keys.append(sectionName)
						self.sections[sectionName] = section
				elif section != None and trimStart[0] != ';':
					self._loadValue(line, section)


	def save(self, sPath=None):
		if not sPath:
			sPath = self.path
		fileStream = open(sPath, 'wb+')
		for key in self.keys:
			fileStream.write("[%s]\n" % key)
			for k, vals in self.sections[key]:
				# keys = vals.keys()
				line = "%s=%s\n" % (k, vals)
				fileStream.write(line)
			fileStream.write('\n')
		fileStream.close()

	def _loadValue(self, sLine, cSection):
		assignIndex = sLine.index('=')
		if assignIndex <= 0:
			return
		key = sLine[0:assignIndex].strip()
		value = sLine[assignIndex+1:].strip()
		cSection[key] = value


	def __setitem__(self, k, v):
		self.keys.append(k)
		print k, self.keys
		self.sections[k] = v


	def __getitem__(self, k):
		return self.sections[k]

	def __len__(self):
		return len(self.sections)

	def __iter__(self):
		return self;

	def next(self):
		if self.index >= len(self.sections):
			raise StopIteration
		key = self.keys[self.index]
		self.index += 1
		return key, self.sections[key]

class IniSection():
	"""ini section"""
	def __init__(self):
		self.values = {}
		self.keys = []
		self.index = 0

	def __setitem__(self, k ,v ):
		self.keys.append(k)
		self.values[k] = v

	def __getitem__(self, k):
		return self.values[k]

	def __iter__(self):
		return self

	def next(self):
		if self.index >= len(self.values):
			raise StopIteration
		key = self.keys[self.index]
		self.index += 1
		return key, self.values[key]

	def __len__(self):
		return len(self.values)
