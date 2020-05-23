file_name1 = './audio/joram-moments_of_clarity-08-solipsism-59-88.mp3'
file_name2 = './audio/iruma.mp3'
file_name3 = './audio/Luffys_Fierce_Attack.mp3'

from musicnn.tagger import top_tags
origin = top_tags(file_name1, model='MTT_musicnn', topN=3)
print("origin", origin)

iruma = top_tags(file_name2, model='MTT_musicnn', topN=3)
print("iruma", iruma)

onepeace = top_tags(file_name3, model='MTT_musicnn', topN=3)
print("onepeace", onepeace)


# from musicnn.extractor import extractor
# taggram, tags, features = extractor(file_name1, model='MTT_musicnn', extract_features=True)
# print("===============tags - oringin=============================")
# print(tags)
# taggram, tags, features = extractor(file_name2, model='MTT_musicnn', extract_features=True)
# print("===============tags - iruma=============================")
# print(tags)
# taggram, tags, features = extractor(file_name3, model='MTT_musicnn', extract_features=True)
# print("===============tags - onepeace=============================")
# print(tags)
# print("===============tags=============================")
# print(tags)
# print("===============tags===========================")
# print("taggram: ",type(taggram))
# print("tags:    ",type(tags))
# print("features:",type(features))
