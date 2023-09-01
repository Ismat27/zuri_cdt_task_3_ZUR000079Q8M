import sys


class Palindrome:

    def __init__(self, text) -> None:
        if not (type(text) == str or type(text) == int or type(text) == float):
            print("invalid input, program terminated")
            sys.exit(1)
        self.text = str(text).lower()

    def _to_list(self):
        return self.text.split(" ")

    # first approach
    def _is_palindrome(self, word: str):
        length = len(word)
        middle = length // 2
        if length < 1:
            return False
        for i in range(0, length):
            # if we are at the middle, we must have looped through both sides,
            # hence the word is a palindrome
            if i == middle:
                return True
            # compare characters at opposite ends e.g first and last characters
            if not (word[i] == word[length - 1 - i]):
                return False

    # second approach
    def _is_palindrome_(self, word: str):
        length = len(word)
        if length < 1:
            return False
        middle = length // 2
        is_even = length % 2 == 0
        if is_even:
            # check if the two middle items are equal
            if not (word[middle - 1] == word[middle]):
                return False
        first_half = word[0:middle]
        second_half = word[middle:]
        if not is_even:
            second_half = word[middle + 1:]
        # split into two, compare the first half to the reversed second half
        return first_half == second_half[::-1]

    # using first approach
    @property
    def palindromes(self):
        items = self._to_list()
        active = [word for word in items if self._is_palindrome(word)]
        return " ".join(active)

    # using second approach
    @property
    def palindromes_(self):
        items = self._to_list()
        active = [word for word in items if self._is_palindrome_(word)]
        return " ".join(active)
