def char_frequency(string):
    freq_dict ={}
    for char in string:
        freq_dict[char]=freq_dict.get(char,0)+1
        return freq_dict
string = input("enter a string:")
result=char_frequency(string)
print("character frequency:",result)
