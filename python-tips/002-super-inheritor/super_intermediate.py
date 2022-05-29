# Python: 你不知道的 super
# https://zhuanlan.zhihu.com/p/23625909


class Base(object):
    def __init__(self, nation="Japan", school="UEC university"):
        self.nation = nation
        self.school = school
        print("enter BaseClass")
        print("leave BaseClass")
    
    def greet_base(self, speaker, content):
        speaker_name = self.nation + "." + self.school + "." +  speaker
        speaker_content = content
        res = speaker_name + " says " + speaker_content
        return res

class A(Base):
    def __init__(self):
        print("enter A based BaseClass")
        super(A, self).__init__()
        print("leave A based BaseClass")

class B(Base):
    def __init__(self):
        print("enter B based BaseClass")
        super(B, self).__init__()
        print("leave B based BaseClass")

class C(A, B):
    def __init__(self):
        print("enter C based BaseClass")
        super(C, self).__init__()
        print("leave C based BaseClass")

        
c = C()
res = c.greet_base("lu", "Thank you for your coming...")
print(res)
print(C.mro())