"""Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases."""
def isPalindrome(self, s: str) -> bool:
        s = [e.lower() for e in s if e.isalnum()]
        return s == s[::-1]
