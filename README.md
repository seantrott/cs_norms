# Contextualized Sensorimotor Norms

GitHub repository for the Contextualized Sensorimotor Norms (CS Norms) database, as described in:

> Trott, S., Bergen, B. (2022). Contextualized Sensorimotor Norms: multi-dimensional measures of sensorimotor strength for ambiguous English words, in context

## About the data

The data sheet can be found [here](https://github.com/seantrott/cs_norms/blob/main/data_sheet.docx).

Additionally, there are several datasets included in the repository:

### Contextualized norms

The file [`data/processed/contextualized_sensorimotor_norms.csv`](https://github.com/seantrott/cs_norms/blob/main/data/processed/contextualized_sensorimotor_norms.csv) is the primary dataset described the primary.

The same directory also contains:

- `sentence_pairs_with_sensorimotor_distance.csv`: for each sentence pair for a given ambiguous word, this file indicates the sensorimotor distance (i.e., the cosine distance between the sensorimotor vectors). 
- `dominance_norms_with_order.csv`: this file contains judgments of the relative dominance of each context of use, for each different-sense sentence pair. 

### Individual responses

In the [`data/individual_responses` folder](https://github.com/seantrott/cs_norms/tree/main/data/individual_responses), you can find subject-level responses, separated into the **Action** and **Perception** groups.

### Supplementary data

Under `data/lexical`, we also include the Lancaster Sensorimotor Norms (Lynott et al, 2019). 

•	Under src/analysis, there is an R-markdown file with code to reproduce the analyses described in the paper, along with a knit .html file.
•	Under data/processed, there are several data files:
o	Contextualized_sensorimotor_norms.csv: this is the primary dataset described in the paper (see Data Sheet for additional details).
o	Sentence_pairs_with_sensorimotor_distance.csv: this contains 672 sentence pairs (originally from the RAW-C dataset), augmented with the sensorimotor distance between each sentence in each sentence pair.
o	Dominance_norms_with_order.csv: this contains judgments of the relative dominance of each context of use, for each different-sense sentence pair.
•	Under data/lexical, we also include the Lancaster Sensorimotor Norms (Lynott et al, 2019). 


## Analysis

Code to run the primary analyses described in the paper can be found in `src/analysis` [here](https://github.com/seantrott/cs_norms/blob/main/src/analysis/contextualized_norms_analysis.Rmd), along with a *knit* `.html` file.

# References

