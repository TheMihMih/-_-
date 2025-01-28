class A:
    __attr = "1234"
    def test(self):
        return self.__attr
    def __test(self):
        return self.__attr
    def _test(self):
        return self.__attr
    def test2(self):
        return self.__test()