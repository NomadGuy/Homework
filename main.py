import re


class NameConverter:
    def __init__(self, convert: str):
        self.convert = convert;

    def to_snake_case(self):
        return '_'.join(
            re.sub('([A-Z][a-z]+)', r' \1',
                   re.sub('([A-Z]+)', r' \1',
                          self.convert.replace('-', ' '))).split()).lower()

    def to_camel_case(self):
        capitalize_first = input('Capitalize first? -  ')
        s = re.sub(r"(_|-)+", " ", self.convert).title().replace(" ", "")
        if capitalize_first == 'False' or capitalize_first == 'false':
            return ''.join([s[0].lower(), s[1:]])
        if capitalize_first == 'True' or capitalize_first == 'true':
            return ''.join([s[0].upper(), s[1:]])


if __name__ == '__main__':
    a = NameConverter('MariaIvanovna')
    b = NameConverter('maria_ivanovna')
    print(a.to_snake_case())
    print(b.to_camel_case())
