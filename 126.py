def automaton_126(s):
    # -------- YOUR CODE HERE ---------
    res=""
    lengh=len(s)
    for i in range(len(s)):
        three=""
        if i==0:
            three+=s[lengh-1]
        else:
            three+=s[i-1]
        three+=s[i]
        if i==lengh-1:
            three+=s[0]
        else:
            three+=s[i+1]

        if three=="..." or three=="XXX":
            res+="."
        else:
            res+="X"
    return  res
    # ---------------------------------


assert automaton_126("...") == "..."
assert automaton_126("XXX") == "..."
assert automaton_126("...X..X...") == "..XXXXXX.."
assert automaton_126(".....X.....") == "....XXX...."
assert automaton_126("X..........") == "XX........X"
assert automaton_126("..........X") == "X........XX"
assert automaton_126(".XX.X.X..X.X.X") == "XXXXXXXXXXXXXX"
assert automaton_126("...X..X..") == "..XXXXXX."
print("Tests OK")