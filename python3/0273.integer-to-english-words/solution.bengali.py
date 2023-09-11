# Created by Bob at 2023/09/10 17:57
# leetgo: dev
# https://leetcode.com/problems/integer-to-english-words/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def numberToWords(self, num: int) -> str:
        zeroToNinetyNine: list[str] = [
            "শূন্য",
            "এক",
            "দুই",
            "তিন",
            "চার",
            "পাঁচ",
            "ছয়",
            "সাত",
            "আট",
            "নয়",
            "দশ",
            "এগার",
            "বার",
            "তের",
            "চৌদ্দ",
            "পনের",
            "ষোল",
            "সতের",
            "আঠার",
            "ঊনিশ",
            "বিশ",
            "একুশ",
            "বাইশ",
            "তেইশ",
            "চব্বিশ",
            "পঁচিশ",
            "ছাব্বিশ",
            "সাতাশ",
            "আঠাশ",
            "ঊনত্রিশ",
            "ত্রিশ",
            "একত্রিশ",
            "বত্রিশ",
            "তেত্রিশ",
            "চৌত্রিশ",
            "পঁয়ত্রিশ",
            "ছত্রিশ",
            "সাঁইত্রিশ",
            "আটত্রিশ",
            "ঊনচল্লিশ",
            "চল্লিশ",
            "একচল্লিশ",
            "বিয়াল্লিশ",
            "তেতাল্লিশ",
            "চুয়াল্লিশ",
            "পঁয়তাল্লিশ",
            "ছেচল্লিশ",
            "সাতচল্লিশ",
            "আটচল্লিশ",
            "ঊনপঞ্চাশ",
            "পঞ্চাশ",
            "একান্ন",
            "বায়ান্ন",
            "তিপ্পান্ন",
            "চুয়ান্ন",
            "পঞ্চান্ন",
            "ছাপ্পান্ন",
            "সাতান্ন",
            "আটান্ন",
            "ঊনষাট",
            "ষাট",
            "একষট্টি",
            "বাষট্টি",
            "তেষট্টি",
            "চৌষট্টি",
            "পঁয়ষট্টি",
            "ছেষট্টি",
            "সাতষট্টি",
            "আটষট্টি",
            "ঊনসত্তর",
            "সত্তর",
            "একাত্তর",
            "বাহাত্তর",
            "তিয়াত্তর",
            "চুয়াত্তর",
            "পঁচাত্তর",
            "ছিয়াত্তর",
            "সাতাত্তর",
            "আটাত্তর",
            "ঊনআশি",
            "আশি",
            "একাশি",
            "বিরাশি",
            "তিরাশি",
            "চুরাশি",
            "পঁচাশি",
            "ছিয়াশি",
            "সাতাশি",
            "আটাশি",
            "ঊননব্বই",
            "নব্বই",
            "একানব্বই",
            "বিরানব্বই",
            "তিরানব্বই",
            "চুরানব্বই",
            "পঁচানব্বই",
            "ছিয়ানব্বই",
            "সাতানব্বই",
            "আটানব্বই",
            "নিরানব্বই",
        ]

        cores = num // 10000000
        num %= 10000000

        lakhs = num // 100000
        num %= 100000

        thousands = num // 1000
        num %= 1000

        hundreds = num // 100
        num %= 100

        words: list[str] = []

        if cores > 0:
            words.append(self.numberToWords(cores) + "কোটি")

        if lakhs > 0:
            words.append(self.numberToWords(lakhs) + "লক্ষ")

        if thousands > 0:
            words.append(self.numberToWords(thousands) + "হাজার")

        if hundreds > 0:
            words.append(self.numberToWords(hundreds) + " শত")

        if num > 0:
            words.append(zeroToNinetyNine[num])
        elif len(words) == 0:
            words.append(zeroToNinetyNine[0])

        return " ".join(words)


if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().numberToWords(num)

    print("\noutput:", serialize(ans))
