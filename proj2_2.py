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
import logging

# Set up logging
logging.basicConfig(filename='galaxy_catalog.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def load_rgb_image(file_path):
    """Load and return the RGB image."""
    try:
        rgb_image = plt.imread(file_path)
        logging.info(f"Loaded RGB image from {file_path}")
        return rgb_image
    except FileNotFoundError:
        logging.error(f"Error loading RGB image from {file_path}: File not found")
        return None

def load_galaxy_catalog(file_path, encoding='latin1'):
    """Load and return the galaxy catalog."""
    try:
        galaxy_catalog = pd.read_csv(file_path, encoding=encoding)
        logging.info(f"Loaded galaxy catalog from {file_path}")
        return galaxy_catalog
    except FileNotFoundError:
        logging.error(f"Error loading galaxy catalog from {file_path}: File not found")
        return None
    except Exception as e:
        logging.error(f"Error loading galaxy catalog from {file_path}: {e}")
        return None

def visualize_rgb_image(rgb_image):
    """Visualize the RGB image."""
    plt.figure(figsize=(8, 8))
    plt.imshow(rgb_image)
    plt.xlabel('X-axis')  # Add appropriate labels based on the image content
    plt.ylabel('Y-axis')
    plt.title('Hubble UDF - RGB Image')
    plt.grid(False)  # Adjust grid settings if necessary
    plt.show()

def plot_galaxies(galaxy_catalog):
    """Plot galaxies from the catalog on the RGB image."""
    plt.scatter(galaxy_catalog['RAJ2000'], galaxy_catalog['DEJ2000'], marker='o', s=5, c='red', label='Galaxies')
    plt.legend()
    plt.grid(color='white', linestyle='--', linewidth=0.5)
    plt.show()

def plot_redshift_histograms(galaxy_catalog):
    """Plot histograms for redshift distributions."""
    galaxies_with_both = galaxy_catalog.dropna(subset=['Photometric_Redshift', 'Spectroscopic_Redshift'])
    plt.figure(figsize=(10, 6))
    plt.hist(galaxies_with_both['Photometric_Redshift'], bins=50, alpha=0.5, label='Photometric Redshift')
    plt.hist(galaxies_with_both['Spectroscopic_Redshift'], bins=50, alpha=0.5, label='Spectroscopic Redshift')
    plt.xlabel('Redshift')
    plt.ylabel('Frequency')
    plt.title('Distribution of Photometric vs. Spectroscopic Redshifts')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_redshift_scatter(galaxy_catalog):
    """Plot scatter plot for redshift distributions."""
    galaxies_with_both = galaxy_catalog.dropna(subset=['Photometric_Redshift', 'Spectroscopic_Redshift'])
    plt.figure(figsize=(8, 6))
    plt.scatter(galaxies_with_both['Photometric_Redshift'], galaxies_with_both['Spectroscopic_Redshift'], s=20, alpha=0.5)
    plt.xlabel('Photometric Redshift')
    plt.ylabel('Spectroscopic Redshift')
    plt.title('Photometric vs. Spectroscopic Redshifts')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Load RGB image
    rgb_image = load_rgb_image('rgb_screenshot.png')
    if rgb_image is not None:
        # Visualize RGB image
        visualize_rgb_image(rgb_image)

    # Load galaxy catalog
    galaxy_catalog = load_galaxy_catalog('galaxy_catalog.csv')
    if galaxy_catalog is not None:
        # Visualize galaxies on RGB image
        plot_galaxies(galaxy_catalog)

        # Plot redshift histograms
        plot_redshift_histograms(galaxy_catalog)

        # Plot redshift scatter plot
        plot_redshift_scatter(galaxy_catalog)
