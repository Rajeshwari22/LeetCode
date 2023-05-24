class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomeNote_dict={}
        magazine_dict={}
        for ch in ransomNote:
            if ch not in ransomeNote_dict:
                ransomeNote_dict[ch]=1
            else:
                ransomeNote_dict[ch]=ransomeNote_dict[ch]+1
        for c in magazine:
            if c not in magazine_dict:
                magazine_dict[c]=1
            else:
                magazine_dict[c]=magazine_dict[c]+1
        for charac in ransomNote:
            if charac not in magazine_dict or magazine_dict[charac]<ransomeNote_dict[charac]:
                return False
        return True
