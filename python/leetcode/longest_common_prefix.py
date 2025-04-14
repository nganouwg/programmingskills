
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

    2. Set an index-i ranging from 0 to the size of the shorted_word - 1 to compare characters by positipn

    3. set the cur_letter to an empty string, which is used to hold prefix character at index-i.

    4. Loop through each word at the same index

    5. if the cur_letter is empty, this means we are at a new character position, 
       so set the cur_letter to the first word's character at index-i 

    6. Compare the cur_letter to the same position characters for subsequent words. 
    
    7. If a mismatch is found set end_of_prefix to true, 
       which mean we no longer found characters for the common prefix and we can break out of the loops

    8. If no mismatch is found include the cur_letter to the prefix

    9. Display the common prefix
'''



def run(strs):

    prefixes = ""
    end_of_prefix = False
    prev_letter = ""
    shortest_word_len = len(strs[0])

    for word in strs:
        if shortest_word_len > len(word):
            shortest_word_len = len(word)

    i = 0
    for i in range(shortest_word_len):
        prev_letter = ""
        for word in strs:
            if prev_letter == "":
                prev_letter = word[i]
            else:
                if prev_letter != word[i]:
                    end_of_prefix = True
                    break

        if end_of_prefix == False:
            prefixes = prefixes + prev_letter
        else:
            break

        i += 1

    print(prefixes)
        