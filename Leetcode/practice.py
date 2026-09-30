class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <right:
            if not s[left].isalnum():
                left = left +1
            elif not s[right].isalnum():
                right = right -1
            elif(s[left].lower() != s[right].lower()):
                return False
            else:
                left = left +1
                right = right -1
            
        return True


# Take input from user
s = input("Enter a string: ")

# Create object
solution = Solution()

# Call the function
result = solution.isPalindrome(s)

# Print result
print("Is Palindrome:", result)