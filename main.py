import random


class Words(object):
    def __init__(self, path="words.txt"):
        self.path = path
        self.fp = None
        self.word_list = []
        self.temp_word_list = []
        self.init_fp()

    def init_fp(self):
        self.fp = open(self.path, 'a+')
        self.fp.seek(0)
        self.word_list = []
        for line in self.fp:
            self.word_list.append(list(line.split(' ')))

    @staticmethod
    def print_message():
        print("What do you want to do?")
        print("1.Record your words.")
        print("2.Get K words.")
        print("3.Exit.")

    def restore(self):
        self.word_list = self.temp_word_list

    def filter(self, type):
        if type != 'A':
            type += '\n'
            self.temp_word_list = self.word_list
            new_word_list = []
            for line in self.word_list:
                if line[2] == type:
                    new_word_list.append(line)
            self.word_list = new_word_list
            print(self.word_list)

    def get_words(self, k, sort_method):
        print(self.word_list)
        now_list = sort_method(self.word_list)[:k]
        print(now_list)
        return now_list

    def write_words(self, word_list):
        self.fp.writelines(word_list)
        self.save_file()
        self.init_fp()

    def save_file(self):
        self.fp.close()


class SortMethod(object):
    def select(self):
        print("1.Sort by frequency.")
        print("2.Sort by date.")
        print("3.Sort by dictionary order.")
        print("4.Random.")
        choice = input()
        if choice == '1':
            method = self.sort_by_frequency
        elif choice == '2':
            method = self.sort_by_date
        elif choice == '3':
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
            res.extend(frequency_to_word[key])
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
    shut_down_signal = False
    while not shut_down_signal:
        wordRecorder.print_message()
        select = input()
        if select == '1':
            print("Each line combines with the word itself, the date and the tag of it.")
            print("\"#\" means the end of your input.")
            word = input("Now input your words!\n")
            words = []
            while word != '#':
                word += '\n'
                while len(word.split(' ')) != 3:
                    word = input("Input error! Check it and input again!")
                words.append(word)
                word = input()
            print(words)
            wordRecorder.write_words(words)
        elif select == '2':
            print("What type of words do you want to get? ")
            word_type = input("L for listening, S for speaking, W for writing, R for reading and A for all: ")
            wordRecorder.filter(word_type)
            k = int(input("Input the number of the words you want to get: "))
            sort_method = method.select()
            now_word = wordRecorder.get_words(k, sort_method)
            with open("result.txt", 'w') as fp:
                for line in now_word:
                    print(line)
                    fp.write(line + '\n')
            if word_type != 'A':
                wordRecorder.restore()
        elif select == '3':
            shut_down_signal = True
        else:
            print("Input error! You can only input 1,2 or 3!")
    wordRecorder.save_file()
