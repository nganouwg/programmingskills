
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

#HINT: Count the number of time each letter appears for a given 


def run(strs):

    prefixes = ""
    end_of_prefix = False
    prev_letter = ""
    shortest_word_len = len(strs[0])

    for word in strs:
        if shortest_word_len > len(word):
            shortest_word_len = len(word)

    i = 0
    while(i < shortest_word_len):
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
        