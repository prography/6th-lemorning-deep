import numpy as np

if __name__ == '__main__':
    feat = np.load('data/feature/feats.npy')
    feat_label = np.load('data/feature/labels.npy')

    mag = np.sqrt(np.sum(feat ** 2, 1)).reshape(-1, 1)
    mat_mag = mag @ mag.T
    mat_sim = feat @ feat.T

    mat_sim = mat_sim / mat_mag
    
    for input_idx in range(19):
        result = np.argsort(mat_sim[input_idx])[::-1]

        print('쿼리 데이터 : {}'.format(feat_label[input_idx]))
        print('결과 데이터 : {}'.format(', '.join(map(lambda x: feat_label[x], result))))
        print(np.sort(mat_sim[input_idx])[::-1])
        print()