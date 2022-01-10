import perlin_noise
import matplotlib.pyplot as plt

#Takes awhile to run



def main():

    noise = perlin_noise.PerlinNoise(octaves=12, seed=5)
    scale = 0.1
    x, y, = 256, 256
    pic = []
    for i in range(x):
        row = []
        for j in range(y):
            row.append(noise([j/x, i/y]) * scale)
        pic.append(row)
    plt.imshow(pic, cmap="gray")
    plt.show()

if __name__ == '__main__':
    main()
