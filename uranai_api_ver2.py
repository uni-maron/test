"""
占いアプリ（tkenter使用）
"""

#モジュール起動
import tkinter as tk
import tkinter.ttk as ttk

#webスクレイピング
import requests
from datetime import date
import json

#今日の日付
today = date.today()
y = today.year
m = today.month
d = today.day

#requestsとjson使用してAPI取得
url = f"http://api.jugemkey.jp/api/horoscope/free/{y}/{m}/{d}"
result = requests.get(url)
data = json.loads(result.text)

#取ってきたAPIを整える
k_name = list(data["horoscope"].keys())[0]
kekka = data["horoscope"][k_name]


#自作関数
def sarch():
    seiza = select.get()
    match seiza:
        case "おひつじ座":
            unsei = kekka[0]
        case "おうし座":
            unsei = kekka[1]
        case "ふたご座":
            unsei = kekka[2]
        case "かに座":
            unsei = kekka[3]
        case "しし座":
            unsei = kekka[4]
        case "おとめ座":
            unsei = kekka[5]
        case "てんびん座":
            unsei = kekka[6]
        case "さそり座":
            unsei = kekka[7]
        case "いて座":
            unsei = kekka[8]
        case "やぎ座":
            unsei = kekka[9]
        case "みずがめ座":
            unsei = kekka[10]
        case "うお座":
            unsei = kekka[11]
        case _:
            unsei = {}
    textbox.delete(0.0,tk.END)
    out_str = f"{seiza}の今日の運勢は……\n{unsei['content']}\n\n【ラッキーカラー】{unsei['color']}\n【ラッキーアイテム】{unsei['item']}"
    
    textbox.insert(tk.END,out_str)


""" tkinter 設定 """
#ウインドウ設定
root = tk.Tk()
root.title("占いアプリ")
root.resizable(False, False)

#キャンバス設定
canvas = tk.Canvas(root, width=800, height=600, bg="blueviolet")
canvas.pack()

#画像設定
pic = tk.PhotoImage(file="image/ekisya.png")
canvas.create_image(200, 400, image=pic)

#タイトル文
text = tk.Label(text="今日の運勢を占いましょう!",
               font=("",40,""),
               background="yellow",
               padx=10)
text.place(x=120, y=30)

#セレクトボックス
holoscope = ("おひつじ座", "おうし座", "ふたご座",
                    "かに座", "しし座", "おとめ座",
                    "てんびん座", "さそり座", "いて座",
                    "やぎ座", "みずがめ座", "うお座")
select = ttk.Combobox(values=holoscope,
                      font=("",20,""),
                      width=10)
select.place(x=500, y=150)

#ボタン
btn = tk.Button(text="占う",
                command=sarch,
                font=("",20,""),
                background="yellow",
                width=10)
btn.place(x=500, y=300)

#出力欄
textbox = tk.Text(width=55,height=14)
textbox.place(x=380, y=400)

#画面継続表示
root.mainloop()