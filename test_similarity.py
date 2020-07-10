import numpy as np

if __name__ == '__main__':
    size = 19
    feat = np.load('data/feature/feats.npy')
    feat_label = np.load('data/feature/labels.npy')

    mag = np.sqrt(np.sum(feat ** 2, 1)).reshape(-1, 1)
    mat_mag = mag @ mag.T
    mat_sim = feat @ feat.T

    mat_sim = mat_sim / mat_mag
    str_format = '%-10s'

    for input_idx in range(size):
        result = np.argsort(mat_sim[input_idx])[::-1]
        mat_sim[input_idx] = np.sort(mat_sim[input_idx])[::-1]

        print('쿼리 데이터 : {}'.format(feat_label[input_idx]))

        print('결과 데이터 : ')
        for idx in range(size):
            # print('결과 데이터 : {}'.format(', '.join(map(lambda x: feat_label[x], result))))
            # print(np.sort(mat_sim[input_idx])[::-1])
            print("{:20} : {}".format(feat_label[idx], mat_sim[input_idx][idx]))
        print()
