#"""
#Galaxy Redshift Analysis Visualization

#This section of code focuses on visualizing redshift distributions for galaxies in the catalog.
#It filters galaxies with both photometric and spectroscopic redshifts, creates histograms to depict their distributions,
#and generates a scatter plot to compare photometric and spectroscopic redshift values.

#Dependencies:
#- matplotlib

#Note: This assumes a 'galaxy_catalog' dataframe is available in the current environment.

#"""
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
