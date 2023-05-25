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
                        
                        
                        
    
row=int(input("Enter the row: "))
col=int(input("enter the columns: "))
grid=Grid(row,col)
i=int(input("How many initial locations are infected??? "))
while i:
    x=int(input("Enter the xth value: "))
    y=int(input("Enter the yth value: "))
    grid.infection(x,y)
    i-=1

how_many=int(input("How many people are there to observe: "))
for i in range(how_many):
    xpos=int(input("X axis position: "))
    ypos=int(input("Y axis position: "))
    direction=input("GIVE THE DIRECTION THE PERSON IS FACING ")
    movement=input("Enter the movement series: ")
    A1=person(xpos,ypos,direction,movement)
    
for x in grid.whole:
    string=""
    for y in x:
        string+=y
    print(string)