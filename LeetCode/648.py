class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        split_sentence = sentence.split(' ')
        words_len = len(dictionary)
        sentence_len = len(split_sentence)
        
        def startsWithWord(dictionary):
            current_word = ""
            for idx, word_dic in enumerate(dictionary):
                if word.startswith(word_dic):
                    if current_word == "":
                        current_word = word_dic
                    else:
                        if len(current_word) > len(word_dic):
                            current_word = word_dic

                if idx == words_len-1:
                    if current_word == "":
                        current_word = word
                    break

            return current_word
        
        answer = ""
        for i, word in enumerate(split_sentence):
            current_word = startsWithWord(dictionary)
            answer += current_word
            if i != sentence_len-1:
                answer += " "

        return answer
