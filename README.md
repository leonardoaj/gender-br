# Name2GenderBR
Enables gender classification based on first names, based on frequency of names found in Census 2010, data obtained from https://brasil.io/dataset/genero-nomes/grupos.
Provides simple methods on a pandas dataframe of names, frequencies and classifications.

## Usage:
from Name2GenderBR import GenderClassifier

classifier = GenderClassifier()
print(classifier.get_gender('Bruno'))
>> 'M'

print(classifier.is_male('Bruno'))
>> True

print(classifier.is_female('Bruno'))
>> False