from random import randint
import pyxel
import time

#固定値
TILE_SIZE = 8     # タイルサイズ
MAP_WIDTH = 14    # 画面横サイズ
MAP_HEIGHT = 25   # 画面縦サイズ
WAIT = 12         # 待ち時間
BLACK_AREA = 7    #（黒）タイルマップの右下の図の、左から7番目が黒
WHITE_BLOCK = 10  #（白）タイルマップの右下の図の、左から10番目が白

class Tetris:
    # コンストラクタ
    def __init__(self):
        self.mGameover = False
        # ブロック番号（全部で７種類（0～6））
        self.mNextBlockNo = randint(0, 6)
        # x座標
        self.mX = 0
        # y座標
        self.mY = 0
        # 回転軸Ｎｏ（0 ～ 3）
        self.mRotaionNo = 0
        # 待ち時間
        self.mWait = 0

        # 初期設定
        pyxel.init(MAP_WIDTH * TILE_SIZE, MAP_HEIGHT * TILE_SIZE, scale=3, fps=10)
        # 設定ファイル（コマンドで参照可 → pyxeleditor tetris.pyxres)
        pyxel.load("tetris.pyxres")

        # テトリス音楽 再生
        pyxel.playm(0, loop=True)

        self.next()
        
        #実行（update関数 ⇒ draw関数 ⇒ update関数 ⇒ draw関数 ... と永遠とループする）
        pyxel.run(self.update, self.draw)
    
    # --------------------------------
    # 関数（画面描画）
    # --------------------------------
    def draw(self):
        # 画面（タイルマップ）
        pyxel.bltm(0, 0, 0, 0, 0, MAP_WIDTH, MAP_HEIGHT)
        # GAME OVER
        if self.mGameover: 
            pyxel.text(40, 80, "GAME OVER", 7)
    
    # --------------------------------
    # 関数（画面更新）
    # --------------------------------
    def update(self):
        # ゲームオーバー
        if self.mGameover:
            return
        # 待ち時間に到達した場合、Wait処理実行
        if self.mWait <= WAIT / 2:
            self.wait()
            return
        
        # 表示されているブロックを削除
        self.put(self.mX, self.mY, self.mT, self.mRotaionNo, True, True)
        
        #ここから更新 ↓↓↓
        # A座標取得(Xボタン、Zボタンで座標が切り替わっている事を考慮)
        mRotaionNo = self.getRotaionNo()
        if self.put(self.mX, self.mY, self.mT, mRotaionNo, False, False):
            # 移動できる場合は、座標をずらす
            self.mRotaionNo = mRotaionNo

        # X座標取得(左ボタン、右ボタンで座標が切り替わっている事を考慮)
        x = self.getMx()
        if self.put(x, self.mY, self.mT, self.mRotaionNo, False, False):
            # 移動できる場合は、座標をずらす
            self.mX = x

        # 一番下にブロックがあるか判定
        if self.put(x, self.mY + 1, self.mT, self.mRotaionNo, False, False):
            # 下にない場合は、Y座標を1つ下にさげる
            self.mY += 1
            self.mWait = WAIT
        else:
            self.mWait -= 1

        # 確定した座標で更新
        self.put(self.mX, self.mY, self.mT, self.mRotaionNo, False, True)
    
    # --------------------------------
    # 関数（回転軸Ｎｏ取得）
    # --------------------------------
    def getRotaionNo(self):
        mRotaionNo = self.mRotaionNo
        if pyxel.btnp(pyxel.KEY_X):
            pyxel.play(2, 11)
            mRotaionNo -= 1
        if pyxel.btnp(pyxel.KEY_Z):
            pyxel.play(2, 11)
            mRotaionNo += 1
        # 回転
        # mRotaionNo = 0 の場合 0
        # mRotaionNo = 1 の場合 1
        # mRotaionNo = 2 の場合 2
        # mRotaionNo = 3 の場合 3
        # mRotaionNo = 4 の場合 0
        # mRotaionNo = -1 の場合 3
        mRotaionNo &= 3
        return mRotaionNo;
    
    # --------------------------------
    # 関数（x座標取得）
    # --------------------------------
    def getMx(self):
        mX = self.mX
        # 左ボタンを押した場合
        if pyxel.btnp(pyxel.KEY_LEFT, 20, 1):
            mX -= 1
        # 右ボタンを押した場合
        if pyxel.btnp(pyxel.KEY_RIGHT, 20, 1):
            mX += 1
        return mX;

    # --------------------------------
    # 関数（ブロック設定）
    #
    # @param mX X座標
    # @param mY Y座標
    # @param mNextBlockNo 次ブロックNo
    # @param mA 回転軸ざ行
    # @param isEraseBlock ブロックを黒に潰す(True:黒固定、False:mNextBlockNoを設定)
    # @param isBlockSet ブロックを画面に設定(True:設定、False:未設定)
    # @return True:ブロック設定可能、False:ブロック設定不可能
    # --------------------------------
    def put(self, mX, mY, mNextBlockNo, mRotaionNo, isEraseBlock, isBlockSet):
        for j in range(4):
            for i in range(4):
                # 全反転パターン定義 詳しくは『並び替えアルゴリズム.xlsx』
                p = [ i, 3 -j, 3 - i,     j ]
                q = [ j,    i, 3 - j,  3 -i ]
                # 7(黒色の場合) 
                if pyxel.tilemap(0).get(16 + mNextBlockNo * 4 
                    + p[mRotaionNo], q[mRotaionNo]) == BLACK_AREA:
                    continue
                
                v = mNextBlockNo
                if isEraseBlock:
                    v = BLACK_AREA
                elif pyxel.tilemap(0).get( mX + i, mY + j) != BLACK_AREA:
                    # 移動後のブロックが7以外（何かしらのブラックがある）場合
                    return False;
                
                if isBlockSet:
                    pyxel.tilemap(0).set( mX + i, mY + j, v)
        return True
    
    # --------------------------------
    # 関数（次ブロック設定）
    # --------------------------------
    def next(self):
        self.mX = 5
        self.mY = 2
        self.mT = self.mNextBlockNo
        self.mWait = WAIT

        self.mRotaionNo = 0
        if pyxel.btn(pyxel.KEY_X):
            self.mRotaionNo = 3
        if pyxel.btn(pyxel.KEY_Z):
            self.mRotaionNo = 1
        
        #次に置くブロックが既におけない場合
        if self.put(self.mX, self.mY, self.mT, self.mRotaionNo, False, True) == False:
            # ゲームオーバー
            self.mGameover = True
        
        self.put(5, -1, self.mNextBlockNo, 0 , True, True)
        self.mNextBlockNo = randint(0, 6)
        self.put(5, -1, self.mNextBlockNo, 0 , False, True)

    # --------------------------------
    # 関数（横一列設定）
    #  横一列が埋まっていた場合は、"10"(横一列complete)を設定する
    # --------------------------------
    def set_row_line_Complete(self):
        # 上から下まで（22～3までループ）
        for y in range(22, 2, -1):
            n = 0
            # 横一列ループ
            for x in range(2, 12):
                if pyxel.tilemap(0).get(x, y) < 7:
                    n += 1
            # 横一列全て埋まった場合
            if n == 10:
                for x in range(2, 12):
                    # "10"（白）を設定 タイルマップの右下の図の、左から10番目が白
                    pyxel.tilemap(0).set(x, y ,WHITE_BLOCK)

    # --------------------------------
    # 関数（待機処理）
    # --------------------------------
    def wait(self):
        # mWaitを１減らす
        self.mWait -= 1

        # 時間オーバーの場合
        if self.mWait == 0:
            # 次へ
            self.next()

        # 初回（wait関数が呼ばれた、初回）の場合
        if self.mWait == WAIT / 2 - 1:
            # 横一列設定
            self.set_row_line_Complete()
        
        # 最終回（wait関数が呼ばれた、最後の回）の場合
        if self.mWait == 1:
            # 上から下まで（22～3までループ）
            for y in range(22, 2, -1):
                # 横一列が全てうまっていた場合
                while pyxel.tilemap(0).get(2, y) == WHITE_BLOCK:
                    
                    # 効果音再生
                    pyxel.play(2, 12)
                    self.mWait = WAIT / 2 -2

                    # ブロック消去
                    for i in range(y, 3, -1):
                        for x in range(2 ,12):
                            pyxel.tilemap(0).set(x, i, pyxel.tilemap(0).get(x, i -1))
                    for x in range(2, 12):
                        pyxel.tilemap(0).set(x, 3, 7)
    

#テトリス起動
Tetris()