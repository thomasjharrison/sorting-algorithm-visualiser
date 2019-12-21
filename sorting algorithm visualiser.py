import pygame #graphics
import random #generate list
import time #framerate


#generate list of random numbers
listOfNums = list()
def genListRandom(array, length, lowerBound, upperBound):
    array.clear()
    for i in range(0, length):
        array.append(random.randint(lowerBound, upperBound))
    return array


#generate list of ascending numbers
def genListAsc(array, length):
    array.clear()
    for i in range(1, length):
        array.append(i)
    return array


#run window
def main():
    #initialise screen & game
    pygame.init()

    windowWidth = 1600
    windowHeight = 900
    window = pygame.display.set_mode((windowWidth, windowHeight))

    pygame.display.set_caption("algorithm")

    running = True


    
    #bubblesort
    def bubblesort(list):
        #Swap the elements to arrange in order
        random.shuffle(list)
        arrayComparisons = 0
        for iter_num in range(len(list)-1,0,-1):
            for idx in range(iter_num):
                if list[idx]>list[idx+1]:
                    temp = list[idx]
                    list[idx] = list[idx+1]
                    list[idx+1] = temp
                arrayComparisons += 1
                    
                bar(list, windowWidth, windowHeight, 25, 2, False)
                writeComparisons(arrayComparisons)
                selectBar(idx + 1, arrayOfPositions)
                time.sleep(0.0005)
        bar(list, windowWidth, windowHeight, 25, 2, False)

    #draw bars function
    def bar(list, windowWidthF, windowHeightF, margin, gap, debug):

        #clear screen
        window.fill((0, 0, 0))

        #constants
        totalBars = len(list)
        barX = margin + 4
        barW = (windowWidthF - margin * 2 - (totalBars * gap)) / totalBars
        R = 255
        G = 0
        B = 50
        global arrayOfPositions
        arrayOfPositions = []

        #print values for debugging
        if debug == True:
            print("totalBars = {}".format(totalBars))
            print("barX = {}".format(barX))
            print("gap = {}".format(gap))
            print("barW = {}".format(barW))
        
        #cycle through list of nums, print the bar
        for i in range(0, totalBars):
            pygame.event.get()
            #work out properties of bar
            barH = round(list[i] / maxList * (windowHeightF - (2 * margin)), 0) 
            barY = windowHeightF - margin - barH 
            #draw bar
            pygame.draw.rect(window, (R, G, B + 205 / totalBars * i), [(barX) + gap * i - 1 + barW * i - 1, barY, barW, barH]) 
            arrayOfPositions.append((barX + gap * i - 1 + barW * i - 1, barY, barW, barH))

        #update display
        pygame.display.update()


    def selectBar(position, posList):
        pygame.draw.rect(window, (255, 255, 255), [posList[position][0], posList[position][1], posList[position][2], posList[position][3]])
        pygame.display.update()


    def writeComparisons(var):
        font = pygame.font.Font("C:\Windows\Fonts\calibri.ttf", 50)
        rendered = font.render("Array Accesses: {}".format(var), False, (255, 255, 255))
        window.blit(rendered, (20, 20))


    #event loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                window.fill((0, 0, 0))

                listType = input("Input asc for ascending, rnd for random list: ").lower()
                if listType == "rnd":
                    maxList = int(input("Max bar value: "))
                    genListRandom(listOfNums, int(input("Number of bars: ")), 1, maxList)
                elif listType == "asc":
                    maxList = int(input("Largest value: "))
                    random.shuffle(genListAsc(listOfNums, maxList))

                
                bubblesort(listOfNums)
    

#run code
main()

'''
to do:
automate gap calculation
add more algorithms
'''