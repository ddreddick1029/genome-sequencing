# function to count the number of each nucleotide
# throughout the file
file = open(r"C:\Users\diava\Documents\thermophile.txt", "r")

data = file.read()

numberofAs = data.count("A")
numberofCs = data.count("C")
numberofGs = data.count("G")
numberofTs = data.count("T")

print('We see the letter A', numberofAs, 'times!')
print('We see the letter C', numberofCs, 'times!')
print('We see the letter G', numberofGs, 'times!')
print('We see the letter T', numberofTs, 'times!')

file.close()

print('\nThe percentage of As in relation to the entire thermophile file is: ', numberofAs /
      (numberofCs + numberofGs + numberofTs + numberofAs) * 100, )

print('\nThe percentage of Cs in relation to the entire thermophile file is: ', numberofCs /
      (numberofGs + numberofAs + numberofTs + numberofCs) * 100, )

print('\nThe percentage of Gs in relation to the entire thermophile file is: ', numberofGs /
      (numberofCs + numberofAs + numberofTs + numberofGs) * 100, )

print('\nThe percentage of Ts in relation to the entire thermophile file is: ', numberofTs /
      (numberofCs + numberofAs + numberofGs + numberofTs) * 100, )
