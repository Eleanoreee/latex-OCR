import pickle
from dataset import Im2LatexDataset

# Specify the path to your .pkl file
file_path = '/Users/eleanorewu/dataset.pkl'

# Load the data from the .pkl file
with open(file_path, 'rb') as file:
    data = pickle.load(file)

# Print or manipulate the loaded data
print(data)
