#Найти первое левое вхождение положительного числа X в нее или вывести -1, если число Х не встречалось
# def findx(seq, x):
#     ans = -1
#     for i in range(len(seq)):
#         if ans == -1 and seq[i] == x:
#             ans = i
#     return ans
#
# seq = [1, 2, 2, 1, 3]
# x = int(input())
# print(findx(seq, x))


#Найти последнее(правое) вхождение числа Х в неё или вывести -1, если число Х не встречалось
# def find_right_x(seq, x):
#     ans = -1
#     for i in range(len(seq)):
#         if seq[i] == x:
#             ans = i
#     return ans

#Найти максимальное число в последовательности
# def findmax(seq):
#     maxx = seq[0]
#     for i in range(1, len(seq)):
#         if seq[i] > maxx:
#             maxx = seq[i]
#     return maxx

#Найти максимальное число в последовательности и второе по величине число
#(такое, которое будет максимальным, если вычеркнуть из последовательнсти одно максимальное)

# def bothmax(seq):
#     maxx1 = min(seq[0], seq[1])
#     maxx2 = min(seq[0], seq[1])
#     for i in range(2, len(seq)):
#         if seq[i] > maxx1:
#             maxx1, maxx2 = seq[i], maxx1
#         elif seq[i] > maxx2:
#             maxx2 = seq[i]
#     return maxx1, maxx2
# print(bothmax([1, 2, 3, 2, 1]))

#Найти минимальное четное число в последовательности или вывести -1, если такого не существует

# def findmineven(seq):
#     ans = -1
#     flag = False
#     for i in range(len(seq)):
#         if seq[i] % 2 == 0 and (not flag or ans > seq[i]):
#             ans = seq[i]
#             flag = True
#     return ans

#Вывести все самые короткие слова через пробел
# def shortwords(words):
#     minlen = len(words[0])
#     for word in words:
#         if len(word) < minlen:
#             minlen = len(word)
#     ans = []
#     for word in words:
#         if minlen == len(word):
#             ans.append(word)
#     return ' '.join(ans)

#Задача 7
# def isleflood(h):
#     maxpos = 0
#     for i in range(len(h)):
#         if h[i] > maxpos:
#             maxpos = h[i]
#     ans = 0
#     nowm = 0
#     for i in range(maxpos):
#         if h[i] > nowm:
#             nowm = h[i]
#         ans += nowm - h[i]
#     nowm = 0
#     for i in range(len(h) - 1, maxpos - 1, -1):
#         if h[i] > nowm:
#             nowm = h[i]
#         ans += nowm - h[i]
#     return ans

#Задача 8
def rle(s):
    def pack(s, cnt):
        if cnt > 1:
            return s + str(cnt)
        return s

    lastsum = s[0]
    lastpos = 0
    ans = []
    for i in range(len(s)):
        if s[i] != lastsum:
            ans.append(pack(lastsum, i - lastpos))
            lastsum = s[i]
            lastpos = i
    ans.append(pack(lastsum, len(s) - lastpos))
    return ''.join(ans)
print(rle('AAAABBBCCXYZDDDDEEEFFFAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'))