def is_palindrom(word):
    new_word = ''
    for x in word:
        new_word = x + new_word
    if new_word == word:
        result = 'palindrom'
    else:
        result = 'not palindrom'
    return result
w = 'abba'
assert is_palindrom(w) == 'palindrom', 'not palindrom word'