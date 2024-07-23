if s == "": return True
for i in range(len(s)):
    if s[i] in t:
        t = t[t.index(s[i]) + 1:]
    else:
        return False

return len(s) == (i + 1)