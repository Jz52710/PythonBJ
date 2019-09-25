# class Person:
#     """
#         `我你你打论文集按时付款我饿akmf/ask的麻烦文件热空气二lkjrl/wm阿斯蒂芬
#     """
    # classname = "person"
    # @classmethod
    # def fn(cls):
    #     print('hello')
    #     print(cls.classname)
    # @staticmethod
    # def fnn():
    #     print('牛逼')
    #     Person.fn()
    #     print(Person.classname)

# Person.fn()
# Person.fnn()
# print(Person.__doc__)
# class Person:
#     def __new__(cls, *args, **kwargs):
#         self = super().__new__(cls)
#         self.age = '12'
#         self.sex = '1232131'
#         return  self
#     def __init__(self):
#         self.name = "xxiaob"
# print(dir(Person()))
class Person:
    def __init__(self):
        self.__username = ''
    def say(self):
        print('xxx')
    @property
    def nm(self):
        return self.__username
    @nm.setter
    def nm(self,value):
        lenght = len(value)
        if lenght < 5 and lenght >1:
            self.__username = value
        else:
            print("验证失败")
p = Person()
# print(dir(p))
# p.say()
p.nm = '我你是的的是的'
print(p.nm)
p.nm = '贾争'
print(p.nm)