class Solution:
    def smallestSubsequence(self, s):
        stack = []

        # Traverse every character
        for i in range(len(s)):
            ch = s[i]

            # Skip if already in stack
            if ch in stack:
                continue

            # Remove bigger characters if they come again later
            while stack:
                top = stack[-1]

                if top > ch and top in s[i + 1:]:
                    stack.pop()
                else:
                    break

            # Add current character
            stack.append(ch)

        return "".join(stack)