import util as u
class Draw_dh:
    def __init__(self,x,y,value,im=False):
        self.x=x
        self.y=y
        self.value=value
        self.len=0
        self.im=im
    def drawing(self,background):
        if self.im:
            background.blit(self.im,(self.x,self.y))
        else:
            u.text_draw(f"-{float(self.value)}",self.x,self.y,24,self.len,background,True)
    def move(self,deltatime):
        self.y-=deltatime*0.1
        self.len+=deltatime*0.1
        if self.len>=50:
            return True
        return False


