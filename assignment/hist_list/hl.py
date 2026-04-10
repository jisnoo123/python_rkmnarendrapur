# Histogram to List

class h_to_l():
    def input(self):
        self.hist = {}
        n = int(input('Enter number of characters: '))

        for i in range(n):
            char = input('Enter character: ')
            freq = int(input('Enter frequency: '))
            self.hist[char] = freq
        
        print(f'Your dictionary:\n{self.hist}')
    
    def convert(self):
        # Convert histogram to list
        self.hist_list = list()

        for k,v in self.hist.items():
            for i in range(v):
                self.hist_list.append(k)
        
        return self.hist_list
    
ob = h_to_l()

ob.input()
hist_list = ob.convert()

print(f'Your list:\n{hist_list}')