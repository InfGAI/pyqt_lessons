#цифры числа
x=int(input())
oct=0
pow=1
while x!=0:
    last_digit=x%5
    x=x//5
    print(last_digit)
    oct=last_digit*pow+oct
    pow*=10
print(oct)


1101(2)=8+4+1
1 * 1
0 *2
1*4
1*8










