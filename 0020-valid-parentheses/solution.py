class Solution(object):
  def isValid(self, s:str) -> bool:
    mapping = {")":"(", "}":"{", "]":"["}
    stack = []
    for char in s:
      if char in mapping:
        if stack and stack[-1] == mapping[char]:
          stack.pop()
        else:
          return False
      else:
        stack.append(char)
    if not stack:
      return True
    return False
