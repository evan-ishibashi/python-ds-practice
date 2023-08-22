def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    #some way to do this with a slice?
    reversed_string = phrase[::-1]
    my_word = ''
    counter = len(phrase) - 1
    while (counter >= 0):
        my_word+= phrase[counter]
        counter-= 1
    return my_word

