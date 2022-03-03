import matplotlib.pyplot as plt

Nucleotides = ['A', 'C', 'G', 'T']
Appearance = [363451,635986,638868,364699]

Colors = ['red', 'green', 'blue', 'yellow']
plt.bar(Nucleotides, Appearance, color=Colors)
plt.title('Presence of Nucleotides in a Thermophile sample', fontsize=15)
plt.xlabel('Type of Nucleotide', fontsize=15)
plt.ylabel('Number of Nucleotides', fontsize=15)
plt.grid(True)
plt.show()
