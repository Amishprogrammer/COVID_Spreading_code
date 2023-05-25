import json

class Grid:
    whole=[]
    row=0
    col=0
    def __init__(self,x,y):
        self.row=x
        self.col=y
        while y:
            self.whole.append(['O' for i in range(x)])
            y-=1
    def __repr__(self):
        return str(self.whole)
    def infection(self,xx,yy):
        self.whole[row-yy-1][xx]='X'
    def output(self):
        return self.whole
    
    
class person(Grid):
    def __init__(self,x,y,side,movements):
        self.face=side
        self.x=x
        self.y=y
        if self.face=='N':
            self.face_num=1
        elif self.face=='E':
            self.face_num=2
        elif self.face=='W':
            self.face_num=0
        elif self.face=='S':
            self.face_num=3
        for i in movements:
            
            if i=='L':
                self.face_num=abs((self.face_num-1)%4)
            elif i=='R':
                self.face_num=abs((self.face_num+1)%4)
            elif i=='F':
                
                if Grid.whole[Grid.row-1-self.y][self.x]=='X':
                    
                    if self.face_num==0:
                        self.x-=1
                        
                        Grid.whole[Grid.row-1-self.y][self.x]='X'
                    elif self.face_num==2:
                        self.x+=1
                        
                        Grid.whole[Grid.row-1-self.y][self.x]='X'
                    elif self.face_num==1:
                        self.y+=1
                        
                        Grid.whole[Grid.row-1-self.y][self.x]='X'
                    elif self.face_num==3:
                        self.y-=1
                        
                        Grid.whole[Grid.row-1-self.y][self.x]='X'
                elif Grid.whole[Grid.row-1-self.y][self.x]=='O':
                    if self.face_num==0:
                        self.x-=1
                        
                    elif self.face_num==2:
                        self.x+=1
                        
                    elif self.face_num==1:
                        self.y+=1
                        
                    elif self.face_num==3:
                        self.y-=1
                        
                        

data=input()
dictdata=json.loads(data)


grid=Grid(dictdata["grid"]["length"],dictdata["grid"]["breath"])

for i in dictdata["infectedCells"]:
    x=i["x"]
    y=i["y"]
    grid.infection(x,y)


for i in dictdata["persons"]:
    xpos=int(i["initialPosition"][0])
    ypos=int(i["initialPosition"][2])
    direction=i["initialPosition"][4]
    movement=i["movement"]
    A1=person(xpos,ypos,direction,movement)
    
for x in grid.whole:
    string=""
    for y in x:
        string+=y
    print(string)
