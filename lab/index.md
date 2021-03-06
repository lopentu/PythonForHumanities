---
layout: default_pfh
permalink: /PythonForHumanities/lab/
---

Lab Session
===========

課程大綱
-------

| 週次 | 日期 |           內容                        | 投影片連結 |
| ----| -----|--------------------------------------|----------|
| 1.  | 09/12|  課程簡介 （no lab session）           |           |
| 2.  | 09/19|  脈絡：程式思維、開發環境                |   [🔗][w2] |
| 3.  | 09/26|  觀察：分析問題（變數、指派、數字與字串）   |   [🔗][w3] |
| 4.  | 10/03|  規則：語法結構（條件式、對應表）          |  [🔗][w4]  |
| 5.  | 10/10|  （國慶日）                            |
| 6.  | 10/17|  功能：操作資料結構（資料結構方法）        |  [🔗][w6]  |
| 7.  | 10/24|  迭代：程式流程控制（迴圈）               |  [🔗][w7]  |
| 8.  | 10/31|  分工：程式組織（函數）                  |  [🔗][w8]  |
| 9.  | 11/07|  期中考準備                            |  [🔗][w9]  |
| 10.  | 11/14|  （期中考）                           |
| 11.  | 11/21|  樣式：正規表達式                      |  [🔗][w11]  |
| 12.  | 11/28|  剖析：分析中文文字檔案                 |  [🔗][w12]  |
| 13.  | 12/05|  田野：網路資料蒐集                    |  [🔗][w13]  |
| 14.  | 12/12|  存取：檔案與資料讀寫                   |  [🔗][w14]  |
| 15.  | 12/19|  文本：電腦與自然語言                   |  [🔗][w15]  |
| 16.  | 12/26|  展演：視覺化與呈現                     |  [🔗][w16]  |
| 17.  | 01/02|  期末報告                             |
| 18.  | 01/09|  繳交期末報告                          |

[w2]:https://docs.google.com/presentation/d/1nvdXhE-HQqtjLFTL6zL1gcnQ-DVpHUETdTT00M28HI8/edit?usp=sharing
[w3]:https://docs.google.com/presentation/d/1tC5rDWTjwftrwuXJux0ydRgz2eICsUnlRWPdBcZRgSU/edit?usp=sharing
[w4]:https://docs.google.com/presentation/d/1ViWN7nhabkomNc508C1Am0Lz-FiaaRX2nps67Fi2kjI/edit?usp=sharing
[w6]:https://drive.google.com/open?id=1l5z3erlN0U4rNj2oVDFROrwJ35u79W-ct7bChKDtxOs
[w7]:https://docs.google.com/presentation/d/1KClaEANP1yRj63LpE-pUds-wvvOydAlEI1qlrBwwqus/edit?usp=sharing
[w8]:https://docs.google.com/presentation/d/1BqbNGBqXJZSfIgwqNDNDFX_xu5yNtzfVZ7XWjJowJJo/edit?usp=sharing
[w9]:https://docs.google.com/presentation/d/1GD2MC91HdEs-vKwjL_xY_mdThflVgk5YGsm3Ipj42vM/edit?usp=sharing
[w11]:https://docs.google.com/presentation/d/1xZUbcX1haocGEn7O9FEiT8tnjy_z7ErYpzyyRVQRMjc/edit?usp=sharing
[w12]:https://docs.google.com/presentation/d/1tXucAP3mRK0LfZBvJosEQjTJfgdJvxJOJO0uM1Shg6o/edit?usp=sharing
[w13]:https://docs.google.com/presentation/d/16EkIuY1z9VJxEUCMmAE8l1z_Qt_LCjYfOZOWgMwVNhw/edit?usp=sharing
[w14]:https://docs.google.com/presentation/d/1czltdRveXiN-58MrF8povT51vzZUC-JZqtM9w_M-Nf0/edit?usp=sharing
[w15]:https://docs.google.com/presentation/d/10axw2qdwlOFBBklctvAnX5GRCXVnNW5r5zMh8NwLZQ4/edit?usp=sharing
[w16]:https://docs.google.com/presentation/d/1lr7hmC5nM4U_uqWrGoe3Hbfsi7ATtagzc3yRch8rtL0/edit?usp=sharing

Python 作為人文學群的程式語言
-------------------------
「學程式」是全民運動：十二年國教科技領域課綱草案也預定將程式列為必修，甚至下伸至國中；坊間的職業訓練課程也教程式，幾乎是就業保證；大眾媒體亦報導眾多「非本科」學生因興趣自學程式，而進入相關產業獲得優渥待遇。的確，寫程式的前景大好，在機器學習、深度學習、資料科學當紅的時代，能夠寫程式好像變成基本能力。

