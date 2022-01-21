import numpy as np
import os
import pickle
import math
import pandas as pd


# Function to calculate the authority and hub score of the nodes
def authority_hub_score(outlinks):
    # Size of the matrix
    size = outlinks.shape[0]

    # Initializing the lists
    h = [1.0 for i in range(size)]
    a = [1.0 for i in range(size)]

    # Printing initial Hub score
    print(h)

    # Printing the augmented matrix
    pickle_off = open(pickle_file, 'rb')
    aug_mat = pickle.load(pickle_off)
    print('\nThe augmented matrix is: \n',aug_mat)

    n = int(input('Enter no. of iterations: '))
    for _ in range(n):
        # Calculating the authority scores
        for j in range(size):
            temp_auth = 0.0
            for i in range(size):
                if outlinks[i][j] == 1:
                    temp_auth += h[i]
            a[j] = temp_auth

        # Normalizing the authority scores
        auth_sum = sum((map(lambda i: i * i, a)))
        auth_sqrt = math.sqrt(auth_sum)
        for i in range(len(a)):
            a[i] = round(a[i] / auth_sqrt, 4)

        # Calculating the hub scores
        for i in range(size):
            temp_hub = 0.0
            for j in range(size):
                if outlinks[i][j] == 1:
                    temp_hub += a[j]
            h[i] = temp_hub

        # Normalizing the hub scores
        hub_sum = sum((map(lambda i: i * i, h)))
        hub_sqrt = math.sqrt(hub_sum)
        for i in range(len(h)):
            h[i] = round(h[i] / hub_sqrt, 4)

        #table = pd.DataFrame({f"X{_ + 1}": h, f"Y{_ + 1}": a})
        #print(table.to_markdown(index=False),'\n')
        print('\n',f'h{_ + 1}:',h,'\n',f'a{_ + 1}:',a)
    return a, h


# Getting the name of pickle file from user
pickle_file = input('Enter the name of the pickle file:\t')

# If the pickle file is not there write the elements to be stored..
# ..in the pickle file
if not os.path.isfile(pickle_file):
    n = int(input('Enter the size of the matrix:\t'))
    outlinks = []
    for i in range(n * n):
        temp = int(input('Enter the element:\t'))
        outlinks.append(temp)
    outlinks = np.reshape(outlinks, (n, n))
    pickle.dump(outlinks, open(pickle_file, 'wb'), protocol=4)
# If the pickle file is already there load the pickle file
else:
    print('Loading outlink matrix from %s' % pickle_file)
    outlinks = pickle.load(open(pickle_file, 'rb'))

a, h = authority_hub_score(outlinks)

print('\n')
# Printing the final scores
output_table = pd.DataFrame({"FinalHubScores": h, "FinalAuthorityScores": a})
print(output_table.to_markdown(index=False))
