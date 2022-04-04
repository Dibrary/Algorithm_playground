

table = {"a":"@", "b":"8", "c":"(","d":"|)", "e":"3","f":"#","g":"6",
         "h":"[-]","i":"|","j":"_|","k":"|<","l":"1","m":"[]\/[]","n":"[]\[]",
         "o":"0","p":"|D","q":"(,)","r":"|Z","s":"$","t":"']['","u":"|_|","v":"\/","w":"\/\/",
         "x":"}{","y":"`/","z":"2"}

string = input()

result = ""
for i in string:
    if i.isalpha():
        tmp = i.lower()
        if tmp in table:
            result += table[tmp]
    else:
        result += i

print(result)
