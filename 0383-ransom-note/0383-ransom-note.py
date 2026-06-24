class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        mag = {}

        if not ransomNote:
            return True

        if not magazine and ransomNote:
            return False

        for m in magazine:
            if m not in mag:
                mag[m] = 1
            else:
                mag[m] += 1    

        for r in ransomNote:
            if r in mag and mag[r] >= 1 :
                mag[r] -= 1
                continue
            else:
                return False
        return True                
        