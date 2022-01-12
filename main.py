import perlin_noise
import matplotlib.pyplot as plt
import mpl_toolkits
import numpy as np

#Takes awhile to run


class terrain:
    __pic = []
    def __init__(self, xBound, yBound, zBound, scale):
        self.xBound = xBound
        self.yBound = yBound
        self.zBound = zBound
        self.scale = scale
        noise = perlin_noise.PerlinNoise(octaves=10, seed=4)
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
        axes.plot_surface(X, Y, Z)
        plt.show()

    def colorTerrain(self):
        pass

def main():
    terrain1 = terrain(200, 200, 100, 0.25)
    #terrain1.printNoise()
    terrain1.createShape()

    #plt.imshow(pic, cmap="gray")

if __name__ == '__main__':
    main()
