class asdf:
    pass


setattr(asdf, 'var', 1234)
print(asdf.var)

a =asdf()
setattr(a, 'a', 1)
print(a.a)
