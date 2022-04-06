from math import *

def STIRLING(N) :
    FRAC_N_LOG10 = (N*log(N) - N + 0.5*log(2*pi*N) + log(1+1/(12.0*N)))/log(10)
    EXP_FRAC_N = int(FRAC_N_LOG10)
    COEF_FRAC_N = 10**(FRAC_N_LOG10 - EXP_FRAC_N)
    FRAC_N = str(COEF_FRAC_N) + " * 10^{" + str(EXP_FRAC_N) + "}"
    #print(str(N)+"! = "+FRAC_N)
    return COEF_FRAC_N, EXP_FRAC_N, FRAC_N
'''
def ANAL_FRAC(N) :
    FRAC_N_LOG10 = 0
    for i in range(1,N+1) :
        FRAC_N_LOG10 = FRAC_N_LOG10 + log10(i)
    EXP_FRAC_N = int(FRAC_N_LOG10)
    COEF_FRAC_N = 10**(FRAC_N_LOG10 - EXP_FRAC_N)
    FRAC_N = str(COEF_FRAC_N) + " * 10^{" + str(EXP_FRAC_N) + "}"
    #print(str(N)+"! = "+FRAC_N)
    return COEF_FRAC_N, EXP_FRAC_N, FRAC_N
    

N = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000]



f = open("stirling_test.txt", 'w')
f.write("N\tSTIRLING-COEF\tSTIRLING-EXP\tANAL-COEF\tANAL-EXP\tRELATIVE-ERROR\n")

for i in N :
    stirling = STIRLING(i)
    anal = ANAL_FRAC(i)
    rel_err = 100*abs(float(stirling[0]) - float(anal[0]))/float(anal[0])
    f.write("%d\t%s\t%s\t%s\t%s\t%.10f\n" %(i,stirling[0],stirling[1],anal[0],anal[1],rel_err))

f.close()
'''

N = int(input("ENTER A POSITIVE INTEGER : "))

coef_exp = STIRLING(N)

print("%d!=%s" %(N,coef_exp[2]))
