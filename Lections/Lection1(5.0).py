#Дана строка в кодировке UTF-8, найти самый часто встречающийся в ней символ
#O(N^2)
# s = input()
# ans = ''
# anscnt = 0
# for i in range(len(s)):
#     nowcnt = 0
#     for j in range(len(s)):
#         if s[i] == s[j]:
#             nowcnt += 1
#     if nowcnt > anscnt:
#         ans = s[i]
#         anscnt = nowcnt
# print(ans)
#O(nk)
# s = input()
# ans = ''
# anscnt = 0
# for now in set(s):
#     nowcnt = 0
#     for i in range(len(s)):
#         if now == s[i]:
#             nowcnt += 1
#     if nowcnt > anscnt:
#         ans = now
#         anscnt = nowcnt
# print((ans, anscnt))
#O(N+K) = O(N)
# s = input()
# ans = ''
# anscnt = 0
# symcnt = {}
# for now in s:
#     if now not in symcnt:
#         symcnt[now] = 0
#     symcnt[now] += 1
#     if symcnt[now] > anscnt:
#         ans = now
#         anscnt = symcnt[now]
# print((ans, anscnt))

#Сумма последовательности
# seq = list(map(int, input().split()))
# seqsum = 0
# for num in seq:
#     seqsum += num
# print(seqsum)

#Максимум последовательности
# seq = list(map(int, input().split()))
# if len(seq) == 0:
#     print("-inf")
# else:
#     seqmax = seq[0]
#     for i in range(1, len(seq)):
#         if seq[i] > seqmax:
#             seqmax = seq[i]
# print(seqmax)