# UNITED NATIONS SPEECHES 1970-2015 ANALYSIS

## GENERAL STRUCTURE 
* Data introduction & overview in notebook (1)
* Data cleaning & tokenisation 
* TF-IDF weighting of document-term matrix
* Initial exploratory analysis & visualisations (wordclouds etc.)
* Topic modeling with SKLEARN
 * includes: Nonnegative Matrix Factorisation (NMF)
 * Singular Value Decomposition (SVD)
* Topic modeling with GENSIM
 * NMF unigrams and NMF bigrams
 * Latent Dirichlet Allocation (LDA) 
 * Hierarchical Dirichlet Process (HDP) (experimental implementation)
 * Optimal topic counts with Coherence optimisation


## STILL A WORK IN PROGRESS - FUTURE WORKS:
* further tune the bi-gram NMF model with lemmatisation/stopword removal
* Re-add tuned Latent Dirichlet Allocation & interactive visual for SKLEARN

## Possible Future Expansions
* Possibly extend to paragraph summation techniques after topic modeling 
* Some sort of sentiment analysis 
