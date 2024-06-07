class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root_map = {word: True for word in dictionary}
        words = sentence.split(" ")
        for i in range(len(words)):
            for j in range(1, len(words[i])):
                if words[i][:j] in root_map:
                    words[i] = words[i][:j]
                    break
        return " ".join(words)
