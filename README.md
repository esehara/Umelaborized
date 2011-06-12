# Umelaborized  Ver0.1 #

## Umelaborizedとは？ ##

Umelaborizeは、Pythonで実装された、梅ラボのコラージュ作品を気軽に生成するためのモジュールです。

## ライセンス ##

このモジュールを使用する場合、著作表記を省略することは可能であり、生成された画像に関しても使用可能です。ただ、下の条件が必要になります。

1. このモジュールで生成された画像は如何なる媒体であれ、無償で使用ならびに改変が可能である。
2. このモジュールで生成された画像を使用して新しい作品を作る場合、如何なる作品であれ、上記の条件ならびにこの条件が適応されます。

## 使い方 ##

Umelaborizeをインスタンスするさいに、Jsonファイルが読み込まれます。
Jsonファイルは画像を配置する部分と、配置しない部分をドット絵のように指定します。
例えば次のように。

  [
    [0,0,0],
    [1,0,1],
    [1,1,1]
  ]

## 実装機能（リファレンス） ##

* Class Umelaborize(size_x,size_y,configfile)
    size_x,size_y:キャンパスサイズを指定します
    configfile   :Jsonfileを呼び出します

* def load_image(file)
    file : 使用する画像を指定します。

* def save_image(file)
    file : ファイルをセーブします。

* def test_show()
    作業中の画像を表示します。
    
* def kill_paste(time,flag)
    time : load_imageで読み込んだファイルの切り刻む回数を指定します。
    flag : 切り刻むさいに回転させ、変色させるかを指定します。

* def stamp_image(size,time)
    size : load_imageで読み込んだファイルのサイズを指定します。元の画像サイズをsize引数で割ったサイズが大きさになります。
    time : スタンプを行う回数です。

