

# 4-1
print("さあ、寝ようかしら")
count = 0
count += 1
print(f"ひつじが{count}匹")
count += 1
print(f"ひつじが{count}匹")
count += 1
print(f"ひつじが{count}匹")
print("おやすみなさい…")

# 4-2
count =0
while count < 10:
    count +=1
    print(f"ひつじが{count}匹")
print("おやすみなさい…")



#4-3　∞ループ
# count =0
# while count<3:
#     print(f"ひつじが{count}匹")
# print("すやすや…zzz")

#4-4
is_awake = True
count = 0
while is_awake == True:
    count += 1
    print(f"ひつじが{count}匹…")
    key = input("もう眠りそうですか？(y/n)>>")
    if key == "y":
        is_awake = False
print("おやすみなさい…")

# 4-5 繰り返しでリストを作成
count = 0
student_num = int(input("学生の数を入力 >>"))
#score_list = list()
score_list = [] #中身のないリストを用意する↑と同様の意味
while count < student_num:
    count += 1
    score = int(input(f"{count}人目の試験の得点を入力>>"))
    score_list.append(score)
print(score_list)
total=sum(score_list)
print(f"平均点は{total/student_num}")

"""
作る数を用意する(入力してもらう)
リストを用意する
    作る数が出来上がるまでループする
    カウントを増やす
    １人目のデータを入力してもらう
    １人目のデータをリストに追加する
リストをすべて表示する
リスト内のデータをすべて足し合わせる
リスト内のデータを作ったリストの数で割る
"""

#4-6 リストの全要素を繰り返し参照する
scores = [80,20,75,60]
count = 0
while count < len(scores):
    if scores[count] >=60:
        print("合格")
    else:
        print("不合格")
    count +=1

# 4-7

scores = [80,20,75,60]
for data in scores:
    if data >= 60:
        print("合格")
    else:
        print("不合格")

"""
繰り返しのたびにリストの要素を代入
リストの要素をひとつづつ処理をしていく
for i in リスト名
    if条件文:
        処理
    else:


"""
#4-8 for文で決まった回数を繰り返す
for num in range(3):
    print("Pythonは楽しい")


#4-
#家でプッシュしていたら、プルを一回やる






""" ゲームループを無限ループで処理
#whileの中で、ループ実行を分岐させる。
 #count 1 増加ループ
 #count 1 減少ループ
 #count 10 増加ループ
 #count 10 減少ループ

# 0.0以上1.0未満のfloat
# print(random.random())
# 任意の範囲のfloat
# print(random.uniform(100,200))
# range()から選択されたint
# print(random.randrange(10))
# 任意の範囲のint
# print(random.randint(50,100))
"""