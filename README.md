# Contextualized Sensorimotor Norms

GitHub repository for the Contextualized Sensorimotor Norms (CS Norms) database, as described in:

> Trott, S., Bergen, B. (2022). Contextualized Sensorimotor Norms: multi-dimensional measures of sensorimotor strength for ambiguous English words, in context

## About the data

The data sheet can be found [here](https://github.com/seantrott/cs_norms/blob/main/data_sheet.docx).

Additionally, there are several datasets included in the repository:

### Contextualized norms

The file [`data/processed/contextualized_sensorimotor_norms.csv`](https://github.com/seantrott/cs_norms/blob/main/data/processed/contextualized_sensorimotor_norms.csv) is the primary dataset described the manuscript.

The same directory also contains:

- `sentence_pairs_with_sensorimotor_distance.csv`: for each sentence pair for a given ambiguous word, this file indicates the sensorimotor distance (i.e., the cosine distance between the sensorimotor vectors). 
- `dominance_norms_with_order.csv`: this file contains judgments of the relative dominance of each context of use, for each different-sense sentence pair. 
- `sentence_pairs_with_baseline.csv`: for each sentence pair for a given ambiguous word, this file contains the "baseline" distance calculated using a bag-of-words model from the LS Norms.  
- `contextualized_sensorimotor_norms_with_ls.csv`: contains the distance between the CS Norm for each sentence and the corresponding LS Norm for that word.


### Individual responses

In the [`data/individual_responses` folder](https://github.com/seantrott/cs_norms/tree/main/data/individual_responses), you can find subject-level responses, separated into the **Action** and **Perception** groups.

### Supplementary data

Under `data/lexical`, we also include the Lancaster Sensorimotor Norms (Lynott et al, 2019). 

## Analysis

Code to run the primary analyses described in the paper can be found in `src/analysis` [here](https://github.com/seantrott/cs_norms/blob/main/src/analysis/contextualized_norms_analysis.Rmd), along with a *knit* `.html` file.

Further, the code to build the bag-of-words baseline can be found in `src/data/bow.py`; the code to calculate the distance between each CS Norm and the LS Norm can be found in `src/data/distance_to_ls.py`. 

# References

Lynott, D., Connell, L., Brysbaert, M., Brand, J., & Carney, J. (2019). The Lancaster Sensorimotor Norms: multidimensional measures of perceptual and action strength for 40,000 English words. Behavior Research Methods, 1-21.
