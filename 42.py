def word_lengths(s):
    return [len(i) for i in s.split()]


result_1 = word_lengths(
    "Contrary to popular belief Lorem Ipsum is not simply random text"
)
print("Result 1:", result_1)
assert result_1 == [8, 2, 7, 6, 5, 5, 2, 3, 6, 6, 4]


result_2 = word_lengths("john paul george ringo")
print("Result 2:", result_2)
assert result_2 == [4, 4, 6, 5]

print("OK")


def max_word_length(s):
    return max([len(i) for i in s.split()])


result = max_word_length(
    "Contrary to popular belief Lorem Ipsum is not simply random text"
)
print("Result:", result)
assert result == 8
print("OK")
