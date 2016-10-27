import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as ml

def contour_plot(x, y, z, nx=100, ny=100, interp='linear'):
    """
    Note grid interpolation can take a long time

    :param x:
    :param y:
    :param z:
    :param nx: How many x intervals in the z grid
    :param ny: How many y intervals in the z grid
    :param interp: Interpolation algorithm, either 'nn' for natural neighbor, or 'linear' for linear interpolation
    :return:
    """

    x_min, x_max = x.max(), x.min()
    y_min, y_max = y.max(), y.min()

    xi = np.linspace(x_min, x_max, nx)  # x grid intervals
    yi = np.linspace(y_min, y_max, ny)  # y grid intervals
    zi = ml.griddata(x, y, z, xi, yi, interp=interp)   # z grid

    plt.contour(xi, yi, zi, linewidths=0.5, colors='k')  # Contour line
    plt.pcolormesh(xi, yi, zi, cmap=plt.get_cmap('rainbow'))  # Colour map

    plt.colorbar() # Put the colour map last so the colorbar is of the color map and not the contour lines
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
