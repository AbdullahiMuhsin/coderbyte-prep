# # Write your python code here

def solution(S):
    """
    This function takes a string S and returns the number of letters to be
    deleted so that every letter appears an even number of times.
    """
    if len(S) == 0 or len(S) > 200000:
        """
        If the string is empty or the length of the string is too long, return 0.
        """
        return 0
    
    lower_case = ''.join(filter(str.isalpha, S.lower()))
    """
    This line filters out all non-alphabetic characters and puts the string in
    lower case.
    """
    
    deleted_letters_count = 0
    count_of_letters = {}
    """
    Initialize a count of deleted letters and a count of letters.
    """
    for letter in lower_case:
        if letter in count_of_letters:
            """
            If the letter is already in the dictionary, increment the count of
            that letter.
            """
            count_of_letters[letter] += 1
        else:
            """
            If the letter is not in the dictionary, add the letter to the
            dictionary with a count of 1.
            """
            count_of_letters[letter] = 1
    print(count_of_letters)

    for count in count_of_letters.values():
        if count % 2 != 0:
            """
            If the count of a letter is not even, increment the deleted letters
            count.
            """
            deleted_letters_count += 1

    return deleted_letters_count

print(solution("acbcbba"))  
print(solution("tactcoa"))  
print(solution("axxaxa"))   
print(solution("aaaa")) 
print(solution("zzbbxxxcccd"))