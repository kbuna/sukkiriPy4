
# 4-4

#(1) 99
for num in range(10):
    if num == 0:
        continue
    for num2 in range(10):
        if num2 == 0:
            continue
        print(num * num2,end="")
    print()

print()
#(2) 奇数の段のみ
for num in range(10):
    if num == 0:
        continue
    if num % 2 ==0:
        continue
    for num2 in range(10):
        if num2 == 0:
            continue
        print(num * num2,end="")
    print()

print()
#(3)　答えが50を越えたら計算中止
for num in range(10):
    if num == 0:
        continue
    if num % 2 ==0:
        continue
    for num2 in range(10):
        if num2 == 0:
            continue
        result = num*num2
        if result > 50:
            continue
        print(result,end="")
    print()



print()
# 4-5
#(1)
days =[
    7.8,
    9.1,
    10.2,
    11.0,
    12.5,
    12.4,
    14.3,
    13.8,
    12.9,
    12.4]
temp =[]
for i in days:
    temp.append(i)

print(days)
print(temp)
print()

#(2)
temp =[]
for i in days:
    print(i)
    temp.append(i)
print()

#(3)
temp =[]
for i in days:
    temp.append(i)
temp_new = temp
temp_new[5] = "N/A"

print(temp_new)
print()

#(4)
total = 0
for i in temp_new:
    if not isinstance (i,float):
        continue
    total += i
print(f"{total}")
print()

# 4-6
#(1)

numbers = [1,1]
backnum = 0 
frontnum = 0
total = 0
count = 0
flag = True
while flag:
    frontnum = numbers[count]
    backnum = numbers[count+1]
    total = frontnum + backnum
    if total >1000:
        flag = False
        break
    numbers.append(total)
    count += 1
    
print(numbers)
print()

#(2)
ratios = []
backnum2 = 0 
frontnum2 = 0
total = 0
count = 0
flag = True

while flag:
    if count==len(numbers):
        flag = False
        break
    if count==0:
        count += 1
        continue

    frontnum2 = numbers[count]
    print(frontnum2)
    backnum2 = numbers[count-1]
    print(backnum2)
    total = frontnum2 / backnum2
   
    ratios.append(total)
    count += 1

print(ratios)
print()
#(3)
for i in ratios:
    result = int(i*1000)
    print(result/1000)

