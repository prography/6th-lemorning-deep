# 6th-lemorning-deep

6기 레모닝 딥러닝

## Install

- python dependencies 설치

```
pip install -r requirements.txt
```

## Directory

```
.
├── audio/
├── data/
├── musicnn/
├── model_light.py
├── run_model_light.py
└── test_similarity.py

```

- audio/ : 샘플 오디오 저장
- data/ : similarity test를 위한 미리 계산된 오디오 features, labels
- musicnn/ : musicnn에 관련된 코드
- model_light.py : 경량화된 musicnn 코드
- run_model_light.py: 태그를 추출하는 샘플 코드
- test_similarity.py: 유사도 계산하는 샘플 코드

## How to use

- features, tags 추출

```
import model_light import Model

model = Model()

path_audio = 'test1.mp3'

features, tags = model.extract_features_and_tags(path_aduio)

print(features) # audio를 나타내는 features 추출
print(tags)     # audio의 Tag 추출
```

## Note

1. 빠른 오디오 로드를 위해서 음원의 6초가량의 첫부분만 사용.

2. 유사도 계산시에 분위기 보다는 사용되는 악기에 따른 유사도 측정됨

- MTT Dataset의 Label이 주로 악기나 장르로 정의 되어 있기 때문에

3. TAG는 MTT Dataset을 사용 (대략 50개)

```
tag = ['ambient', 'beat', 'beats', 'cello', 'choir', 'choral', 'classic', 'classical', 'country', 'dance', 'drums', 'electronic', 'fast', 'female', 'female vocal', 'female voice', 'flute', 'guitar', 'harp', 'harpsichord', 'indian', 'loud', 'male', 'male vocal', 'male voice', 'man', 'metal', 'new age', 'no vocal', 'no vocals', 'no voice', 'opera', 'piano', 'pop', 'quiet', 'rock', 'singing', 'sitar', 'slow', 'soft', 'solo', 'strings', 'synth', 'techno', 'violin', 'vocal', 'vocals', 'voice', 'weird', 'woman']
```

## Reference

- musicnn
  https://github.com/jordipons/musicnn/tree/516acb2a0ff5ef73f64547898e018e793152c506
