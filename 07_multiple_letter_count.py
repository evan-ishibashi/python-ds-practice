def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    letter_counter ={}

    for char in phrase:
        if letter_counter.get(char):
            letter_counter[char] += 1
        else:
            letter_counter[char] = 1

    return letter_counter