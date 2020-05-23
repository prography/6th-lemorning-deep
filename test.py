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


#실행결과
#origin ['techno', 'electronic', 'synth']
#iruma ['piano', 'slow', 'classical']
#onepeace ['drums', 'strings', 'violin']