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
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import resize  # Importing the resize function

# Load FITS files for each wavelength (red, green, blue)
red_data = fits.getdata('red_image.fits')
green_data = fits.getdata('green_image.fits')
blue_data = fits.getdata('blue_image.fits')

# Normalize pixel values between 0 and 1 for each color channel
red_data_normalized = (red_data - np.nanmin(red_data)) / (np.nanmax(red_data) - np.nanmin(red_data))
green_data_normalized = (green_data - np.nanmin(green_data)) / (np.nanmax(green_data) - np.nanmin(green_data))
blue_data_normalized = (blue_data - np.nanmin(blue_data)) / (np.nanmax(blue_data) - np.nanmin(blue_data))

# Replace NaN values with a default value (e.g., 0)
red_data_normalized = np.nan_to_num(red_data_normalized, nan=0)
green_data_normalized = np.nan_to_num(green_data_normalized, nan=0)
blue_data_normalized = np.nan_to_num(blue_data_normalized, nan=0)

# Check shapes of the arrays
print("Red shape:", red_data_normalized.shape)
print("Green shape:", green_data_normalized.shape)
print("Blue shape:", blue_data_normalized.shape)

# Resize red and blue images to match the shape of the green image
red_data_resized = resize(red_data_normalized, green_data_normalized.shape, mode='reflect')
blue_data_resized = resize(blue_data_normalized, green_data_normalized.shape, mode='reflect')

# Check the shapes after resizing
print("Resized Red shape:", red_data_resized.shape)
print("Resized Blue shape:", blue_data_resized.shape)

# Combine the color channels into an RGB image
if red_data_resized.shape == green_data_normalized.shape == blue_data_resized.shape:
    rgb_image = np.stack((red_data_resized, green_data_normalized, blue_data_resized), axis=-1)

    # Plot the RGB image with equatorial coordinates
    plt.figure(figsize=(8, 8))
    plt.imshow(rgb_image, origin='lower')  # Set origin to 'lower' for equatorial coordinates
    plt.xlabel('Right Ascension')
    plt.ylabel('Declination')
    plt.title('Hubble UDF - RGB Image')
    plt.colorbar(label='Intensity')
    plt.grid(color='white', linestyle='--', linewidth=0.5)
    plt.show()
else:
    print("Shapes of the resized arrays are not compatible for stacking into an RGB image.")
