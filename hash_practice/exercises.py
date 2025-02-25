def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """

    anagram_result = {}

    # iterate through each word in strings
    for word in strings:
        # sort anagrams into different lists
        # use sorted to rearrange each word alphabetically
        # eat, tea, ate --> aet, aet, aet
        # nat --> ant
        # bat --> abt 

        # can I use this sorted method?
        sort_anagram = ''.join(sorted(word))
        if sort_anagram in anagram_result:
            # if word is already an anagram of another word, append word to same list
            anagram_result[sort_anagram].append(word)

        else:
            # add word to new list
            # ! brackets need to be around word b/c we're adding it as a new list in hash table
            anagram_result[sort_anagram] = [word]

    return list(anagram_result.values())


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """

    #  return empty list if nums is empty
    if not nums:
        return []

    # create an empty hash table. key = number, value = occurence in string 
    # iterate through nums 
    # if number is not currently in the table, add it to the table and update value to 1
    # if number is in table, update value
    nums_table = {}
    for number in nums:
        if number in nums_table:
            nums_table[number] += 1
        else:
            nums_table[number] = 1
    

    # create an empty array 
    # iterate through hash table and append key to array based on value - in desc order
    # delete key from original hash table so we don't see it again
    nums_arr = []

    # loop through K # of times
    for n in range(k):
        max_number = 0
        frequency = 0

        for num, count in nums_table.items():
            if count > frequency:
                frequency = count
                max_number = num
        
        nums_arr.append(max_number)
        del nums_table[max_number]
    
    return nums_arr
    
def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: ?
        Space Complexity: ?
    """
    pass

