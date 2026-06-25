class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 1) Normalize the original paragrah
        new_para = ''.join(c.lower() if c.isalnum() else ' ' for c in paragraph)
        banned_set = set(banned)

        # 2) Split the new paragraph into a list of words and count the frequencies of them
        words = new_para.split()
        word_count = {}
        for word in words:
            if word not in banned_set:
                word_count[word] = 1 + word_count.get(word, 0)
        
        # 3) Iterate through the word count dict to get the most frequent one
        max_count = 0
        max_word = ''

        for w, c in word_count.items():
            if c > max_count:
                max_count = c
                max_word = w
        
        return max_word
