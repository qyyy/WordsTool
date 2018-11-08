## Introduction
This tool aims at helping people to memorize or collect English words more efficiently.
I use it to prepare for my TOEFL Exam. You can also use it for your other English exams.
The tool has the following functions:
- Record a new word.
- Sort the words according to frequency, date or dictionary order. Also just random.
- Produce an output file with the words in the order you want, you can use the output to repeat these words.
### How to use it
#### For interactive mode
1. Clone the interactive mode code: `git clone -b interactive https://github.com/qyyy/WordsTool.git`.
2. Run the tool: `python3 main.py -i words.txt -o result.txt`. The "-i" means the path of input file with your words, "-o" means the output file.
3. Input your selection of every setting.
#### For data processing mode
1. Prepare your input file with words. You must following the fix format:`word	date	type`(**Pay attention to the blank here, it's "\t", not "\p"**). "Word" means the word, "date" means the date of you record the word, and "type" means the type of the word, which includes "A" for all, "L" for listening, "R" for reading, "S" for speaking, "W" for writing. You can refer to my [wordlist.list](./wordlist.list) as an example to see how to record your words.
2. Clone the data processing mode code: `git clone https://github.com/qyyy/WordsTool.git`.
3. Revise the `settings.py` config file according to your demand.
4. Run the tool: `python3 main.py`.
### Todo list
- Support Chinese meaning of the words by using NLP method.
