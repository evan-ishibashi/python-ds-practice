def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    upper_swap = to_swap.upper()
    lower_swap = to_swap.lower()

    swapped_phrase = []

    for char in phrase:
        if char == upper_swap:
            swapped_phrase.append(lower_swap)
        elif char == lower_swap:
            swapped_phrase.append(upper_swap)
        else:
            swapped_phrase.append(char)

    return ''.join(swapped_phrase)
