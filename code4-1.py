

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
# rangeは0→1→2と増えていく　range(0,3)オブジェクト
for num in range(3):
    print("Pythonは楽しい")

print(list(range(10)))
#[0,1,2,3,4,5,6,7,8,9,]
range(10,0,-1)
#→[10,9,8,7,6...]
range(3,10,9)
#→[3]スタートから9増やせないので次のステップに行けない
#第三引数はステップ、
#オーバーロード同じ名前の関数を、引数の数種類で宣言できる



#4-9 データのまとまりからサンプルを抽出する

ages = [28,50,8,20,78,25,22,10,27,33]#データ数10
num = 5 #目標の抽出数
samples = [] #samples = list() #選別後のデータを格納するリスト
for age in ages:
    if 20 <= age < 30: #20以上30未満
    #if age / 10 == 2 #10で割って整数が2になるもの
        if len(samples) < num:#追加された要素数がnumの数になるまで
            samples.append(age)
print(samples)




#4-10 break　目標数に達成したら繰り返しを終了
ages = [28,50,8,20,78,25,22,10,27,33]#データ数10
num = 5
samples=[]
for data in ages:
    if 20 <= data <30:
        samples.append(data)
        if len(samples) == num:#追加されたサンプル数とnumが一致したら
            break
print(samples)



#4-11 不要な回のループをスキップする
ages = [28,50,8,20,78,25,22,10,27,33]#データ数10
num = 5
samples=[]
for data in ages:
    if not isinstance(data,int):#整数出ないデータはスキップ
        continue
    if data < 20 or data >=30:#条件に合致しないデータはスキップ
        continue
    samples.append(data)
print(samples)
#isinstance (指定の変数,データ型)　データがあっていればTrue違えばFalse
#not がついているので、特定のデータ型でなければTrue



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