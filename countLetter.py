#coding=utf-8
#countLetter.py
print("아무 문자열을 입력하세요.")
a = input() #문자열을 입력받는다.

capLett = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #대문자
smalLett = "abcdefghijklmnopqrstuvwxyz" #소문자

numLett = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #a,b,c,...,z의 개수 (0으로 초기화)

totNumLett = 0 #전체 문자수

for i in range(0,26) : 
    numLett[i] = a.count(capLett[i]) + a.count(smalLett[i]) #입력받은 문자열에서 a,b,c,...,z의 개수를 계산한다.(대문자+소문자)
    arbitLet = smalLett[i]
    arbitNum = numLett[i]
    totNumLett = totNumLett + arbitNum #입력받은 문자열의 전체 문자수를 계산한다.
    print('\"',a,'\"에서 ',arbitLet,'는 ', arbitNum,'개입니다.')

print('\"',a,'\"는 총 ', totNumLett, '개의 문자로 이루어져 있습니다.')
