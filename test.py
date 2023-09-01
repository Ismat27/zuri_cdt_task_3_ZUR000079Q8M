from palindrome.palindrome import Palindrome

cases = [
    "1230321", "abcd5dcba 1230321 09234 0124210",
    "1230321 09234 0124210", 8888.8888, "kayak deified ontop your matter",
    "repaper deep wow peep", "noon square market rotator butter", "nothing is Steponnopets",
    "mom on another level", "deified soon deed", "1 001100 123456",
]


for case in cases:
    c = Palindrome(case)
    first_approach_palindromes = c.palindromes
    # second_approach_palindromes = c.palindromes_
    print(first_approach_palindromes)
