import random

from settings import my_settings


class Words(object):
    def __init__(self):
        self.path = my_settings["input_dir"]
        self.fp = None
        self.word_list = []
        self.temp_word_list = []
        self.init_fp()

    def init_fp(self):
        self.fp = open(self.path, 'a+')
        self.fp.seek(0)
        self.word_list = []
        for line in self.fp:
            line = line.strip()
            self.word_list.append(list(line.split('\t')))

    def filter(self, type):
        if 'A' not in type:
            self.temp_word_list = self.word_list
            new_word_list = []
            for line in self.word_list:
                if line[2] in type:
                    new_word_list.append(line)
            self.word_list = new_word_list
            print(self.word_list)

    def get_words(self, k, sort_method, exact_phrase, is_reversed):
        now_list = sort_method(self.word_list)[:k]
        if exact_phrase:
            words = []
            phrases = []
            for word in now_list:
                if ' ' in word:
                    phrases.append(word)
                else:
                    words.append(word)
            if is_reversed:
                words = words[::-1]
                phrases = phrases[::-1]
                is_reversed = False
            now_list = words + phrases
        if is_reversed:
            now_list = now_list[::-1]
        return now_list

    def save_file(self):
        self.fp.close()


class SortMethod(object):
    def select(self):
        choice = my_settings["sort_method"]
        if choice == "frequency":
            method = self.sort_by_frequency
        elif choice == "date":
            method = self.sort_by_date
        elif choice == "dictionary order":
            method = self.sort_by_dictionary_order
        else:
            method = self.random_sort
        return method

    def sort_by_date(self, word_list):
        word_list.sort(key=lambda x: x[1])
        word_list = [x[0] for x in word_list]
        res = list(set(word_list))
        res.sort(key=word_list.index)
        return res

    def sort_by_frequency(self, word_list):
        word_to_frequency = {}
        frequency_to_word = {}
        word_list = [x[0] for x in word_list]
        for word in word_list:
            if word not in word_to_frequency:
                word_to_frequency[word] = 1
            else:
                word_to_frequency[word] += 1
        for k, v in word_to_frequency.items():
            if v not in frequency_to_word:
                frequency_to_word[v] = [k]
            else:
                frequency_to_word[v].append(k)
        keys = list(frequency_to_word.keys())
        keys.sort(reverse=True)
        res = []
        for key in keys:
            for word in frequency_to_word[key]:
                res.append(word + '\t' + str(key))
        return res

    def sort_by_dictionary_order(self, word_list):
        word_list.sort(key=lambda x: x[0])
        word_list = [x[0] for x in word_list]
        res = list(set(word_list))
        res.sort(key=word_list.index)
        return res

    def random_sort(self, word_list):
        word_list = [x[0] for x in word_list]
        res = list(set(word_list))
        random.shuffle(res)
        return res
    

if __name__ == '__main__':
    wordRecorder = Words()
    method = SortMethod()

    wordRecorder.filter(my_settings["words_type"])

    sort_method = method.select()
    now_word = wordRecorder.get_words(my_settings["words_number"], sort_method, my_settings["exact_phrase"], my_settings["is_reversed"])
    with open(my_settings["output_dir"], 'w') as fp:
        for line in now_word:
            fp.write(line + '\n')
            print(line)

    wordRecorder.save_file()
