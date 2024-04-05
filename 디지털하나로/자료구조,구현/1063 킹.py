import sys
input = sys.stdin.readline

king,stone,N = map(str,input().split())
N = int(N)
cmds = ['R','L','B','T','RT','LT','RB','LB']
dx = [0,0,-1,1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]

king_x,king_y,stone_x,stone_y = king[1],king[0],stone[1],stone[0]
for _ in range(N):
      cmd = input().rstrip()
      for i in range(8):
            if cmds[i] == cmd:
                  ky,kx = chr(ord(king_y)+dy[i]),int(king_x) + dx[i]
                  sy,sx = chr(ord(stone_y)+dy[i]),int(stone_x) + dx[i]
                  
                  if kx == int(stone_x) and ky == stone_y:
                        if 1<=sx<=8 and 'A'<=sy<='H':
                              stone_x,stone_y = sx,sy
                              king_x,king_y = kx,ky
                  elif 1<=kx<=8 and 'A'<=ky<='H':
                        king_x,king_y = kx,ky

print(king_y+str(king_x))
print(stone_y+str(stone_x))