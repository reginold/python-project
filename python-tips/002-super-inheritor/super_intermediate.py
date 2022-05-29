# Python: 你不知道的 super
# https://zhuanlan.zhihu.com/p/23625909


class Base(object):
    def __init__(self, nation="Japan", school="UEC university"):
        self.nation = nation
        self.school = school
        print("enter BaseClass")
        print("leave BaseClass")
    
    def greet_base(self, speaker, content):
        speaker_name = self.nation + "." + self.school + "." + speaker
        speaker_content = content
        res = "BaseCls " + speaker_name + " says " + speaker_content
        return res

class A(Base):
    def __init__(self, nation: str):
        self.nation = nation
        print("enter A based BaseClass")
        super(A, self).__init__()
        print("leave A based BaseClass")

    def call_init(self):
        return "Call the base init val" + self.nation

class B(Base):
    def __init__(self):
        print("enter B based BaseClass")
        super(B, self).__init__()
        print("leave B based BaseClass")

class C(A, B):
    def __init__(self):
        print("enter C based BaseClass")
        super(C, self).__init__(self)
        print("leave C based BaseClass")

    def greet_base(self, speaker, content):
        speaker_name = self.nation + "." + self.school + "." + speaker
        speaker_content = content
        res = "Cls C " + speaker_name + " says " + speaker_content
        return res

        
c = C()
a = A("China")
res = c.greet_base("lu", "Thank you for your coming...")
print(a.call_init())
print("BREAKING NEWS: " + res)
print(C.mro())

# result:
# 1. revoke the greet_base on BaseCls
# 2. add the new func in A cls


# enter C based BaseClass
# enter A based BaseClass
# enter B based BaseClass
# enter BaseClass
# leave BaseClass
# leave B based BaseClass
# leave A based BaseClass
# leave C based BaseClass
# enter A based BaseClass
# enter BaseClass
# leave BaseClass
# leave A based BaseClass
# Call the base init valJapan
# BREAKING NEWS: Cls C Japan.UEC university.lu says Thank you for your coming...
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>]

