'''
Reverse Words

Given a string s, reverse the string without reversing its individual words. Words are separated by spaces.

Note: The string may contain leading or trailing spaces, or multiple spaces between two words. The returned string should only have a single space separating the words, and no extra spaces should be included.

Examples :

Input: s = " i like this program very much "
Output: "much very program this like i"
Explanation: After removing extra spaces and reversing the whole string (not individual words), the input string becomes "much very program this like i". 
Input: s = " pqr mno "
Output: "mno pqr"
Explanation: After removing extra spaces and reversing the whole string, the input string becomes "mno pqr". 
Input: s = " a "
Output: "a"
Explanation: The input string contains only one word with extra spaces around it. After removing the extra spaces, the output is "a".Constraints:

Constraints:
1 <= s.size() <= 106
String s contains only lowercase English alphabets and spaces.

'''

def reverse_words():
    phrase = " i like this program very much "
    print(phrase)

    words = phrase.split(' ')
    print(words)

    rev_phrase = ' '.join(reversed(words))
    print(rev_phrase)


'''
Here we'll talk about the novel and perhaps tantalizing concept of slicing. Slicing is the process through which you can extract some continuous part of a string. For example: string is "python", let's use slicing in this. Slicing can be done as:

a. string[0:2] = py (Slicing till index 1)
b. string[0:] = python (Slicing till last index)
c. string[0:4] = pyth (Slicing till index 3)
d. string[0:-2] = pyth (Slicing till index -3).
Note: -1 indexing starts from last of any string.

Now, lets look into this through a question. Given a string of braces named bound_by, and a string named tag_name. The task is to print a new string such that tag_name is in the middle of bound_by.

Example 1:

Input: 
bound_by = [[]], tag_name = tag
Output:
[[tag]]
Example 2:

Input: 
bound_by = <>, tag_name = body
Output:
<body>
Your Task:
Your task is to complete the function join_middle() which should return the modified string.

Constraints:
1 <= |tag_name| <= 103
'''

def join_middle():
    bound_by = '[[]]'
    tag_name = 'tag'
    b_size = len(bound_by)
    mid = b_size//2

    tag = bound_by[0:mid] + tag_name + bound_by[mid:b_size]
    print(tag)


'''
    Whooaah! Your are now familiar with String slicing. Let's have one more question to make it crystal clear for you with some conditional statements.

    Given two strings a and b. The task is to make a new string where the string with longer length should be in between and the one with shorter length should be outside on front and end. New string should be like shorter+longer+shorter.

    Note: It is guranteed that no two string are of same length.

    Example:

        Input: 
        a = Hi, b = There
        Output: 
        HiThereHi
        Explanation: 
        After joining short+long+short strings, 
        we have new string as "HiThereHi".
        Constraints:
        1 <= |a, b| <= 103
'''

def repeat_the_string():
    a = 'Hi' 
    b = 'There'

    print(a+b+a if len(a) < len(b) else b+a+b)


'''
Given a string s which may contain lowercase and uppercase characters. The task is to remove all duplicate characters from the string and find the resultant string. The order of remaining characters in the output should be same as in the original string.

Example 1:

Input: s = "geEksforGEeks"
Output: "geEksforG"
Explanation: After removing duplicate characters such as E, e, k, s, we have string as "geEksforG".
Example 2:

Input: s = "HaPpyNewYear"
Output: "HaPpyNewYr"
Explanation: After removing duplicate characters such as e, a, we have string as "HaPpyNewYr".
Constraints:
1 ≤ N ≤ 106
String contains uppercase and lowercase english letters.
'''

def remove_dups_from_string():

    s = 'geEksforGEeks'
    char_set = []

    for c in s:
        if c not in char_set:
            char_set.append(c)

    print(''.join(char_set))

if __name__ == "__main__":

    #reverse_words()
    #join_middle()
    #repeat_the_string()
    remove_dups_from_string()

