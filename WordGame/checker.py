# letters = ['a','a','b','a']
# i = 0
# length = len(letters)
# while(i<length):
#     if(letters[i]=='a'):
#         letters.remove(letters[i])
#         length = length - 1
#         continue
#     i=i+1
# print(letters)



def f1(nos,t):
    result=[]
    for x in nos:
        if x > t:
            result.append(x)
    return result


nos = [1,2,3,4,6,79,21,23,3,7]
print(f1(nos,10))
filtered=filter(f1(nos,10),nos)
