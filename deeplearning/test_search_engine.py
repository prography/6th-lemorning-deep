import os

from dl.deep.model import DeepModel
from dl.search_engine.milvusdb import SearchEngine

if __name__ == '__main__':
    model = DeepModel()
    path_root = 'data/audio/test/'
    path_audios = [os.path.join(path_root, file)
                   for file in os.listdir(path_root)]
    path_new_audio = 'dl/data/audio/joram-moments_of_clarity-08-solipsism-59-88.mp3'

    HOST = os.environ.get('HOST_SEARCH_ENGINE', '3.15.42.143')
    PORT = os.environ.get('PORT_SEARCH_ENGINE', 19530)
    N_DIM_FEATURE = os.environ.get('N_DIM_FEATURE', 200s)

    # 1. set engine
    engine = SearchEngine(HOST, PORT)

    ##############################
    # Collection
    ##############################
    # 2-1. create collection
    engine.create_collection('musicDB', N_DIM_FEATURE)

    # 2-2. show info of collection
    engine.get_collection_stats('musicDB')

    # 2-3. delete collection
    engine.drop_collection('musicDB')

    ##############################
    # CRUD Data
    ##############################
    engine.create_collection('musicDB', N_DIM_FEATURE)
    engine.set_collection('test')

    # 3-1. insert data
    for i, path_audio in enumerate(path_audios):
        feature = model.extract_info(path_audio, mode='feature')
        engine.insert_data(i, feature)
    engine.get_collection_stats('musicDB')

    # 3-3. update data
    feature = model.extract_info(path_new_audio, mode='feature')
    engine.update_data(len(path_audios) - 1, feature)
    engine.get_collection_stats('musicDB')

    # # 3-3. update data
    engine.delete_data(len(path_audios) - 1)
    engine.get_collection_stats('musicDB')

    # ##############################
    # # Search Data
    # ##############################

    # # 4-1. search data by feature
    feature = model.extract_info(path_new_audio, mode='feature')
    li_id, li_distance = engine.search_by_feature(feature, 5)
    result = [(idx, dis) for idx, dis in zip(li_id, li_distance)]
    print(result)

    # 4-2. search data by key
    li_id, li_distance = engine.search_by_key(len(path_audios) - 2, 5)
    result = [(idx, dis) for idx, dis in zip(li_id, li_distance)]
    print(result)
