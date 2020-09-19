from random import randint
import pyxel
import time

#タイルサイズ
TILE_SIZE = 8
#画面横サイズ
MAP_WIDTH = 14
#画面縦サイズ
MAP_HEIGHT = 25
#待ち時間
WAIT = 20

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
        self.mA = 0
        # 待ち時間
        self.mWait = 0

        # 初期設定
        pyxel.init(MAP_WIDTH * TILE_SIZE, MAP_HEIGHT * TILE_SIZE, scale=3, fps=10)
        pyxel.load("tetris.pyxres")

        # テトリス音楽 再生
        pyxel.playm(0, loop=True)

        self.next()
        
        #実行（update関数 ⇒ draw関数 ⇒ update関数 ⇒ draw関数 ... と永遠とループする）
        pyxel.run(self.update, self.draw)
    
    # ---------------
    # 関数（画面描画）
    # ---------------
    def draw(self):
        # 画面（タイルマップ）
        pyxel.bltm(0, 0, 0, 0, 0, MAP_WIDTH, MAP_HEIGHT)
        # GAME OVER
        if self.mGameover: 
            pyxel.text(40, 80, "GAME OVER", 7)
    
    # ---------------
    # 関数（画面更新）
    # ---------------
    def update(self):
        # ゲームオーバー
        if self.mGameover:
            return
        if self.mWait <= WAIT / 2:    
            self.wait()
            return
        
        self.put(self.mX, self.mY, self.mT, self.mA, False, True)
        
        a = self.mA
        if pyxel.btnp(pyxel.KEY_X):
            pyxel.play(2, 11)
            a -= 1
        if pyxel.btnp(pyxel.KEY_Z):
            pyxel.play(2, 11)
            a += 1
        a &= 3
        if self.put(self.mX, self.mY, self.mT, a, True, False):
            self.mA = a
        
        x = self.mX
        # 左ボタンを押した場合
        if pyxel.btnp(pyxel.KEY_LEFT, 20, 1):
            x -= 1
        # 右ボタンを押した場合
        if pyxel.btnp(pyxel.KEY_RIGHT, 20, 1):
            x += 1
        if self.put(x, self.mY, self.mT, self.mA, True, False):
            self.mX = x
        
        # 一番下にブロックがあるか判定
        if self.put(x, self.mY + 1, self.mT, self.mA, True, False):
            self.mY += 1
            self.mWait = WAIT
        else:
            self.mWait -= 1

        self.put(self.mX, self.mY, self.mT, self.mA, True, True)
    
    # ---------------
    # 関数（ブロック設定）
    #
    # @param mX X座標
    # @param mY Y座標
    # @param mNextBlockNo 次ブロックNo
    # @param mA
    # @param s
    # @param isBlockSet ブロックを画面に設定(True:設定、False:未設定)
    # ---------------
    def put(self, mX, mY, mNextBlockNo, mA, s, isBlockSet):
        for j in range(4):
            for i in range(4):
                p = [ i, 3 -j, 3 - i,     j ]
                q = [ j,    i, 3 - j,  3 -i ]
                if pyxel.tilemap(0).get(16 + mNextBlockNo * 4 + p[mA], q[mA]) == 7:
                    continue
                v = mNextBlockNo
                if s == False:
                    v = 7
                elif pyxel.tilemap(0).get( mX + i, mY + j) != 7:
                    return False;
                
                if isBlockSet:
                    pyxel.tilemap(0).set( mX + i, mY + j, v)
        return True
    
    # --------------------
    # 関数（次ブロック設定）
    # --------------------
    def next(self):
        self.mX = 5
        self.mY = 2
        self.mT = self.mNextBlockNo
        self.mWait = WAIT

        self.mA = 0
        if pyxel.btn(pyxel.KEY_X):
            self.mA = 3
        if pyxel.btn(pyxel.KEY_Z):
            self.mA = 1
        
        if self.put(self.mX, self.mY, self.mT, self.mA, True, True) == False:
            self.mGameover = True
        
        self.put(5, -1, self.mNextBlockNo, 0 , False, True)
        self.mNextBlockNo = randint(0, 6)
        self.put(5, -1, self.mNextBlockNo, 0 , True, True)

    # --------------------------
    # 関数（横一列設定）
    #  横一列が埋まっていた場合は、"10"(横一列complete)を設定する
    # --------------------------
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
                    # "10"を設定
                    pyxel.tilemap(0).set(x, y ,10)

    # ---------------
    # 関数（待機処理）
    # ---------------
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
                while pyxel.tilemap(0).get(2, y) == 10:
                    
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