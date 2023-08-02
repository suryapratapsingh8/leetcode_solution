class Solution:
    def reverseWords(self, s: str) -> str:
        word = ""
        words = []
		
		#making words list without space
        for a in s:
            if a != " ":
                word += a
            else:
                if word != "":
                    words.append(word)
                    word = ""
        if word != "":
            words.append(word)
        new_word = ""
		
		#reversing
        for w in words:
            new_word = " " + w + new_word
        return new_word[1:]