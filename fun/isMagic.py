
# import math
# arr = [7, 3, 2]
# ct = 0 
# for i in range(len(arr)):
#     if math.ceil( float(sum(arr[:i]) / 2) ) == arr[i]:
#         ct += 1
# print(ct)

text = "SaharaNet"
res = [] 
l = len(text)
for i in range(l):
    ct = 1
    for j in range(i+1, l):
        if not text[i] == text[j]:
            ct += 1
        else:
            break
    res.append(ct)
print(max(res))
print(res)