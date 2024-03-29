#tuple_ex.py

#튜플
#(시퀀스형,) 변경불가 자료형

#튜플 생성()
t=(1,2,3)
print(t, type(t))

#()를 생략해도 튜플로 인식
t=1, 2, "python"
print(t, type(t))

#연결 : +
t2 = t + (3,4,5)
print("t2", t2)

#반복 : *
print(t * 3)

#인덱싱과 슬라이싱 가능
#t2에서 'Python', 3, 4를 추출해 봅시다
print(t2[2:5])  #[0][1][2][3][4][5] 2에서 5까지해야 python 3 4가 나옴

#길이를 얻자
print("len : ", len(t2))

print("----------------------------------------------")
print("Packing, Unpacking")
# [[[Packing, Unpacking]]]
print("t2", t2)

a, b, c, d, e, f = t2
print("Unpacking : ", a, b, c, d, e, f)

#튜플의 요소보다 변수의 수가 적을때
'''
a, b = t2 # ValueError: too many values to unpack 변수와 딱 맞아야함 
print(a, b)
'''

a, *b = t2
print(a, b)

a, b, *c, d, e = t2
print(a, b, c, d, e)