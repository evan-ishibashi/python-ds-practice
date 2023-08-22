def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    #TODO: refactor with slicing trick
    alt_phrase = phrase.lower().replace(" ", "")

    standard = list(alt_phrase)

    reversed = list(alt_phrase)

    reversed.reverse()

    return standard == reversed
