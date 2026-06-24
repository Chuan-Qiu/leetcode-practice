class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        class WordItem:
            def __init__(self, freq, word):
                self.freq = freq
                self.word = word
            
            def __lt__(self, other):
                if self.freq == other.freq:
                    return self.word > other.word
                return self.freq < other.freq
        
        word_count = {}
        for word in words:
            word_count[word] = 1 + word_count.get(word, 0)

        res = []
        for word in word_count.keys():
            heapq.heappush(res, WordItem(word_count[word], word))

            if len(res) > k:
                heapq.heappop(res)

        res_of_words = []
        while len(res) > 0:
            wordItem = heapq.heappop(res)
            res_of_words.append(wordItem.word)

        
        return res_of_words[::-1]