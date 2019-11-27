from flask import Flask
from flask import json
from flask import jsonify
from flask_cors import CORS
import random

class cats_race:
    name: ""
    def __init__(self, name):
        self.name = name
        return
    def obj(self):
        return {"name" : self.name, "desc": "かわいい。"}

myD = [
    cats_race("アビシニアン").obj(),
    cats_race("アメリカンカール").obj(),
    cats_race("アメリカンショートヘア").obj(),
    cats_race("アメリカンボブテイル").obj(),
    cats_race("アメリカンワイヤーヘア").obj(),
    cats_race("ヴァン猫").obj(),
    cats_race("エジプシャンマウ").obj(),
    cats_race("オシキャット").obj(),
    cats_race("キムリック").obj(),
    cats_race("クリルアイランドボブテイル").obj(),
    cats_race("コーニッシュレックス").obj(),
    cats_race("コラット").obj(),
    cats_race("サイペリアン").obj(),
    cats_race("ジャパニーズ").obj(),
    cats_race("ジャパニーズボブテイル").obj(),
    cats_race("シャム").obj(),
    cats_race("シャルトリュー").obj(),
    cats_race("シンガプーラ").obj(),
    cats_race("スコティッシュフォールド").obj(),
    cats_race("スフィンクス").obj(),
    cats_race("セルカークレックス").obj(),
    cats_race("ソマリ").obj(),
    cats_race("ターキッシュアンゴラ").obj(),
    cats_race("ターキッシュバン").obj(),
    cats_race("デボンレックス").obj(),
    cats_race("トンキニーズ").obj(),
    cats_race("ドンスコイ").obj(),
    cats_race("日本猫").obj(),
    cats_race("ノルウェージャンフォレストキャット").obj(),
    cats_race("バーマン").obj(),
    cats_race("バーミーズ").obj(),
    cats_race("バリニーズ").obj(),
    cats_race("ピクシーボブ").obj(),
    cats_race("ヒマラヤン").obj(),
    cats_race("ブリティッシュショートヘア").obj(),
    cats_race("ペルシャ").obj(),
    cats_race("ボンベイ").obj(),
    cats_race("マンクス").obj(),
    cats_race("マンチカン").obj(),
    cats_race("ミンスキン").obj(),
    cats_race("メインクーン").obj(),
    cats_race("ヨーロピアンショートヘア").obj(),
    cats_race("ラガマフィン").obj(),
    cats_race("ラグドール").obj(),
    cats_race("ラパーマ").obj(),
    cats_race("ロシアンブルー").obj(),
    
]


app = Flask(__name__)

CORS(app)


@app.route('/')
def get_json():
    return jsonify(
        name= "my awesome api",
        data= random.sample(myD, 10) 
    )

if __name__ == '__main__':
    app.run(debug=False)
