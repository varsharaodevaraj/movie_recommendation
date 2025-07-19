import pickle

# Assuming movies.pkl is in your current folder
with open('movies.pkl', 'rb') as f:
    movies = pickle.load(f)

print(type(movies))       # Check what type of object it is
print(movies[:2])         # Print first 2 items (works if it's a list or DataFrame)
