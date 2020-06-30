import os
import time

import numpy as np

from model_light import Model

if __name__ == '__main__':
    model = Model()
    path_audio = './audio/TRWJAZW128F42760DD_test.mp3'

    start_time = time.time()
    feat, tags = model.extract_features_and_tags(path_audio)
    end_time = time.time()
    print(tags)
    print('inference time : {}'.format(end_time - start_time))

    # path_folder = './audio/data'
    
    # model = Model()

    # filenames = os.listdir(path_folder)

    # feats = []
    # labels = []
    # for file in filenames:

    #     feat, tags = model.extract_features_and_tags(os.path.join(path_folder, file))

    #     feats.append(feat)
    #     labels.append(file)

    # feats = np.stack(feats, 0)
    # labels = np.array(labels)

    # np.save('./data/feats.npy', feats)
    # np.save('./data/labels.npy', labels)

    

    
    

