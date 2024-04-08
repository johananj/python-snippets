# Reading text files
# loading a text file onto a list
# each line is an item on the list
with open('./textfile.txt') as f:
    vocab = f.read().splitlines()


# Pickling
# saving variables and reloading them using pickle
import pickle
var1 = ['some', 'stuff']
var2 = ['someother', 'stuff']
pickle_path = 'path/to/picklefile.pkl'
# dump to a pickle file
with open(pickle_path, 'wb') as file:
    pickle.dump(var1, file)
    pickle.dump(var2, file)
# call load method to deserialze
with open(pickle_path, 'rb') as file:
    var1 = pickle.load(file)
    var2 = pickle.load(file)