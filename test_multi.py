#coding:utf-8

#GPIOライブラリをインポート
import RPi.GPIO as GPIO

#timeライブラリをインポート
import time

#collectionsライブラリのdequeオブジェクトをインポート
from collections import deque

#ピン番号の割当方式を「コネクタピン番号」に設定
GPIO.setmode(GPIO.BOARD)

#使用するピン番号を代入
IN_1=8    #BLUE
IN_2=10   #PINK
IN_3=16   #YELLOW
IN_4=18   #ORANGE

#各ピンを出力ピンに設定し、初期出力をローレベルにする
GPIO.setup(IN_1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN_2,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN_3,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN_4,GPIO.OUT,initial=GPIO.LOW)

#出力信号パターンのリストを作成
sig_1 = deque([0,1,0,0])       #1相励磁
sig_2 = deque([1,1,0,0])       #2相励磁

#回転させる角度をdegで入力
ang = 360

#角度degをパルス数に換算
p_cnt = int(ang / (5.625 / 64))

#回転方向を定義（-1が時計回り、1が反時計回り）
dir = 1

#パルス幅を変数に入力
#値が小さい程回転速度は上がる。0.001より小さい値にすると回転しない
p_wid = 0.001


#時計回りに1回転、反時計回りに1回転する
for i in range(0,2):
    #パルス出力開始
    for j in range(0,p_cnt):
        
        if(j % 2 == 0):
            #出力信号パターンを出力
            GPIO.output(IN_1, sig_2[0])
            GPIO.output(IN_2, sig_2[1])
            GPIO.output(IN_3, sig_2[2])
            GPIO.output(IN_4, sig_2[3])
                        
            #パスル幅分待機
            time.sleep(p_wid)
            
            #出力信号パターンをローテート
            sig_2.rotate(dir)
        else:
            #出力信号パターンを出力
            GPIO.output(IN_1, sig_1[0])
            GPIO.output(IN_2, sig_1[1])
            GPIO.output(IN_3, sig_1[2])
            GPIO.output(IN_4, sig_1[3])
                        
            #パスル幅分待機
            time.sleep(p_wid)
            
            #出力信号パターンをローテート
            sig_1.rotate(dir)
            
            
    #回転方向を逆向きにする
    dir = dir * -1
    #1秒待機
    time.sleep(1.0)
    #カウントアップ
    i += 1


#メッセージを表示
print("End of program")
    

#GPIOを開放
GPIO.cleanup()
