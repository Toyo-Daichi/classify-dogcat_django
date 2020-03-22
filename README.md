# 画像判定アプリ

## 1. 概要
犬 or 猫どちらに該当するかを判定してくれるアプリ

![](./screenshot/1.png)
　　　　　　　　　　　　　　↓
![](./screenshot/2.png)

___
## 2. 環境
- Python 3.6.10
- Django 19.03.8
___
## 3. 大まかな手順
1. 仮想環境にてTensorFlowの導入
```bash
$ create -n djangoai tensorflow
$ source activate djangoai
```
2. データの収集
- [Flickr API](https://www.flickr.com/services/apps/create/)を取得
```bash
$ pip install flickrapi
```
→犬と猫を取得するためのスクリプト`dl.py`を作成
- 収集したデータをNumpy配列に変換する`generate_data.py`を作成
→トレーニングデータとテストデータに分割した`imagefiles.npy`を吐き出す。
3. モデル構築
4. Webアプリ開発
