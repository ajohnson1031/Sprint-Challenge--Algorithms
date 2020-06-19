'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    word = list(word)
   
    def count_helper(word, count=0):
        if len(word) <= 1:
            return count
        
        if word[:1] == ['t'] and word[1:2] == ['h']:
            count += 1
            word = word[2:]
        else:
            word = word[1:]
        return count_helper(word, count)

    return count_helper(word)    