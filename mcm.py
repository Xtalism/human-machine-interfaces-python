num1 =int(input())
num2 =int(input())

A = max(num1, num2)
B = min(num1, num2)

while B:
    mcd = B
    B = A % B
    A = mcd
mcm =  (num1 * num2) // mcd

print('El M.C,D de {0} y {1} es {2}'.format(num1, num2, mcd))
print('El M.C.D de {0} y {1} es {2}'.format(num1, num2, mcm))