def foo(def_li=[]):
    def_li.append(123)
    print(def_li)


# что принтанет тут
foo()

# и тут
foo(["sobes"])

# и тут
foo()
