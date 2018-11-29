"""
Fisher linear discriminant algorithm

author: Yajue Yang
"""

from project.data_processing import load_train_test_data
import numpy as np

# Number of classes
NUM_CLASSES = 3


def fisher_discriminant(x, y):

    num_data = len(x)
    dim_feat = len(x[0])

    x_classified = [[], [], []]

    for (i, j) in zip(x, y):
        x_classified[j-1].append(i)

    x_classified = [np.array(x_classified[0]).transpose(), np.array(x_classified[1]).transpose(), np.array(x_classified[2]).transpose()]

    x_mean = [x_classified[i].mean(axis=1) for i in range(3)]

    x_mean_total = 0
    for i in range(3):
        x_mean_total += x_mean[i] * x_classified[0].shape[1]

    x_mean_total /= num_data

    S_w = np.zeros((dim_feat, dim_feat))
    S_b = np.zeros((dim_feat, dim_feat))
    for i in range(3):
        S_w += (x_classified[i] - x_mean[i][:, np.newaxis]) @ (x_classified[i] - x_mean[i][:, np.newaxis]).transpose()
        S_b += x_classified[i].shape[1] * (x_mean[i][:, np.newaxis] - x_mean_total[:, np.newaxis]) @ (x_mean[i][:, np.newaxis] - x_mean_total[:, np.newaxis]).transpose()

    eig_val, eig_vec = np.linalg.eigh(np.linalg.inv(S_w) @ S_b)
    idx = np.absolute(eig_val).argsort()[::-1]
    eig_val = eig_val[idx]
    eig_vec = eig_vec[:, idx]

    Theta = eig_vec[0][:, np.newaxis]
    Theta = np.append(Theta, eig_vec[1][:, np.newaxis], axis=1)

    print(Theta.transpose() @ x_classified[0])
    print(Theta.transpose() @ x_classified[1])
    print(Theta.transpose() @ x_classified[2])

    # print(eig_vec)











if __name__ == '__main__':

    train_data, test_data = load_train_test_data()

    fisher_discriminant(train_data[1], train_data[0])