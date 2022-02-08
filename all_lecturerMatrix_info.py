import pickle

allLecturerMatrix = [[[0 for j in range(8)]for i in range(6)]for k in range(1, 29)]
with open('file3.txt','wb') as f:
    pickle.dump(allLecturerMatrix,f)