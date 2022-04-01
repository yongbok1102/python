# -*- coding: utf-8 -*-

from math import * #math 모듈의 모든 함수 import

#Legendre 함수 P5(x)의 5개의 영점과 가중치
xi = [0, 
1./3*sqrt(5-2*sqrt(10./7)),
-1./3*sqrt(5-2*sqrt(10./7)),
1./3*sqrt(5+2*sqrt(10./7)),
-1./3*sqrt(5+2*sqrt(10./7))]

wi = [128./225,
(322+13*sqrt(70))/900,
(322+13*sqrt(70))/900,
(322-13*sqrt(70))/900,
(322-13*sqrt(70))/900]

def f(x) : #피적분함수
    return 2000*log(140000/(140000-2100*x)) - 9.8*x
a = 8
b = 30

N = int(input("구간 수를 입력하시오. "))
dx = (b-a)/N

x = [a+i*dx for i in range(N)]
x.append(b)

I = 0

for i in range(N) : 
    A = x[i]
    B = x[i+1]
    for j in range(5) : 
        I = I + 0.5*(B-A)*wi[j]*f(0.5*(B-A)*xi[j] + (A+B)*0.5)


print("S = %.10f" %I)
