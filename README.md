## Introduction
This tool is aiming for memorize and collect English words more efficient.
I use it to prepare my TOEFL Exam. You can also use it for your other English exams.
The tool has the following functions:
- Record a new word.
- Sort the words according to frequency, date and dictionary order. Also just random.
- Produce an output file with the words in the order you want, you can use this to repeat these words.
### How to use it
#### For interactive mode
1. Clone the interactive mode code: `git clone -b interactive https://github.com/qyyy/WordsTool.git`.
2. Run the tool: `python3 main.py -i words.txt -o result.txt`. The "-i" means the path of input file with your words, "-o" means the output file.
3. Input your selection of every setting.
#### For data processing mode
1. Clone the data processing mode code: `git clone https://github.com/qyyy/WordsTool.git`.
2. Revise the `settings.py` config file according to your demand.
3. Run the tool: `python3 main.py`.
### Todo list
- Support Chinese meaning of the words by using NLP method.
