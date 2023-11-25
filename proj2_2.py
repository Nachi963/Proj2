#"""
#Galaxy Catalog Visualization and Redshift Analysis

#This code segment focuses on loading and visualizing data related to the Hubble Ultra Deep Field (HUDF).
#It involves loading an RGB image and a galaxy catalog, visualizing the RGB image, plotting galaxies on the image,
#and analyzing redshift distributions of the cataloged galaxies.

#Dependencies:
#- pandas
#- matplotlib

#Note: Ensure 'rgb_screenshot.png' and 'galaxy_catalog.csv' files exist in the working directory.

#"""
import pandas as pd
import matplotlib.pyplot as plt

# Load the RGB image (assuming 'rgb_screenshot.png' is the filename)
rgb_image = plt.imread('rgb_screenshot.png')

# Load the galaxy catalog (assuming 'galaxy_catalog.csv' is the filename)
# Load the galaxy catalog with a specified encoding
galaxy_catalog = pd.read_csv('galaxy_catalog.csv', encoding='latin1')
# Replace 'latin1' with other encodings if needed

# Verify the content and structure of the galaxy catalog



# Verify the content and structure of the galaxy catalog
print(galaxy_catalog.head())

# Plot the RGB image
plt.figure(figsize=(8, 8))
plt.imshow(rgb_image)
plt.xlabel('X-axis')  # Add appropriate labels based on the image content
plt.ylabel('Y-axis')
plt.title('Hubble UDF - RGB Image')
plt.grid(False)  # Adjust grid settings if necessary

# Plot galaxies from the catalog on the RGB image
plt.scatter(galaxy_catalog['RAJ2000'], galaxy_catalog['DEJ2000'], marker='o', s=5, c='red', label='Galaxies')
plt.legend()
plt.grid(color='white', linestyle='--', linewidth=0.5)
plt.show()

import matplotlib.pyplot as plt

# Filter galaxies with both photometric and spectroscopic redshifts
galaxies_with_both = galaxy_catalog.dropna(subset=['Photometric_Redshift', 'Spectroscopic_Redshift'])

# Plot histograms for redshift distributions
plt.figure(figsize=(10, 6))

plt.hist(galaxies_with_both['Photometric_Redshift'], bins=50, alpha=0.5, label='Photometric Redshift')
plt.hist(galaxies_with_both['Spectroscopic_Redshift'], bins=50, alpha=0.5, label='Spectroscopic Redshift')

plt.xlabel('Redshift')
plt.ylabel('Frequency')
plt.title('Distribution of Photometric vs. Spectroscopic Redshifts')
plt.legend()
plt.grid(True)
plt.show()



# Scatter plot for redshift distributions
plt.figure(figsize=(8, 6))

plt.scatter(galaxies_with_both['Photometric_Redshift'], galaxies_with_both['Spectroscopic_Redshift'], s=20, alpha=0.5)
plt.xlabel('Photometric Redshift')
plt.ylabel('Spectroscopic Redshift')
plt.title('Photometric vs. Spectroscopic Redshifts')
plt.grid(True)
plt.show()
