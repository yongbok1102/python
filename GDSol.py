#coding=utf8

# 잔차 계산 (일정값 이하면 stop)
def calRes(r,n):
    sum = 0
    for i in range(n):
        sum += r[i]*r[i]
    return sum**0.5

# 미지수의 개수 입력
n = int(input("미지수의 개수를 입력하시오 : "))

#최대 반복횟수 입력.
itr = 0
max_itr = int(input("최대 반복횟수를 입력하시오 : "))

#허용 잔차 입력
resid = float(input("허용 잔차를 입력하시오 : "))

# A 입력
A = []
print("A를 입력하시오 (Ax=b) ' '으로 구분됩니다.")
for i in range(n):
    tmp_A = []
    A_tmp = input()
    A_tmp = A_tmp.split(' ')
    for j in range(n):
        a = float(A_tmp[j])
        tmp_A.append(a)
    A.append(tmp_A)

# b 입력
b = []
print("b를 입력하시오 (Ax=b)")
for i in range(n) : 
    b_ele = float(input())
    b.append(b_ele)

# x 입력
x = []
print("연립방정식 Ax=b의 해의 초기 추정치 x0을 입력하시오.")
for i in range(n):
    x_ele = float(input())
    x.append(x_ele)

# x0 설정
x0 = []
for i in range(n):
    x0_ele = x[i]
    x0.append(x0_ele)

AX = [] #AX = A*x
AX_old = []
r = [] #r = AX-b
r_old=[]
grad = [] #grad = (AT)*r
grad_old=[]


#잔차 계산 (r=Ax-b, res=sum(r^2))
for i in range(n):
    AX_tmp = 0
    for j in range(n):
        AX_tmp += A[i][j]*x[j]
    AX.append(AX_tmp)
for i in range(n):
    r_tmp = AX[i]-b[i]
    r.append(r_tmp)

#구배 계산
for i in range(n):
    grad_tmp = 0
    for j in range(n):
        grad_tmp += A[j][i]*r[j]
    grad.append(grad_tmp)

#잔차 계산 (r=Ax-b, res=sum(r^2))
for i in range(n):
    AX_tmp = 0
    for j in range(n):
        AX_tmp += A[i][j]*x0[j]
    AX_old.append(AX_tmp)
for i in range(n):
    r_tmp = AX[i]-b[i]
    r_old.append(r_tmp)

#구배 계산
for i in range(n):
    grad_tmp = 0
    for j in range(n):
        grad_tmp += A[j][i]*r_old[j]
    grad_old.append(grad_tmp)

#step parameter 입력
step_para = float(input("step parameter를 입력하시오 : "))

#수치해석
while calRes(r,n)>resid :
    itr += 1
    for i in range(n):
        x0[i] = x[i]
        AX_old[i] = AX[i]
        r_old[i] = r[i]
        grad_old[i] = grad[i]
        x[i] = x0[i] - step_para*grad_old[i]
    #잔차, 구배의 초기화
    for i in range(n):
        AX[i] = 0
        r[i] = 0
        grad[i] = 0
    #잔차 계산 (r=Ax-b, res=sum(r^2))
    for i in range(n):
        for j in range(n):
            AX[i] += A[i][j]*x[j]
    for i in range(n):
        r[i] = AX[i]-b[i]
    #구배 계산
    for i in range(n):
        for j in range(n):
            grad[i] += A[j][i]*r[j]
    #step parameter 조정
    if calRes(r,n) < calRes(r_old,n):
    	step_para *= 10.0
    else : 
        step_para /= 10.0
        for i in range(n) :
            x[i] = x0[i]-step_para*grad_old[i]
        for i in range(n):
            AX[i] = 0
            r[i] = 0
        #잔차 계산 (r=Ax-b, res=sum(r^2))
        for i in range(n):
            for j in range(n):
                AX[i] += A[i][j]*x[j]
        for i in range(n):
            r[i] = AX[i]-b[i]
    if step_para>=1e+018 or step_para<=1e-016 :
        step_para = 1;
    if itr%100==0 : 
        print("itr: %d, resid: %e" %(itr, calRes(r,n)))

    if calRes(r,n)<=resid :
        print("itr: %d, resid: %e" %(itr, calRes(r,n)))
    if itr == max_itr:
        break
print("x=\n")
for i in range(n):
    print("%f" %(x[i]))

input("Press any key to continue...")
