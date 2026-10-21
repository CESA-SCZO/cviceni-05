# -*- coding: utf-8 -*-

'Import knihoven'
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft2, ifft2, fftshift,ifftshift
from scipy.ndimage import gaussian_filter
from scipy.signal import convolve2d,medfilt2d
from skimage.util import random_noise
from skimage.color import rgb2gray
from skimage.io import imread

plt.close('all')

def plot_3D(number_of_rows, number_of_columns, position_of_plot, original_image_shape, information_to_visualise, title = '', x_label = '', y_label = ''):
    '''
    Function for 3D visualisation of provided values.

    :param number_of_rows: (int) number of subplot rows in figure
    :param number_of_columns: (int) number of subplot columns in figure
    :param position_of_plot: (int) position of generated subplot in figure
    :param original_image_shape: (tuple) shape of original image
    :param information_to_visualise: (numpy.ndarray) 2D array of values to be visualised
    :param title: (str) plot title
    :param x_label: (str) label on x axis
    :param y_label: (str) label on x axis
    :return: 3D visualisation of provided values
    '''
    X, Y = np.meshgrid(np.arange(0,original_image_shape[1]), np.arange(0,original_image_shape[0]))

    ax = plt.subplot(number_of_rows,number_of_columns,position_of_plot, projection= '3d')
    ax.plot_surface(X = X, Y= Y, Z= information_to_visualise, cmap = 'jet')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    return()

#%% Ukol 1
# =============================================================================
# Nactete obraz 'basket.jpg‘ a prevedte na sedotonovy obraz.
# Vytvorte obraz o velikosti nacteneho obrazu obsahujici pouze aditivni gaussovsky sum s nulovou strední hodnotou a rozptylem 0.3 (np.random.normal())
# Zobrazte si vytvoreny sum spolu s jeho amplitudovym spektrem (vyuzijte k tomu prilozenou funkci 'plot_3D()') a histogramem
# Zasumte obraz Vami vytvorenym gaussovskym sumem
# Zobrazte si do jednoho okna originalni obraz, jeho zasumenou variantu a odpovidsajici histogramy 
# Mente parametry sumu a pozorujte, jaky maji vliv na vysledny obraz. Zobrazte si zaroven jeho spektrum a histogram sumu
# =============================================================================
plt.close('all')




#%% Ukol 2
# =============================================================================
# Nactete obraz 'basket.jpg‘ a prevedte na sedotonovy obraz.
# Zasumte tento obraz impulznim sumem s hustotou zasumeni 0.3 (random_noise())
# Zobrazte si zasumeny obraz spolu s jeho amplitudovym spektrem (vyuzijte k tomu prilozenou funkci 'plot_3D()') a histogramem
# Ziskejte obraz pouze pouziteho impulsniho sumu 
# Zobrazte si obraz impulsniho sumu spolu s jeho amplitudovym spektrem (vyuzijte k tomu prilozenou funkci 'plot_3D()') a histogramem
# Mente parametry sumu a pozorujte, jaky maji vliv na vysledny obraz. Zobrazte si zaroven spektrum a histogram jak obrazu, tak sumu
# =============================================================================
plt.close('all')




#%% Ukol 3
# =============================================================================
# Definujte impulsni charakteristiky prumerujicich konvolucnich masek o velikostech 3x3, 7x7, 11x11.
# Definujte impulsni charakteristiky gaussovskeho filtru (gaussian_filter()) s rozptylem 3, 7 a 11
# Zobrazte amplitudovou frekvencni charakteristiku jednotlivych filtru.
# Pomoci definovanych prumerujicich masek filtrujte ten zasumeny obraz, ktereho sum lze potlacit pomoci prumerovani
# Pomoci medianove filtrace s maskou o velikosti 3x3 filtrujte ten zasumeny obraz, ktereho sum lze potlacit pomoci teto filtrace 
# Mente velikost masky a pozorujte, jaky maji vliv na vysledny obraz
# =============================================================================
plt.close('all')



#%% Ukol 4
# =============================================================================
# Najdete a stahnete si obrazek Vasho favorita (vybirejte obrazek do velikosti 500x500, pripadne jej na tuto velikost podvzorkujte)
# Vygenerujte dvourozmernou harmonickou funkci s parametry A=1, u=8, v=13, phi=0. 
# Pomoci vygenerovane harmonicke funkce zasumte Vami vybrany obraz favorita sumem moire
# Zobrazte spektra jak originalniho, tak zasumeneho favorita
# Odstrante uzkopasmovy sum obrazku pomoci nulovani danych frekvenci ve spektru
# Zobrazte zasumeny a vyfiltrovany obraz spolu s jejich amplitudovymi spektry. 
# =============================================================================
plt.close('all')

def create_harmonic_function(sf_u,sf_v,phase,amplitude,img_shape):
    """
    Generates a 2D harmonic function with provided parameters

    :param sf_u: (int, float) spatial frequency in y axis
    :param sf_v: (int, float) spatial frequency in x axis
    :param phase: (int, float) phase
    :param amplitude: (int, float) amplitude
    :param img_shape: (tuple) shape of the image in x and y direction
    :return: (numpy.ndarray) Array of generated 2D harmonic function
    """

    n, m = img_shape
    omega_u = 2 * np.pi * sf_u
    omega_v = 2 * np.pi * sf_v

    [N, M] = np.meshgrid(range(m), range(n))
    harmonic_function = amplitude * np.cos((omega_u * N) / n + (omega_v * M) / m + phase)
    return(harmonic_function)


