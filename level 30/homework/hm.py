# 2) გააკეთეთ manual_replace ფუნქცია

def manual_len(s):
    count = 0
    for i in s:
        count += 1
    return count

print(manual_len("1da"))
print(len("1"))



def manual_replace(s1, char, replace_char):
     res = ""

     for i in s1:
         if i == char:
             res += replace_char
         else:
             res += i
     
     return res

print(manual_replace("Hello", "e", "."))
    