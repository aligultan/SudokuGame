import pygame
import requests

#setting up the width and the background color of the window
WIDTH=550
bg = (38,38,38)
o_color=(255,255,255)
buffer = 5

#adding the API in our Sudoku Game

res = requests.get("http://sugoku.herokuapp.com/board?difficulty=easy")
grid = res.json(['board'])
original_grid = [[grid[x][y]for y in range(len(grid[0]))] for x in range (len(grid))]

#Adding the functionality that can add the number on user bases

def insert(win,position):
    i,j=position[1],position[0]
    #add the font and the size
    myfont = pygame.font.SysFont('Comic Sans Ms',35)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type==pygame.KEYDOWN:
                if(grid.original[i-1][j-1]!=0):
                    return
                if (event.key==48 ):
                    grid[i-1][j-1]=event.key - 48
                    pygame.draw.rect(win,bg,(position[0]*50+buffer,position[1]*50+buffer,50-2*buffer,50-2*buffer))
                    pygame.display.update()
                    return
                if (0< event.key-48 <10):
                    #checking for valid input entered by your keyboard
                    pygame.draw.rect(win,bg,(position[0]*50+buffer,position[0]*50+buffer,50-2*buffer,50 - 2*buffer))

                    value = myfont.render(str(event.key-48),True,(179,179,179))
                    win.blit(value,(position[0]*50+15,
                                    position[1]*50))
                    grid[i-1][j-1]=event.key-48
                    pygame.display.update()
                    return
                return

#Initalizing pygame

def main():
    pygame.init()
    win=pygame.display.set_mode((WIDTH,WIDTH))
    pygame.display.set_caption("*Sudoku Game*")
    win.fill(bg)
    myFont=pygame.font.SysFont('Comic Sans MS',35)
    #let us create the grid

    for i in range(0,10):
        if(i%3==0):
            #Drawing Horizontal lines
            pygame.draw.line(win,(255,255,255),(50+50*i,50),4)
            pygame.draw.line(win, (255, 255, 255), (50 , 50 +50*i),(500,50+50*i),4)

        #Drawing vertical lines
        pygame.draw.line(win,(166,166,166),(50+50*i,50),(50+50*i,500),2)
        pygame.draw.line(win, (166, 166, 166), (50 ,50+50*i),(500,50+50*i),2)
    pygame.display.update()

    for i in range(0,len(grid[0])):
        for j in range(0,len(grid[0])):
            if(0<grid[i][j]<10):
                value=myFont.render(str(grid[i][j]),True,original_grid)
                win.blit(value,((j+1)*50+15,(i+1)*50))
    pygame.display.update()

#add the function that if we press the quit key ,pygame window will close [X]
    while True:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONUP and event.button==1:
                pos=pygame.mouse.get_pos()
                insert(win,(pos[0//50,pos[1]//50]))
            if event.type==pygame.QUIT:
                pygame.quit()
                return
#invoke the main function
main()










