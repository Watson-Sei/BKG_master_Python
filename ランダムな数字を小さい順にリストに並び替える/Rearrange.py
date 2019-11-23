'''　準備 '''
# Python標準ライブラリーをインポート
import random      

# ランダムで取得した数値を追加するリスト
model_list = []
# 数値が小さい順に格納されるリスト     
result_list = []

# 10回forループを繰り返す
for numeric in range(1,11):     
    # 1~100までのランダムな数値を出力しリストに追加する 
    model_list.append(random.randint(1,100))  

# model_listにランダムな数値が追加されているか確認をする
print(model_list)

''' メイン処理 '''
# model_listをforループする
for numeric in model_list:

    # print(numeric)

    # result_listに値がない場合は比べることができないので比べずにresult_listに追加する
    if len(result_list) == 0 :
        # result_listにnumericの値を追加する
        result_list.append(numeric)
        print(result_list)
        continue

    # もしnumericがresult_listの最大値より大きければ処理を実行
    if result_list[-1] < numeric :
        # result_listに追加する
        result_list.append(numeric)
        print(result_list)
        continue
    
    # もしnumericがresult_listの最大値より小さければ処理を実行する
    elif result_list[-1] > numeric :
        print('result_list[-1]より小さい'+str(numeric))
        print('result_listの数:'+str(len(result_list)))
        for i in range(len(result_list)):
            if result_list[i] < numeric :
                continue
            elif result_list[i] > numeric:
                result_list.insert(i,numeric)
                print('小さい値のリスト格納が完了しました。')
                # result_listに数値が追加されたかを確認
                print(result_list)
                break




print('小さい順に並べました:'+str(result_list))
        
    
    