但學程式對人文學群的實踐者而言有另一層意義。最近十幾年來，社群媒體、電子商務、個人媒體、甚至物聯網（IoT）、區塊鍊（block chain）應用，都是之前從未有過的人類活動，這些活動特殊之處是其軌跡存於數位世界。對比以往人文學群的經驗對象來自於訪談、問卷、實驗法、文本、民族誌探詢實際的人、部落、族群、社會；現在，人類文化社會活動的痕跡卻以數位形式儲存，可能在個人運算裝置（手機、筆電、桌機），更可能存在於某雲端伺服器（Google, Facebook, Instagram, Dcard）。人文學群實踐者在現代反而須透過人造物，電腦，才得以近用（甚至更大膽的用語是認識）人類活動在數位世界產生的真實投影。學程式，在這個意義下，重要性遠遠不止實用考量，而更是因程式是我們和電腦溝通的管道，它是我們得以認識人類在數位世界活動的窗口。

Python是近幾年當紅的程式語言，語法看似簡單卻完全不減其強大的表達功能。Python具有活躍的社群，提供各式各樣的套件（packages）、問答與教學資源，學習者或開發者都能有堅實的社群支持。

學習「寫程式」不只是學語言，也是學新世界，而接觸程式世界的第一步是培養「計算思維」。Lab Session的目的是讓大家有機會熟悉如何透過「計算思維」思考問題，並將思考過程用Python程式語言表達出來。期待這個能力「帶得走」，因為人類的文化社會活動總是複雜，我們永遠需要更多的觀點，更大膽地創新揭示層層疊疊的新世界。



請配合...
--------

### 保持正面思考

在短短幾個月從無到有學會Python，需要很多時間和心力，老師和助教也相信大家的學習熱誠和能力。可是萬一有其他事件轉移了你的注意力（社團、朋友、家庭、熱戀、失戀、其他課程等等），也請保持對於Python以及程式設計的正面態度。既然選了課，至少期待你能藉機認識Python。即便現在和Python無緣，以後可能還是會有緣。

### 主動學習
學程式很難，也正因為難，所以很有趣。老師及助教群會盡可能將如何學程式的內容設計成一套有系統的課程安排。然而，學習是很個人的事，每個人都有自己的經驗、能力、動機和節奏，一套課程設計不可能完全適合每個學生。如果你行有餘力，目前線上有相當多各式各樣不同的線上學習資源，如[Codecademy][codecademy]、[Learnpython][learnpython]等等，或者在網路上各個部落格也都有相關資源，甚至也有免費的教科書。多試著和Python說說話，認識他/她的需要、個性、抱怨、牢騷，你們會漸漸變熟的。

[codecademy]: https://www.codecademy.com/learn/learn-python
[learnpython]: https://www.learnpython.org/

### 分享包容
寫程式、想問題是一種說故事的方法，每個人說的故事都不一樣。我們總會比較喜歡某些故事和比較不喜歡某些故事，可是這不影響他們的價值。如果你之前已經對程式語言很有經驗，但還是選擇來上這門課，就當作聽聽其他人說故事；若有機會，也歡迎分享自己的故事。

### 請配合課程要求
助教希望能夠幫助大家快快樂樂且充實地度過這個學期的課程。助教課、作業都請大家盡量配合參與。如果作業有問題，歡迎找助教幫忙。

作業繳交規定
----------

* 作業的主要目的是讓同學熟悉課程內容，並有實際的練習機會。但為了確認同學跟上課程進度節奏，請同學盡可能在每次上課前（週三17:00前），繳交上週作業。遲交作業以9折計分。
* 所有作業必須在第17週上課前繳交完成。請同學務必跟著每週的進度完成作業。一方面確保同學的學習節奏、另一方面愈到期末會愈累愈忙，為不耽誤同學其他的生活規劃，請及早完成作業。
* 作業原則上「認真寫」就會滿分，繳交的Python程式碼必須：
  * 是正確（valid）的程式碼，也就是不能有語法錯誤（syntax error）。
  * 試圖解決和作業需求相同的問題。
  * 不能和課堂所用的範例程式「完全相同」。
* 作業是輔助學習用的，希望這樣做能降低同學們初學程式的焦慮感，盡可能自由地嘗試和探索。但仍歡迎同學在作業中挑戰自己。挑戰自己的回饋不是（也不應是）作業成績，而是當你日以繼夜又挑燈夜戰跟Python奮戰至凌晨三四點終於「過了」的瞬間感動和成就。

