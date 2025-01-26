# funny_reverse2.py


def funny2(s):
    return " ".join([i[::-1].capitalize() for i in s.split() if not "!" in i])


result = funny2("Foo bar! I said bar!")
print(result)
assert result == "Oof I Dias"

result = funny2("The qu!ck brown fox")
print(result)
assert result == "Eht Nworb Xof"

print("OK")
