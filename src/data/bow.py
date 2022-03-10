"""Code for creating BOW representations."""

import numpy as np
import pandas as pd 

# from nltk.stem import WordNetLemmatizer

from scipy.spatial.distance import cosine


## PATHS
LANCASTER_PATH = "data/lexical/lancaster_norms.csv"
SENTENCE_PAIRS = "data/processed/sentence_pairs_with_sensorimotor_distance.csv"
SAVE_PATH = "data/processed/sentence_pairs_with_baseline.csv"

## Columns
COLUMNS = ['Auditory.mean', 'Gustatory.mean', 'Haptic.mean',
		   'Interoceptive.mean', 'Olfactory.mean', 'Visual.mean', 'Foot_leg.mean',
       'Hand_arm.mean', 'Head.mean', 'Mouth.mean', 'Torso.mean']

###### Lancaster norms
df_lancaster = pd.read_csv(LANCASTER_PATH)
df_lancaster['word'] = df_lancaster['Word'].str.lower()
# Create dictionary
sm_norms = dict(zip(df_lancaster['word'].values, df_lancaster[COLUMNS].values))

###### Read in sentence pairs
df_pairs = pd.read_csv(SENTENCE_PAIRS)

###### Lemmatizer
# lemmatizer = WordNetLemmatizer()



###### Get BOW?
def get_bow_for_sentence(sentence):
	"""Get LS Norms for each word in sentence."""
	words = sentence.lower().replace(".", "").split()

	sv = []
	for w in words:
		if w in sm_norms:
			sv.append(sm_norms[w])

	sv = np.array(sv)
	sv_mean = np.mean(sv, axis = 0)
	return sv_mean


def get_bow_distance(row):

	### Get all words
	words_s1 = row['sentence1'].lower().replace(".", "").split()
	words_s2 = row['sentence2'].lower().replace(".", "").split()

	### Get disambiguating words
	### (Final word is relevant for ones that differ in a/an)
	disambiguating_s1 = [w for w in words_s1 if w not in words_s2][-1]
	disambiguating_s2 = [w for w in words_s2 if w not in words_s1][-1]

	### Check if it appears in sm_norms
	if disambiguating_s1 not in sm_norms or disambiguating_s2 not in sm_norms:
		return None

	s1 = sm_norms[disambiguating_s1]
	s2 = sm_norms[disambiguating_s2]

	# s1 = get_bow_for_sentence(row['sentence1'])
	# s2 = get_bow_for_sentence(row['sentence2'])

	return cosine(s1, s2)


df_pairs['baseline_distance'] = df_pairs.apply(get_bow_distance, axis = 1)

df_pairs.to_csv(SAVE_PATH)