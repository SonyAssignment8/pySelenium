#Replace function using own method

class ReplacableString:
    def __init__(self, base_string):
        self.base_string =base_string

    def replacer(self, to_replace, replacer):
        for i in range(len(self.base_string)):
            if to_replace == self.base_string[i:i+len(to_replace)]:
                self.base_string = self.base_string[:i] + replacer + self.base_string[i+len(to_replace):]

    def __str__(self):
        return str(self.base_string)


test_str = ReplacableString("This is eth string")
test_str.replacer("eth", "the")
print (test_str)