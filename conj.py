def calNorm(x) : 
    result = 0
    for ele in x : 
        result += ele**2
    
    return result



#A input###############################################################
N = int(input("Enter the number of unknowns : "))
A = []
print("Enter the matrix A. Each element is separated by \' \'")
for i in range(N) :
    A_tmp=[]
    A_tmp_set = input()
    A_tmp_set = A_tmp_set.split(' ')

    for j in range(N) :
        a = float(A_tmp_set[j])
        A_tmp.append(a)
    A.append(A_tmp)
######################################################################




#b input##############################################################
b = []
print("Enter the vector b")
for i in range(N) : 
    b_ele = float(input())
    b.append(b_ele)
######################################################################




#x0 input#############################################################
x = []
print("Enter the initial guess x0")
for i in range(N) : 
    x_ele = float(input())
    x.append(x_ele)
######################################################################




#calculating AT*A#####################################################
ATA = []
for i in range(N) :
    ATA_tmp = []
    for j in range(N) :
        ATA_tmp.append(0.0)
    ATA.append(ATA_tmp)

for i in range(N) :
    for j in range(N) :
        for k in range(N) : 
            ATA[i][j] += A[k][i]*A[k][j]
######################################################################




#calculating AT*b#####################################################
ATb = []
for i in range(N) : 
    ATb.append(0.0)

for i in range(N) : 
    for j in range(N) : 
        ATb[i] += A[j][i]*b[j]
######################################################################




#calculating r0#######################################################
r = []
ATAx = []
for i in range(N) : 
    ATAx.append(0.0)
    r.append(0.0)

for i in range(N) : 
    for j in range(N) : 
        ATAx[i] += ATA[i][j]*x[j]
    r[i] = ATb[i] - ATAx[i]
######################################################################




#setting p0###########################################################
p = []
for i in range(N) : 
    p.append(r[i])
######################################################################




#calculating rold######################################################
rold = calNorm(r)
#######################################################################




#simulation setting####################################################
N_itr = int(input("Enter the iteration number : "))
tol = float(input("Enter the tolerance error : "))
#######################################################################




#ATAp setting##########################################################
ATAp = []
for i in range(N) : 
    ATAp.append(0.0)
#######################################################################   


print("itr : 1 , err : %e" %(rold**0.5))

#conjugate gradient method#############################################
for itr in range(N_itr) : 
    pTATAp = 0.0
    
    for i in range(N) : 
        ATAp[i] = 0.0
    
    for i in range(N) : 
        for j in range(N) : 
            ATAp[i] += ATA[i][j]*p[j]
        pTATAp += ATAp[i]*p[i]
    
    alpha = rold / pTATAp

    for i in range(N) : 
        x[i] = x[i] + alpha*p[i]
        r[i] = r[i] - alpha*ATAp[i]
    
    rnew = calNorm(r)
    print("itr : %d , err : %e" %(itr+2, rnew**0.5))
    if rnew**0.5 < tol : 
        break
    
    beta = rnew / rold

    for i in range(N) : 
        p[i] = r[i] + beta*p[i]

    rold = rnew
#######################################################################




#showing result########################################################
print("x=")
for i in range(N) : 
    print("%.6f" %(x[i]))
#######################################################################




input("press any keys to continue")