file_name1 = './audio/joram-moments_of_clarity-08-solipsism-59-88.mp3'
file_name2 = './audio/iruma.mp3'
file_name3 = './audio/Luffys_Fierce_Attack.mp3'

from musicnn.tagger import top_tags

origin = top_tags(file_name1)
print(origin)

iruma = top_tags(file_name2)
print(iruma)

onepeace = top_tags(file_name3)
print(onepeace)


#origin ['techno', 'electronic', 'synth']
#iruma ['piano', 'slow', 'classical']
#onepeace ['drums', 'strings', 'violin']



tag = ['ambient', 'beat', 'beats', 'cello', 'choir', 'choral', 'classic', 'classical', 'country', 'dance', 'drums', 'electronic', 'fast', 'female', 'female vocal', 'female voice', 'flute', 'guitar', 'harp', 'harpsichord', 'indian', 'loud', 'male', 'male vocal', 'male voice', 'man', 'metal', 'new age', 'no vocal', 'no vocals', 'no voice', 'opera', 'piano', 'pop', 'quiet', 'rock', 'singing', 'sitar', 'slow', 'soft', 'solo', 'strings', 'synth', 'techno', 'violin', 'vocal', 'vocals', 'voice', 'weird', 'woman']