# circle.py

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """The radius property."""
        print("Get radius")
        return self._radius

    @radius.setter
    def radius(self, value):
        print("Set radius")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("Delete radius")
        del self._radius

circle = Circle(5.0)
print(circle.radius)
circle.radius = 100.0
print(circle.radius)

del circle.radius
print(circle.radius)

# help(circle)

# 装饰器@property必须装饰getter 方法。
# 文档字符串必须放在getter 方法中。
# setter 和 deleter 方法必须分别用 getter 方法的名称加和.setter装饰.deleter。