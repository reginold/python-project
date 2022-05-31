# delattr(object, name)  # objectから属性nameを削除
# getattr(object, name[, default])  # objectの属性nameの値を取得
# hasattr(object, name)  # objectに属性nameがあるかをチェック
# setattr(object, name, value)  # objectの属性nameの値をvalueに設定


class AttrTest:
    def __init__(self, name="", num=0):
        self.name = name  # setattr(self, "name", name)
        setattr(self, "num", num)

    def __repr__(self):
        result = ""
        for idx, value in vars(self).items():
            result += f"{idx}: {value}, "
        return result[0:-2]


at = AttrTest()

setattr(at, "name", "insider.net")
at.name = "build insider"
print(at.name)
# setattr(at, "newprop", 200)  # 新規の属性も作成可能（場合による）
# print(getattr(at, "newprop"))  # 出力結果： 200
# print(hasattr(at, "foo"))  # 出力結果： False
# print(getattr(at, "foo", None))  # 出力結果： None
# delattr(at, "newprop")
# print(repr(at))  # 出力結果： 'name: build insider, num: 0'
# print(getattr(at, "foo"))  # 例外： AttributeError
