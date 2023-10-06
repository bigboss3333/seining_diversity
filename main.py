# This is a sample Python script.
import csv
import pathlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

Common_Name = 0
Genus = 1
Species = 2
Number_Caught = 3
Year = 4


def read_diversity_file(csv_path: pathlib.Path):
    with open(csv_path, 'r', encoding='utf-8') as csv_stream:
        reader = csv.reader(csv_stream)
        fish_dict = {}
        years = []
        for row in reader:
            years.append(row[Year])
        for year in sorted(set(years)):
            csv_stream.seek(0)
            for row in reader:
                year_read = row[Year]
                if row[Year] == year:
                    fish_dict.update({row[Common_Name]: int(row[Number_Caught])})
            yield year, fish_dict


def simpson_diversity_index(d):
    """Calculates the Simpson's diversity index from a dictionary.

      Args:
        d: A dictionary mapping species names to abundances.

      Returns:
        The Simpson's diversity index.
      """
    total_diversity = sum(d.values())
    numerator_list = []
    for _, abundance in d.items():
        numerator_list.append(abundance*(abundance-1))
    numerator = sum(numerator_list)
    denominator = total_diversity*(total_diversity-1)
    return 1-(numerator / denominator)


def write_diversity_table(generator_diversity, total_abundance: dict):
    with open('simpson_diversity_by_year.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerow(['Year', 'Diversity', 'Simpson_diversity_index'])
        for year, csv_data in generator_diversity:
            sdi = simpson_diversity_index(csv_data)
            diversity = total_abundance[year]
            writer.writerow([year, diversity, sdi])


def generate_simpsons_graph():
    data = pd.read_csv('simpson_diversity_by_year.csv')

    # Plot the data
    plt.plot(data.Year, data.Simpson_diversity_index)

    # Set the title and labels
    plt.title("Simpson's Diversity Graph")
    plt.xlabel("Years")
    plt.ylabel("Simpson's Diversity Index")

    # Show the plot
    #plt.show()
    plt.savefig('simpsons_diversity.png', bbox_inches='tight')


def generate_total_diversity_graph():
    data = pd.read_csv('simpson_diversity_by_year.csv')

    # Plot the data
    plt.plot(data.Year, data.Diversity)

    # Set the title and labels
    plt.title("Diversity Graph")
    plt.xlabel("Years")
    plt.ylabel("Species Richness")

    # Show the plot
    plt.show()
    #plt.savefig('species_richness.png', bbox_inches='tight')


def main():
    total_abundance = {'2023': 905, '2022': 3894, '2021': 3105, '2020': 5185, '2019': 385, '2018': 5419, '2017': 2325,
                       '2016': 2177, '2015': 2178, '2014': 901, '2013': 505, '2012': 8388, '2011': 1321, '2010': 1039}
    generator_diversity = read_diversity_file(pathlib.Path('Ninigret-Compiled.csv'))
    write_diversity_table(generator_diversity, total_abundance)
    generate_simpsons_graph()
    generate_total_diversity_graph()


if __name__ == '__main__':
    main()
