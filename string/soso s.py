def string_both_end(str):
 if len(str)<2:
    return ' '
 return str[0:2]+str[-2:]
print(string_both_end('so'))
print(string_both_end('soumensir'))
print(string_both_end('s'))