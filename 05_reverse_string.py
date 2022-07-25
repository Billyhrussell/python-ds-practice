def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    letters = list(phrase)
    letters_reverse = letters[::-1]
    return "".join(letters_reverse)