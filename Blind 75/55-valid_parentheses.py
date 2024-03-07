class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Initialize an empty stack to keep track of opening brackets
        brackets = ["(", "[", "{"]
        for char in s:  # Loop through each character in the input string
            if char in brackets:  # Check if the character is an opening bracket
                stack.append(char)  # If so, push it onto the stack
            else:  # If the character is not an opening bracket, it must be a closing bracket
                if (
                    not stack
                ):  # If the stack is empty, there is no corresponding opening bracket
                    return False  # Therefore, the string is not valid
                current_char = (
                    stack.pop()
                )  # Pop the top element from the stack (last opening bracket)
                # Check if the current closing bracket matches the last opening bracket
                if current_char == "(":
                    if char != ")":
                        return False
                if current_char == "[":
                    if char != "]":
                        return False
                if current_char == "{":
                    if char != "}":
                        return False

        if (
            stack
        ):  # If the stack is not empty, some opening brackets didn't have a matching closing bracket
            return False  # Therefore, the string is not valid

        return True  # If the stack is empty, all brackets were properly matched
