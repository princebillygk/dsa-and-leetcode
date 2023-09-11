# Created by Bob at 2023/09/10 17:57
# leetgo: dev
# https://leetcode.com/problems/integer-to-english-words/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def numberToWords(self, num: int) -> str:
        zeroToNine = [
            "Zero",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
        ]

        tenToNineteen = [
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]

        twentyToNinety = [
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]

        billions = num // 1000000000
        num %= 1000000000

        millions = num // 1000000
        num %= 1000000

        thousands = num // 1000
        num %= 1000

        hundreds = num // 100
        num %= 100

        tens = num // 10
        num %= 10

        words: list[str] = []

        if billions > 0:
            words.append(self.numberToWords(billions) + " Billion")

        if millions > 0:
            words.append(self.numberToWords(millions) + " Million")

        if thousands > 0:
            words.append(self.numberToWords(thousands) + " Thousand")

        if hundreds > 0:
            words.append(self.numberToWords(hundreds) + " Hundred")

        if tens > 1:
            words.append(twentyToNinety[tens - 2])
            if num > 0:
                words.append(zeroToNine[num])
        elif tens == 1:
            words.append(tenToNineteen[num])
        elif num > 0:
            words.append(zeroToNine[num])
        elif len(words) == 0:
            words.append(zeroToNine[num])

        return " ".join(words)


if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().numberToWords(num)

    print("\noutput:", serialize(ans))
