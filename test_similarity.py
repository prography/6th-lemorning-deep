import numpy as np

if __name__ == '__main__':
    feat = np.load('sample_audio/numpy/features.npy')
    feat_label = np.load('sample_audio/numpy/labels.npy')

    mat_sim = feat @ feat.T

    for input_idx in range(15):
        result = np.argsort(mat_sim[input_idx])[::-1]

        print('쿼리 데이터 : {}'.format(feat_label[input_idx]))
        print('결과 데이터 : {}'.format(
            ', '.join(map(lambda x: feat_label[x], result))))
        print(np.sort(mat_sim[input_idx])[::-1])
        print()
