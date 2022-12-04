from re import sub


def to_snake_case(replacer):
    return '_'.join(
        sub('([A-Z][a-z]+)', r' \1',
            sub('([A-Z]+)', r' \1',
                replacer.replace('-', ' '))).split()).lower()


def to_camel_case(replacer):
    capitalize_first = input('Capitalize first? -  ')
    s = sub(r"(_|-)+", " ", replacer).title().replace(" ", "")
    if capitalize_first == 'False' or capitalize_first == 'false':
        return ''.join([s[0].lower(), s[1:]])
    if capitalize_first == 'True' or capitalize_first == 'true':
        return ''.join([s[0].upper(), s[1:]])


print(to_snake_case('IdIoTic-CaseCase'))
