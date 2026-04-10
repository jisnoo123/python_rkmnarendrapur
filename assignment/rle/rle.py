# Run Length Encoding and Decoding: A compression technique

class rle:
    def input_chars(self):
        self.input_list = list()
        n = int('Enter number of characters:')
        for i in range(n):
            self.input_list.append(input('Enter character:'))

        print(f'Your input\n{self.input_list}')
    
    def encode_to_rl(self):
        # Encode to run length
        self.encoded = list()
        c = 0
        char = self.input_list[0]

        for i in self.input_list:
            if char == i:
                c += 1
            else:
                self.encoded.append((char, c))
                char = i
                c = 1
        
        return self.encoded
    
    def decode_back(self):
        # Decode back to original list
        self.decoded = list()

        for i in self.encoded:
            for iter in range(i[1]):
                self.decoded.append(i[0])
        
        return self.decoded
    
ob = rle()
ob.input_chars()

encoded = ob.encode_to_rl()
decoded = ob.decode_back()

print(f'Encoded: {encoded}\nDecoded: {decoded}')