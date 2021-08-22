Combine two strings according to the below rule:

Input Strings a and b: For every character in string a swap the casing of every occurrence of the same character in string b. Then repeat the same casing swap in string a with reference from characters in string b.

Example:

Input: "abc", "cde"      		--> Output: "abCCde" 
Input: "ab", "aba"       		--> Output: "aBABA"
Input: "abab", "bababa"  		--> Output: "ABABbababa"
Input: "abcabcabc", "cdhfcbda"	--> Output: "ABcABcABcCdhfCBdA"