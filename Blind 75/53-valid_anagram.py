class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = "".join(sorted(s))  # sort s
        t = "".join(sorted(t))  # sort t
        if s == t:  # check if s is equal to t
            return True  # if it's true return True
        else:
            return False  # if not return False

        # One line solution
        return Counter(s) == Counter(t)
