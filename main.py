import perlin_noise
import matplotlib.pyplot as plt
import mpl_toolkits
import numpy as np
import random

#Takes awhile to run

class terrain:
    __pic = []
    def __init__(self, xBound, yBound, scale, oct, seed):
        self.xBound = xBound
        self.yBound = yBound
        self.scale = scale
        self.oct = oct
        self.seed = seed
        noise = perlin_noise.PerlinNoise(octaves=self.oct, seed=self.seed)
        for i in range(self.xBound):
            row = []
            for j in range(self.yBound):
                noiseNumber = noise([j / self.xBound, i / self.yBound]) * self.scale
                if noiseNumber < 0.0:
                    noiseNumber = 0.0
                row.append(noiseNumber)
            self.__pic.append(row)

    def printNoise(self):
        print(self.__pic)

    def createShape(self):
        fig = plt.figure(figsize=(self.xBound, self.yBound))
        axes = fig.add_subplot(projection="3d")
        xArranged = np.arange(0, self.xBound, 1)
        yArranged = np.arange(0, self.yBound, 1)
        X, Y = np.meshgrid(xArranged, yArranged)
        Z = np.array(self.__pic)
        axes.set_zlim3d(0, 1)
        axes.plot_surface(X, Y, Z, cmap="terrain")
        plt.show()

    def colorTerrain(self):
        pass

def main():
    terrain1 = terrain(100, 100, 0.5, random.randint(1, 10), random.randint(1, 10))
    #terrain1.printNoise()
    terrain1.createShape()

    #plt.imshow(pic, cmap="gray")

if __name__ == '__main__':
    main()
