
string = input()
left = string[:string.index("(")]
right = string[string.index(")")+1:]
left_cnt = left.count("@=")
right_cnt = right.count("=@")
print(left_cnt, right_cnt)



