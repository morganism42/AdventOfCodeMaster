file = open('dec1.txt', 'r')
data = file.read()
file.close()
data = data.split('\n')
total = 0
nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numss = ['on1e', 'tw2o', 'thr3ee', 'fou4r', 'fiv5e', 'si6x', 'sev7n', 'eig8t', 'nin9e']
for i in data:
    temp = ''
    temp2 = i
    for j, x in enumerate(nums):
        temp2 = temp2.replace(x, numss[j])
    for j in temp2:
        if j in '123456789': temp += j
    total += int(temp[0]+temp[-1])
print(total)