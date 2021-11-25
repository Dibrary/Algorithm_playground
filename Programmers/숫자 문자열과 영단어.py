'''
2021 카카오 채용연계형 인턴십
'''

def solution(s):
    tmp = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    value = ['0','1','2','3','4','5','6','7','8','9']
    for i in range(0, len(tmp)):
        s = s.replace(tmp[i], value[i])
    return int(s)