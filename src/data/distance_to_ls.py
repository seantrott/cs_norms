"""Calculate distance between each contextualized norm and the LS Norms."""


import numpy as np
import pandas as pd 


from scipy.spatial.distance import cosine


## PATHS
LANCASTER_PATH = "data/lexical/lancaster_norms.csv"
CONTEXT_PATH = "data/processed/contextualized_sensorimotor_norms.csv"
SAVE_PATH = "data/processed/contextualized_sensorimotor_norms_with_ls.csv"

###
LS_COLUMNS = ['Auditory.mean', 'Gustatory.mean', 'Haptic.mean',
		   'Interoceptive.mean', 'Olfactory.mean', 'Visual.mean', 'Foot_leg.mean',
       'Hand_arm.mean', 'Head.mean', 'Mouth.mean', 'Torso.mean']

CS_COLUMNS = ['Hearing.M', 'Taste.M', 'Touch.M',
		   'Interoception.M', 'Olfaction.M', 'Vision.M', 'Foot_leg.M',
       'Hand_arm.M', 'Head.M', 'Mouth_throat.M', 'Torso.M']

###### Lancaster norms
df_lancaster = pd.read_csv(LANCASTER_PATH)
df_lancaster['word'] = df_lancaster['Word'].str.lower()
# Create dictionary
sm_norms = dict(zip(df_lancaster['word'].values, df_lancaster[LS_COLUMNS].values))


###### Contextualized norms
df_contextualized = pd.read_csv(CONTEXT_PATH)

distances = []
for index, row in df_contextualized.iterrows():

	cs = list(row[CS_COLUMNS].values)
	ls = sm_norms[row['word']]

	distance = cosine(cs, ls)
	distances.append(distance)

df_contextualized['distance_to_lancaster'] = distances
df_contextualized.to_csv(SAVE_PATH)
