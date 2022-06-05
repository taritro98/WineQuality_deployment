import pickle
import numpy as np

# Loading model to compare the results
model = pickle.load(open('modlel.pkl','rb'))

s = np.load('std.npy')
m = np.load('mean.npy')

pred_row = [7.4, 0.7, 0.0, 1.9, 0.076, 11.0, 34.0, 0.9978, 3.51, 0.56, 9.4]

proc_row = (np.array([pred_row] - m)) / s

preds = model.predict(proc_row)

print(preds)