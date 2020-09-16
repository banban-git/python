from random import randint
import pyxel

TILE_SIZE = 8
MAP_WIDTH = 14
MAP_HEIGHT = 25
WAIT = 60

class Tetris:
    def __init__(self):
        self.mGameover = False
        self.mNext = randint(0, 6)
        self.mX = 0
        self.mY = 0
        self.mA = 0
        self.mWait = 0

        pyxel.init(MAP_WIDTH * TILE_SIZE, MAP_HEIGHT * TILE_SIZE, scale=3, fps=15)
        pyxel.load("tetris.pyxres")

        self.next()
        
        pyxel.run(self.update, self.draw)
    def update(self):
        # ゲームオーバーの場合
        if self.mGameover:
            # 終了
            return
        if self.mWait <= WAIT / 2:
            self.wait()
            return
        
        self.put(self.mX, self.mY, self.mT, self.mA, False, False)
        #self.put(self.mX, self.mY, self.mT, self.mA, True, False)
        a = self.mA
        if pyxel.btnp(pyxel.KEY_X):
            a -= 1
        if pyxel.btnp(pyxel.KEY_Z):
            a += 1
        a &= 3
        if self.put(self.mX, self.mY, self.mT, a, True, True):
            self.mA = a
        
        x = self.mX
        if pyxel.btnp(pyxel.KEY_LEFT, 20, 1):
            x -= 1
        if pyxel.btnp(pyxel.KEY_RIGHT, 20, 1):
            x += 1
        if self.put(x, self.mY, self.mT, self.mA, True, True):
            self.mX = x
        
        if self.put(x, self.mY + 1, self.mT, self.mA, True, True):
            self.mY += 1
            self.mWait = WAIT
        else:
            self.mWait -= 1

        self.put(self.mX, self.mY, self.mT, self.mA, True, False)

    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, MAP_WIDTH, MAP_HEIGHT)
        if self.mGameover:
            pyxel.text(40, 80, "GAME OVER", 7)
    def put(self, x, y, t, a, s, test):
        for j in range(4):
            for i in range(4):
                p = [ i, 3 -j, 3 - i,     j ]
                q = [ j,    i, 3 - j,  3 -i ]
                if pyxel.tilemap(0).get(16 + t * 4 + p[a], q[a]) == 7:
                    continue
                v = t
                if s == False:
                    v = 7
                elif pyxel.tilemap(0).get( x + i, y + j) != 7:
                    return False;
                if test == False:
                    pyxel.tilemap(0).set( x + i, y + j, v)
        return True
    def next(self):
        self.mX = 5
        self.mY = 2
        self.mT = self.mNext
        self.mWait = WAIT

        self.mA = 0
        if pyxel.btn(pyxel.KEY_X):
            self.mA = 3
        if pyxel.btn(pyxel.KEY_Z):
            self.mA = 1
        
        if self.put(self.mX, self.mY, self.mT, self.mA, True, False) == False:
            self.mGameover = True
        
        self.put(5, -1, self.mNext, 0 , False, False)
        self.mNext = randint(0, 6)
        self.put(5, -1, self.mNext, 0 , True, False)
    def wait(self):
        self.mWait -= 1
        if self.mWait == 0:
            self.next()
        
        if self.mWait == WAIT / 2 - 1:
            for y in range(22, 2, -1):
                n = 0
                for x in range(2, 12):
                    if pyxel.tilemap(0).get(x, y) < 7:
                        n += 1
                if n != 10:
                    continue
                for x in range(2, 12):
                    pyxel.tilemap(0).set(x, y ,10)
        
        if self.mWait == 1:
            for y in range(22, 2, -1):
                while pyxel.tilemap(0).get(2, y) == 10:
                    self.mWait = WAIT / 2 -2
                    for i in range(y, 3, -1):
                        for x in range(2 ,12):
                            pyxel.tilemap(0).set(x, i, pyxel.tilemap(0).get(x, i -1))
                    for x in range(2, 12):
                        pyxel.tilemap(0).set(x, 3, 7)
#テトリス起動
Tetris()
