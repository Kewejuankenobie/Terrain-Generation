import perlin_noise
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import random
import tkinter


#Creates terrain object
class terrain:
    __pic = []
    fig = None
    axes = None
    def __init__(self, xBound, yBound, scale, oct, seed):
        self.xBound = xBound
        self.yBound = yBound
        self.scale = scale
        self.oct = oct
        self.seed = seed
        self.__pic = []
        #Creates noise function from perlin noise
        noise = perlin_noise.PerlinNoise(octaves=self.oct, seed=self.seed)
        #Creates a 2D array based on the noise and position within the x and y bounds
        for i in range(self.xBound):
            row = []
            for j in range(self.yBound):
                noiseNumber = noise([j / self.xBound, i / self.yBound]) * self.scale
                noiseNumber += 0.1
                #Removes unrealistic vallies that make it look unrealistic
                if noiseNumber < 0.0:
                    noiseNumber = 0.0
                row.append(noiseNumber)
            self.__pic.append(row)
        #Created the Graph figure and 3d axes
        self.fig = plt.figure(figsize=(self.xBound, self.yBound), num="exists")
        self.axes = self.fig.add_subplot(projection="3d")

    #Prints the noise Array
    def printNoise(self):
        print(self.__pic)

    #Creates the visual 3d terrain
    def createShape(self):
        xArranged = np.arange(0, self.xBound, 1)
        yArranged = np.arange(0, self.yBound, 1)
        X, Y = np.meshgrid(xArranged, yArranged)
        #The Z value equals the noise values, usually between -1 and 1
        Z = np.array(self.__pic)
        #The highest z value shown, makes terrain look better
        self.axes.set_zlim3d(0, 1)
        #Plots the terrain with a terrain color map
        self.axes.plot_surface(X, Y, Z, cmap="terrain")
        plt.draw()
        #Only does this if a terrain has not been created yet
        if len(terrainList) == 1:
            canvas = FigureCanvasTkAgg(self.fig, master=window)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=True)
#End of terrain class

#Generates new terrain by instancing a new terrain object, and adds it to a terrain list so the last in the list is created
def generateNew():
    ter = terrain(100, 100, 0.5, random.randint(3, 8), random.randint(1, 10))
    terrainList.append(ter)
    terrainList[-1].createShape()

#When the generate terrain button is pressed, it removes unessisary terrain from the terrain list and generates new terrain
def onClick():
    if len(terrainList) > 2:
        terrainList.remove(terrainList[0])
    generateNew()

#When the exit button is pressed, the program is closed
def exitPgm():
    window.destroy()
    exit()

def main():
    #Global variables that everything can access
    global window
    global canvas
    global terrainList
    #Creates window and the terrain list
    window = tkinter.Tk()
    terrainList = []

    window.geometry("1000x800")
    #Creates and places buttons in program, and adds functionality to them
    button = tkinter.Button(window, text="Generate Terrain", command=onClick)
    button.pack(side=tkinter.TOP)
    buttonEx = tkinter.Button(window, text="Exit", command=exitPgm)
    buttonEx.pack(side=tkinter.TOP)
    window.mainloop()

if __name__ == '__main__':
    main()
