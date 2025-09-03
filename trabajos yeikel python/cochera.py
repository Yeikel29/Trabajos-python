string_list = []
result = []

def upe(len):
    for i in range(len - 3):
        if string_list[i] != "U" or string_list[i] != "P" or string_list[i] !="E" :
            result.append(string_list[i])
        elif string_list[i] == "U" and (string_list[i + 1] != "P" or string_list[i + 2] != "E"):
            result.append(string_list[i])
            
            
    return "".join(result)

len = int(input())
string = input()


for i in range(len):
    string_list.append(string[i])


print(upe(len))