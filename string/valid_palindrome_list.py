def isPalindrome(self, s: str) -> bool:
  strs = []
  for char in s:
    # check if char is alphanumeric string
    if char.isalnum():
      strs.append(char.lower())

  while len(strs) > 1:
    if strs.pop(0) != strs.pop():
      return False
  
  return True