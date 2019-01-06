import pygame

pygame.init()    #initializing pygame

display_width = 800
display_height = 600

black = (0,0,0)   #(R,G,B)
white = (255,255,255)
red = (255,0,0)


# Making a window for game using pygame package

gameDisplay = pygame.display.set_mode((display_width,display_height))   # set the size of window 800 * 600


pygame.display.set_caption('Moti Racing Game')  # Name of top task bar

clock = pygame.time.Clock()    

carImg = pygame.image.load('MyCarNew.png')

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

x = (display_width  *0.45)    #these dimension are important 
y = (display_height *0.8)    

x_change = 0

crashed = False   

while not crashed:

    for event in pygame.event.get():                       # this loop will hendle the movement 
        if event.type == pygame.QUIT:
            crashed = True

        if event.type  == pygame.KEYDOWN:  #this mean a key is pressed
            if event.key == pygame.K_LEFT:
                x_change = -5

            elif event.key == pygame.K_RIGHT:
                x_change = 5


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0


        #print(event) 
    x +=  x_change 
    gameDisplay.fill(white)   #this must be done before displaying car otherwise car will be gone
    car(x,y)
    pygame.display.update()    # update the display in forground  or we can use .flip() instead of .update() both will work. this line itself tells that in our game nothing is moving actually the frame is updating each time like a flip book to give feeling of motion 

    clock.tick(60)     # refreshing or updating frequency (60 frames per second)


pygame.quit()    # quit pygame

quit()     # quit python
