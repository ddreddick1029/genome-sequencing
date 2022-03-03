import matplotlib.pyplot as plt

Nucleotides = ['A', 'C', 'G', 'T']
Appearance = [1268010,1305686,1292707,1265665]

Colors = ['red', 'green', 'blue', 'yellow']
plt.bar(Nucleotides, Appearance, color=Colors)
plt.title('Presence of Nucleotides in a Escherichia coli sample', fontsize=15)
plt.xlabel('Type of Nucleotide', fontsize=15)
plt.ylabel('Number of Nucleotides (in millions)', fontsize=15)
plt.grid(True)
plt.show()
