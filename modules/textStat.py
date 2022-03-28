import string

class TextContainer:
    def __init__(self, my_text):
        self.my_text = my_text

    def word_count(self):
        return (len(self.my_text.split(' ')))

    def char_count(self):
        return(len(self.my_text))
    
    def ascii_count(self):
        return(len([letter for letter in self.my_text if letter in string.ascii_letters]))

    def remove_punc(self):
        return_String = ""
        for letter in self.my_text:
            if letter not in string.punctuation:
                return_String += letter

        return return_String 
    
    

text = TextContainer("hello hello hello!!!")
print(text.word_count())
print(text.char_count())
print(text.ascii_count())
print(text.remove_punc())