class Solution:
  def backspaceCompare(self, S, T):
    string1 = []
    string2 = []
    for c in S:
      if c == "#" and len(string1) > 0:
        string1.pop()
      elif c != "#":
        string1.append(c)
    for c in T:
      if c == "#" and len(string2) > 0:
        string2.pop()
      elif c != "#":
        string2.append(c)
    return string1 == string2

# 双指针，从后面开始遍历
class Solution:
    def backspaceCompare(self, S, T):
        i, j = len(S) - 1, len(T) - 1
        skipS = skipT = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == "#":
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if T[j] == "#":
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1
        
        return True
