"""
4-1

(1)
   5
(2)
   5
(3)
   5
(4)
   5
(5)
   5
(6)
   5
(7)
   4
(8)
   5

"""

#4-2
isCurry=True

while isCurry:
   #このループは別になくても
    count =1
    print("カレーを召し上がれ")
    while True:
        print(f"{count}皿のカレーを食べました")
        answer=input("おかわりはいかがですか？(y/n)>>")
        if answer == "y":
            count += 1
            continue
        if answer == "n":
            print("ごちそうさまでした")
            isCurry = False
            break

# 4-3

for num in range(10,0,-1):
    print(f"{num}、",end="")
    if num == 1:
        print("Lift off ！")
        break
print("Lift off ！")

"""
ptint(f"(10 -count),",end="")
"""

# 4-4
#(1)
for num in range(10):
   print()
   for num2 in range(10):
      print(num * num2,end=" ")
      
#(2)

#(3)

# 4-5

# 4-6
