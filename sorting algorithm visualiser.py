import pygame #graphics
import random #generate list
import time #framerate


#generate list of random numbers
listOfNums = list()
def genList(array, length, lowerBound, upperBound):
    array.clear()
    for i in range(0, length):
        array.append(random.randint(lowerBound, upperBound))
    return array


#run window
def main():
    #initialise screen & game
    pygame.init()

    windowWidth = 1500
    windowHeight = 900
    window = pygame.display.set_mode((windowWidth, windowHeight))

    pygame.display.set_caption("algorithm")

    clock = pygame.time.Clock()

    running = True


    #bubblesort
    def bubblesort(list):
        #Swap the elements to arrange in order
        for iter_num in range(len(list)-1,0,-1):
            for idx in range(iter_num):
                if list[idx]>list[idx+1]:
                    temp = list[idx]
                    list[idx] = list[idx+1]
                    list[idx+1] = temp
                bar(len(list), windowWidth, windowHeight, 25, 12)


    #draw bars
    def bar(totalBars, windowWidthF, windowHeightF, margin, gap):
        window.fill((0, 0, 0))
        #constants
        barX = margin
        barW = (windowWidthF - margin * 2 - (totalBars * gap)) / totalBars
        R = 255
        G = 0
        B = 50
        for i in range(0, totalBars):
            pygame.event.get()
            #work out properties of bar
            barH = round(listOfNums[i] / maxList * (windowHeightF - (2 * margin)), 0) 
            barY = windowHeightF - margin - barH 
            #draw bar
            pygame.draw.rect(window, (R, G, B + 205 / totalBars * i), [(barX) + 4 + gap * i - 1 + barW * i - 1, barY, barW, barH]) 
            #update display
        pygame.display.update()


    #game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                window.fill((0, 0, 0))
                maxList = int(input("Max bar value: "))
                genList(listOfNums, int(input("Number of bars: ")), 1, maxList)
                bubblesort(listOfNums)
    

main()