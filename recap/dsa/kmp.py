def strStr(haystack: str, needle: str) -> int:
    prevLPS, i = 0, 1
    lps = [0] * len(needle)

    while i < len(needle):
        if needle[i] == needle[prevLPS]:
            lps[i] = prevLPS + 1
            i += 1
            prevLPS += 1
        elif prevLPS > 0:
            prevLPS = lps[prevLPS - 1]
        else:
            i += 1

    h, n = 0, 0

    while h < len(haystack):
        if needle[n] == haystack[h]:
            n += 1
            h += 1
            if n == len(needle):
                return h - n
        elif n > 0:
            n = lps[n - 1]
        else:
            h += 1

    return -1


print(strStr("Prince Billy Graham", "Billy"))
