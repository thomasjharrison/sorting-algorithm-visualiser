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

    windowWidth = 900
    windowHeight = 900
    window = pygame.display.set_mode((windowWidth, windowHeight))

    running = True


    #sorting algorithmns
    #bubblesort
    def bubbleSort(list):
        random.shuffle(list)
        global arrayComparisons
        arrayComparisons = 0
        limValue = len(list)
        for index in range(0, len(list)):
            for value in range(0, limValue - 1):
                if list[value] > list[value + 1]:
                    list[value + 1], list[value] = list[value], list[value + 1]
                arrayComparisons += 1
                updateScreen(listOfNums, [value])
            limValue -= 1
        updateScreen(listOfNums, [value])

    
    #selection sort
    def selectionSort(list):
        random.shuffle(list)
        global arrayComparisons
        arrayComparisons = 0
        for index in range(0, len(list)):
            minValue = index
            for value in range(index, len(list)):
                if list[minValue] > list[value]:
                    minValue = value
                arrayComparisons += 1
                updateScreen(listOfNums, [value, index])
            list[index], list[minValue] = list[minValue], list[index]
      

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
        #pygame.display.update()


    def selectBar(position, posList):
        pygame.draw.rect(window, (255, 255, 255), [posList[position][0], posList[position][1], posList[position][2], posList[position][3]])
        #pygame.display.update()


    def writeComparisons(var):
        font = pygame.font.Font("C:\Windows\Fonts\calibri.ttf", 40)
        rendered = font.render("Array Comparisons: {}".format(var), False, (255, 255, 255))
        window.blit(rendered, (20, 20))

    
    def updateScreen(list, index):
        bar(list, windowWidth, windowHeight, 30, 3, False)
        writeComparisons(arrayComparisons)
        for i in range(0, len(index)):
            selectBar(index[i], arrayOfPositions)
        time.sleep(0.01)
        pygame.display.update()


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

                sortType = input("Chose a sort: ")
                if sortType == "bubble":
                    bubbleSort(listOfNums)
                    pygame.display.set_caption("bubble sort algorithm")
                if sortType == "selection":
                    selectionSort(listOfNums)
                    pygame.display.set_caption("selection sort algorithm")
    

#run code
main()

'''
to do:
automate gap calculation
add more algorithms
'''