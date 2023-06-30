#решаем задачу
#N**2; СЛОЖНОСТЬ O(N*M) - НЕ ЖЕЛАТЕЛЬНАЯ
def strcointer(stroka):
    for sym in set(stroka):
        cointer=0
        for sub_sym in stroka:
            if sym==sub_sym:
                cointer+=1
        print(sym, cointer)

#ПЕРЕДЕЛЫВАЕМ В СЛОЖНОСТЬ O(N) - ЖЕЛАТЕЛЬНАЯ
def strcointer_new(stroka):
    syms_cointer={}
    for sym in stroka:
        syms_cointer[sym]=syms_cointer.get(sym, 0)+1
    print(syms_cointer)

stroka='abbccddd'
print(set(stroka))
strcointer(stroka)

strcointer_new(stroka)