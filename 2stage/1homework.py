import random
# word = "python"
# dict_1 = {}
#
# for i in word:
# 	dict_1 = random.randint(1,20)
#
# print(dict_1)


class NewDict:
	def __init__(self,string_):
		self.dict_1 = {}

		for key in string_:
			self.dict_1[key] = random.randint(1,20)


	def rem_dub(self):
		d = {}

		for i in self.dict_1:
			if self.dict_1[i] not in d.values():
				d[i] = self.dict_1[i]

		self.dict_1[i] = d


	def max_3(self):

		list_1 = (self.dict_1.values())
		list_1.sort(reverse = True)

		return list_1[:3]


dict_new = NewDic("python")

print(dict_new.dict_1)
