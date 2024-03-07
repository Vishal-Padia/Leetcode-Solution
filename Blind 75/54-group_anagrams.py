class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}  # Initialize an empty dictionary to hold lists of anagrams

        for word in strs:  # Loop through each word in the input list 'strs'
            sortedWord = "".join(
                sorted(word)
            )  # Sort the letters of the word alphabetically and join them back into a string

            if (
                sortedWord not in dictionary
            ):  # Check if the sorted version of the word is not already a key in the dictionary
                dictionary[sortedWord] = [
                    word
                ]  # If not, add it as a new key with the original word as its value in a list
            else:
                dictionary[sortedWord].append(
                    word
                )  # If it is, append the current word to the list of anagrams for this sorted key

        return [
            dictionary[i] for i in dictionary
        ]  # Return a list of all values in the dictionary, which are lists of anagrams
