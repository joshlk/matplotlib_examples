import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

def contour_density_plot(x, y, nx=100, ny=100):

    x_min, x_max = x.max(), x.min()
    y_min, y_max = y.max(), y.min()

    # Convert to imaginary number (dont know why it needs to be)
    nx, ny = complex(0, nx), complex(0, ny)

    # Peform the kernel density estimate
    xx, yy = np.mgrid[x_min:x_max:nx, y_min:y_max:ny]
    positions = np.vstack([xx.ravel(), yy.ravel()])
    values = np.vstack([x, y])
    kernel = st.gaussian_kde(values)
    f = np.reshape(kernel(positions).T, xx.shape)

    # Create figure
    plt.contour(xx, yy, f, colors='k')  # Contour lines
    plt.contourf(xx, yy, f, cmap=plt.get_cmap('rainbow'))   # Colour map

    plt.colorbar()  # Put the colour map last so the colorbar is of the colour map and not the contour lines
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

