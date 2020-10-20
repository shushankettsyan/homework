# class Store:
#     # def presentation(self):
#     #     return "This store sells equipments"
#
#     def __init__(self, text):
#         self.text = text
#     def presentation(self):
#         return self.text
#
#
#
# class NewStore(Store):
#     def __init__(self, text, type_):
#         super().__init__(text)
#         self.type_ = type_
#
#     def presentation(self):
#         presentation = F"{super().presentation()} and our type {self.type_}"
#         return presentation
#
# little_store = NewStore("Hi we're Saturn we sell phones", "phone-seller")
#
# class ClothesStore:
#     def presentation(self, text):
#         return "this store sells clothes",
#
# class Shoes(ClothesStore):
#     def presentation(self):
#         b = super().presentation()
#         return b, "this shoe is for kids"
#
#         if "not" in b:
#             b += ")))))"
#
#         return b
#
# shoe_1 = Shoes()
#
# print(shoe_1.presentation())

# a = Store()
# b = ClothesStore()
#
# #2 arjeq return anelu hamar
# k,p = b.presentation()
# c = b.presentation()
# print("this store sells clothes", k, type(k))
# print("tuple", c, type(c))
# print(a.presentation())
# print(b.presentation())




class Store:
    def __init__(self, text):
        self.__text = text
    def presentation(self):
        return self.text
    def set_text (self,new_text):
        try:
            if new_text.isalpha():
                self.text = new_text
        except:
            print("wrong value")

new_store = Store("Saturn")

print(new_store.text)
new_store.set_text("asd")
print(new_store.text)
new_store.text = 5
print(new_store.text)

# d = 0
# def a(b):
#     return b
