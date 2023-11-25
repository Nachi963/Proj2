#RGB Image Generation from FITS Data

#This code snippet processes FITS files containing red, green, and blue wavelength data to create an RGB image
#representing the Hubble Ultra Deep Field (HUDF). It involves loading, normalization, resizing, and combining the
#color channels to generate the final RGB image.

#Dependencies:
#- astropy
#- numpy
#- matplotlib
#- skimage

#Note: Ensure FITS files 'red_image.fits', 'green_image.fits', and 'blue_image.fits' exist in the working directory.

#"""
import logging
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import resize

logging.basicConfig(filename='rgb_image_generation.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def load_fits_data(file_path):
    logging.info(f"Loading FITS file: {file_path}")
    data = fits.getdata(file_path)
    return data

def normalize_data(data):
    logging.info("Normalizing pixel values between 0 and 1")
    normalized_data = (data - np.nanmin(data)) / (np.nanmax(data) - np.nanmin(data))
    return np.nan_to_num(normalized_data, nan=0)

def resize_data(data, target_shape):
    logging.info("Resizing data to match target shape")
    return resize(data, target_shape, mode='reflect')

def combine_channels(red, green, blue):
    logging.info("Combining color channels into an RGB image")
    return np.stack((red, green, blue), axis=-1)

def plot_rgb_image(rgb_image):
    plt.figure(figsize=(8, 8))
    plt.imshow(rgb_image, origin='lower')
    plt.xlabel('Right Ascension')
    plt.ylabel('Declination')
    plt.title('Hubble UDF - RGB Image')
    plt.colorbar(label='Intensity')
    plt.grid(color='white', linestyle='--', linewidth=0.5)
    plt.show()

try:
    red_data = load_fits_data('red_image.fits')
    green_data = load_fits_data('green_image.fits')
    blue_data = load_fits_data('blue_image.fits')

    red_normalized = normalize_data(red_data)
    green_normalized = normalize_data(green_data)
    blue_normalized = normalize_data(blue_data)

    logging.info("Shapes of the normalized arrays")
    logging.info(f"Red shape: {red_normalized.shape}")
    logging.info(f"Green shape: {green_normalized.shape}")
    logging.info(f"Blue shape: {blue_normalized.shape}")

    target_shape = green_normalized.shape
    red_resized = resize_data(red_normalized, target_shape)
    blue_resized = resize_data(blue_normalized, target_shape)

    logging.info("Shapes after resizing")
    logging.info(f"Resized Red shape: {red_resized.shape}")
    logging.info(f"Resized Blue shape: {blue_resized.shape}")

    if red_resized.shape == green_normalized.shape == blue_resized.shape:
        rgb_image = combine_channels(red_resized, green_normalized, blue_resized)
        plot_rgb_image(rgb_image)
    else:
        logging.error("Shapes of the resized arrays are not compatible for stacking into an RGB image.")

except Exception as e:
    logging.exception(f"An error occurred: {str(e)}")

