import pygame
import time
import random

pygame.init()    #initializing pygame

display_width = 800
display_height = 600

black = (0,0,0)   #(R,G,B)
white = (255,255,255)
red = (255,0,0)

block_color1 = (53,115,225)
block_color2 = red

car_width = 80

# Making a window for game using pygame package

gameDisplay = pygame.display.set_mode((display_width,display_height))   # set the size of window 800 * 600


pygame.display.set_caption('Moti Racing Game')  # Name of top task bar

clock = pygame.time.Clock()    

carImg = pygame.image.load('mycar1_rsz.png')

def things_dodged(count):
    font =  pygame.font.SysFont(None, 25)
    text =  font.render("Dodged:"+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])   # Draw a box 



def car(x,y):
    gameDisplay.blit(carImg,(x,y))


def text_object(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_object(text,largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()     # update display to show on screen

    time.sleep(2)     # for 2 sec
    game_loop()     # restart the game again

def crash():
    message_display('You Crashed')

    
def game_loop():
    x = (display_width  *0.45)    #these dimension are important 
    y = (display_height *0.8)    

    x_change = 0
    thing_width = 100
    thing_startx = random.randrange(0, display_width-thing_width)    # object start in whole x width means randomly in x-direction
    thing_starty = -600   # 600 pixel above the screen (y=0 is top most point in left) 
    thing_speed =  3     # how fast pixel move 
    #thing_width =  100  #100 pixel object width
    thing_height = 100  # 100 * 100 box
    thing_count =  3    # number of things at a time
    dodged = 0  # starting dodge count
    gameExit = False   

    while not gameExit:

        for event in pygame.event.get():                       # this loop will hendle the movement (event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                #gameExit = True

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

        # things(thingx, thingy, thingw, thingh, color)
        #for i in  range(thing_count):
        things(thing_startx, thing_starty, thing_width, thing_height, block_color1)
        thing_starty += thing_speed     #moving in y-direction


        car(x,y)
        things_dodged(dodged)


        if x > display_width - car_width or x < 0:
            crash()
        
        if thing_starty > display_height:
            thing_starty = 0 - thing_height      # for continuous obstacles
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed +=  0.02 # speed of obstacle update with dodged
            thing_width  =  random.randrange(display_width/20, display_width/10) # randomly change width of obstacle
            #thing_width += (dodged * 1.2)    # obstacle width change with dodged count

        if y < thing_starty + thing_height: # thing_starty is point to the top left most pixel but we check collision from bottom most point thats why we are adding thing_height. this is y crossover.
            #print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                #if not (x + car_width < thing_startx or  x > thing_startx + thing_width):
                #print('x crossover')
                crash()
                #print(x)

        pygame.display.update()    # update the display in forground  or we can use .flip() instead of .update() both will work. this line itself tells that in our game nothing is moving actually the frame is updating each time like a flip book to give feeling of motion 

        clock.tick(60)     # refreshing or updating frequency (60 frames per second)

game_loop()      #calling game_loop function
pygame.quit()    # quit pygame

quit()     # quit python
