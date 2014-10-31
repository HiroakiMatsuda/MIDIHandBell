MIDIHandBell
======================
MIDIHandBellはMIDI::Message型のデータを受けてハンドベルを演奏するロボットを制御する[RT-Component][rtm]です．  
20音のハンドベルを持つロボットを制御することができます．  
MIDI::Messageについては[こちら][idl]をごらんください． 

[rtm]:http://www.openrtm.org/openrtm/ja
[idl]: https://github.com/HiroakiMatsuda/MIDIDataType

動作確認環境
------
Python:  
2.6.6  

OS:  
Windows 8/8.1 64bit / 32bit  

依存モジュール:  
[pySerial][serial]  

[serial]:http://pyserial.sourceforge.net/

ハンドベル駆動用ホビーサーボ:  
RS301   

Serial:  
 [RSC-U485](:http://www.futaba.co.jp/robot/rsc/index.html)  
RPU-11

更新履歴:  
------

ファイル構成
------
MIDIHandBell  
│― idl   
│― MIDI  
│― MIDI_POA  
│― MIDIDataType_idl.py  
│― bell.py  
│― pyrs.py  
│― MIDIHandBell.conf  
│― MIDIHandBell.py  

* MIDI, MIDI_POA, MIDIDataType.py  
独自データ型 MIDIDataTypeに関するファイルです．  
 
* bell.py  
ホビーサーボを動作させハンドベルを鳴らす制御全般を行うPython Moduleです.  
このファイル内でホビーサーボのIDとハンドベルの周波数のマッピングを行っています．  

* pyrs.py  
Futaba製のホビーサーボの制御を行うPython Moduleです．  
このモジュールの説明は[こちら][pyrs]をご覧ください．  

[pyrs]:https://github.com/HiroakiMatsuda/pyrs

* MIDIHandBell.conf  
ホビーサーボのPort番号やBaudrateの設定を行います．  
またハンドベルの振り上げ位置と，振り下ろし位置を設定できます.  

* MIDIHandBell.py  
MIDIConsoleOut RTC本体です．  

＊ 本RTCにおいてユーザーが操作すると想定しているファイルのみ説明しています．  

RTCの構成
------  
<img src="https://farm8.staticflickr.com/7575/15480999410_06933185a8.jpg" width="400px" />    
データポートは1つあり、以下のようになっています  
  
* midi\_in port :InPort  
データ型; MIDI::MIDIMessage  
MIDIメッセージを受け取り，受け取ったデータをコンソール上に表示します．  

* コンフィグレーション  
 ・`port`:  
 ホビーサーボの通信ポートの設定を行います．  
 ・`baudrate`:   
 ホビーサーボのボーレートを設定します．  
 ・`down\_position`:  
 ハンドベルの振り下ろし位置を設定します．   
 ・`up\_position`:  
 ハンドベルの振り上げ位置を設定します．   
 ・`channel`:  
 MIDIメッセージのチャンネルを設定します．  
 -1を設定した場合は，全チャンネルのメッセージに対して処理を行います．  
 ・`delay_time`:  
 各ロボット間でMIDIメッセージの遅延をキャンセルための待ち時間を設定します．  
 設置は1/1000秒となります．  
 
 コンフィグレーションはonStartUpで読み込みます．  
 モードを変更する場合は，一度MIDIConsoleOutを終了し，コンフィグレーション変更後に再度実行して下さい．


使い方：　MIDIParserを使用してテストする
------
###1. MIDIParserの入手する###
[MIDIParser][parser]はMIDIファイルを解析し，MIDI::MIDIMessage型のデータを曲のタイミングに合わせて出力するRTCです．  
[こちら][parser]よりDLしてください．

[console]:http://pyserial.sourceforge.net/


###2. 解析するMIDIファイルを設定する###
MIDIParser RTCに解析させるMIDIファイルを設定します．  

MIDIParser.confをテキストエディタなどで開きます．  
以下のようにコンフィグレーションが設定されていると思います．  

```conf.mode0.midi_file: ./midifile/simpletest.mid ```     

以下のように，mode numberとfile nameを設定することで複数MIDIファイルを登録することができます．  
＊MIDIファイルはmidifileフォルダ内に配置することを前提としています．  

```conf.mode<mode number>.midi_file: ./midifile/<file name>.mid ```     

###3. MIDIメセージを受け取る###
MIDIParser RTCとMIDIHandBell RTCを実行してください．  
各RTCが起動したらMIDIParser RTCのmidi\_outポートとMIDIHandBell RTCのmidi\_inポートを接続します．  
各ポートを接続したらMIDIParser RTCをActivateします．  
するとNote Onのイベントに合わせてハンドベルが演奏されます．  
      
以上が本RTCの使い方となります  

ライセンス
----------
Copyright &copy; 2014 Hiroaki Matsuda  
Licensed under the [Apache License, Version 2.0][Apache]  
Distributed under the [MIT License][mit].  
Dual licensed under the [MIT license][MIT] and [GPL license][GPL].  
 
[Apache]: http://www.apache.org/licenses/LICENSE-2.0
[MIT]: http://www.opensource.org/licenses/mit-license.php
[GPL]: http://www.gnu.org/licenses/gpl.html