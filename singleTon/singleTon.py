
# 单例模式基于模块
# singleTon.py
class Animal(object):
    def eat(self):
        print('eating...')

a=Animal()



# # 单例模式基于__new__
# class Animal(object):
#     _instance=None
#
#     def __new__(cls,*args,**kw):
#         if not cls._instance:
#             cls._instance=super(Animal,cls).__new__(cls,*args,**kw) #构建一个实例对象
#
#         return cls._instance
# # 测试
# dog=Animal()
# cat=Animal()
#
# print(id(dog))
# print(id(cat))


# # 单例模式基于装饰器
# from functools import wraps
#
# def singleton(cls):
#     instances={}
#
#     @wraps(cls)
#     def getinstance(*args,**kwargs):
#         if cls not in instances:
#             instances[cls]=cls(*args,**kwargs)
#         return instances[cls]
#
#     return getinstance()
#
# @singleton
# class Animal(object):
#     def eat(self):
#         print('eating...')

# # 单例模式基于元类
#
# class Singleton(type):
#     _instance={}
#
#     def __call__(cls,*args,**kwargs):
#         if cls not in cls._instance:
#             cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
#
#         return cls._instance[cls]
#
# class Myclass(metaclass=Singleton):
#     pass





