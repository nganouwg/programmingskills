
'''

Tag: Easy, String / Trie (A Trie is a general tree, in that each node can have any number of children. It is used to store a dictionary (list) of words that can be searched on)

-------------------------------------------------------------------------------------------

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters if it is non-empty.

'''

'''
    Solution:

    1. Determine the lenght of the shortest_word

    2. Set the prefix to an emtpy string

    3. Set and index-i and loop through each character position from ranging 0 to lenght of the shortest_word -1

    4. Assume the character at index-i of the first word is part of the common prefix
    
    5. Loop through each word at the same index, to make sure it is in fact a common prefixed character

    5. if it's not slice of that character and return the rest

    6. If all character are common part of the common prefix, return the shortest word
'''


def run(strs):

    
    shortest_word_len = len(strs[0])

    for word in strs:
        if shortest_word_len > len(word):
            shortest_word_len = len(word)

    prefix = ""
    for i in range(shortest_word_len):
        prefix += strs[0][i]
        for word in strs:
            if prefix[i] != word[i]:
                return prefix[:i]

    return prefix
        