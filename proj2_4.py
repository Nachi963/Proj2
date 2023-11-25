#"""
#Multi-panel Image Plot

#This code segment demonstrates the creation of a multi-panel plot using Matplotlib. It loads a main image 
#('Hubble_UDF_RGB.png') using 'mpimg.imread', then generates subregion placeholders with random data to showcase 
#inset views within a 2x2 subplot grid.

#Dependencies:
#- matplotlib
#- numpy

#Note: Replace 'Hubble_UDF_RGB.png' with the path to your main image file.

#"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Load the main image using imread
image = mpimg.imread('Hubble_UDF_RGB.png')  # Replace 'Hubble_UDF_RGB.png' with your image file

# Placeholder data for subregions (replace with your actual data)
subregion_shape = (100, 100, 3)  # Define the shape of subregion images
subregion1 = np.random.rand(*subregion_shape)  # Random data for subregion 1
subregion2 = np.random.rand(*subregion_shape)  # Random data for subregion 2
subregion3 = np.random.rand(*subregion_shape)  # Random data for subregion 3
subregion4 = np.random.rand(*subregion_shape)  # Random data for subregion 4

# Create a main figure and subplot grid
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

# Plot the main image in the central subplot
ax[0, 0].imshow(image)
ax[0, 0].set_title('Hubble_UDF_RGB')

# Plot insets in other subplots
ax[0, 1].imshow(subregion1)
ax[0, 1].set_title('Inset 1')

ax[1, 0].imshow(subregion2)
ax[1, 0].set_title('Inset 2')

ax[1, 1].imshow(subregion3)
ax[1, 1].set_title('Inset 3')

# Adjust layout to prevent overlap
plt.tight_layout()

# Add annotations for clarity
ax[0, 0].annotate('(a)', xy=(0.1, 0.9), xycoords='axes fraction', fontsize=12)
ax[0, 1].annotate('(b)', xy=(0.1, 0.9), xycoords='axes fraction', fontsize=12)
ax[1, 0].annotate('(c)', xy=(0.1, 0.9), xycoords='axes fraction', fontsize=12)
ax[1, 1].annotate('(d)', xy=(0.1, 0.9), xycoords='axes fraction', fontsize=12)

# Show the plot
plt.show()
