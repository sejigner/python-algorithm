import re
def isPalindrome(self, s: str) -> bool:
  s = s.lower()
  # filter through regex
  s = re.sub('[^a-z0-9]','',s)

  return s == s[::-1]