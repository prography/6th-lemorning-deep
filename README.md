# 6th-lemorning-deep
6기 레모닝 딥러닝


## installation

```
pip install musicnn

```
or 
```
git clone https://github.com/jordipons/musicnn.git

python setup.py install
```

## Tag 추출

- top_tags 함수 호출

```
from musicnn.tagger import top_tags
top_tags('./audio/joram-moments_of_clarity-08-solipsism-59-88.mp3')
```

- return: list, 가장 유사도 높은 장르(카테고리= 태그) 3개 추출
['drums', 'strings', 'violin']


## 전체 태그 갯수: 50개

tag = ['ambient', 'beat', 'beats', 'cello', 'choir', 'choral', 'classic', 'classical', 'country', 'dance', 'drums', 'electronic', 'fast', 'female', 'female vocal', 'female voice', 'flute', 'guitar', 'harp', 'harpsichord', 'indian', 'loud', 'male', 'male vocal', 'male voice', 'man', 'metal', 'new age', 'no vocal', 'no vocals', 'no voice', 'opera', 'piano', 'pop', 'quiet', 'rock', 'singing', 'sitar', 'slow', 'soft', 'solo', 'strings', 'synth', 'techno', 'violin', 'vocal', 'vocals', 'voice', 'weird', 'woman']


## musicnn 모델 

https://github.com/jordipons/musicnn/tree/516acb2a0ff5ef73f64547898e018e793152c506