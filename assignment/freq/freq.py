# Count the frequency of each word

class word_freq:
    def input_str(self):
        self.sentence = input('Enter string:')
    
    def find_freq(self):
        self.words = self.sentence.split(' ')
        self.freq = {}
        for i in self.words:
            if i in self.freq:
                self.freq[i] += 1
            else:
                self.freq[i] = 1
    
    def display(self):
        print(f'Your frequency of occurence:\n{self.freq}')

ob = word_freq()
ob.input_str()
ob.find_freq()
ob.display()