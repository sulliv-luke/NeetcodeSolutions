class Solution(object):
    def encode_decode(self, list):

        def encode_list(list):
            # Uses list comprehension to append the delimiter to all elements except the last one
            # and then joins them together in one operation.
            encoded_string = ':;'.join(list)
            return encoded_string
        
        def decode(string):
            # Decodes a given string into a list of strings
            length = len(list)
            decoded_list = []
            return string.split(':;')
        
        s = encode_list(list)
        print(f"Encoded: {s}")
        print(f"Decoded: {decode(s)}")
    
if __name__ == "__main__":
    sol = Solution()
    list = ["neet", "code", "love", "you"]
    sol.encode_decode(list)