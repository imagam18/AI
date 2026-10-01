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



def mincoin(coin,amount):
    n = len(coin)
    coin.sort()
    res = 0
    
    for i in range(len(coin)-1,-1,-1):
        if amount >= coin[i]:
            
            cnt = amount // coin[i]
            
            res += cnt
            
            amount -= cnt * coin[i]
        
        if amount == 0:
            break
    return res 

if __name__ == "__main__":
    coin = [5, 2, 10, 1]
    amount = 40

    print(mincoin(coin, amount))
            