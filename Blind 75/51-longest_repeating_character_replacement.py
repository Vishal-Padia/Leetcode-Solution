class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0  # Initialize starting pointer to 0
        max_len = 0  # Initialize max_len to 0 for storing the maximum length
        max_count = 0  # Initialize max_count to 0 for storing the maximum count
        freq = {}  # Initialize a hashmap for storing the frequency

        for end in range(len(s)):  # run a loop through the length of string
            freq[s[end]] = (
                freq.get(s[end], 0) + 1
            )  # Increase the frequency count of the character at the current 'end' position of the string

            max_count = max(
                max_count, freq[s[end]]
            )  # update the max_count with max of itself and the frequency of current character

            if (
                end - start + 1
            ) - max_count > k:  # check if the current window size minus the max_count exceeds the k
                freq[
                    s[start]
                ] -= 1  # if it is, then decrement frequency of character at 'start' position
                start += 1  # increment the start by 1

            max_len = max(
                max_len, end - start + 1
            )  # update the max_len with max of itselt and current window(end-start+1)

        return max_len
