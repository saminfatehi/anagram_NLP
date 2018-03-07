# anagram_NLP

this is a code for a NLP homework that find all meaningful anagram of a word. 
for find them we can find all of anagrams and for each one search it in list of words (all meaningful words in persion. we have a CSV file with more than 20000 word.)(O(n^2))
but for achive O(n) in this problem we can sort the word. then for each word in dictionary, we should sort it and if this new string and sorted first string is same, in fact that main word in dictionary is an anagram for our main word. 
+ implementation of algorithem in order n^2 is comented at the end of code.
++ there is 5 lists in CSV file. this prorogram checked words of Moin`s dictionary. for check the other ones you can change the index in line 9. 
