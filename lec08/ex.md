<!-- author: Jason Dolatshahi -->

# lec 8 exercises
## naive bayes

Complete these exercises in groups of 2 or 3. Try to make your responses as
simple as possible.

### no computers

1) Define the following terms:
- likelihood function
- conditional probability
- posterior distribution
- independence
- updating
- prior probability
- sample space

2) Why is the model called "naive" Bayes? What do we gain by imposing this
naivety?

3) Bayesian statistics requires us to cast our beliefs and expectations as
degrees of belief, whereas classical (frequentist) statistics only permits
statements of probability that pertain to limits of repeated random trials.
Which interpretation makes more sense to you intuitively? What about
mathematically?

### yes computers

4) Text processing (or in flashier terms, **natural language processing**) is a
field of data science where the feature space is populated by documents
containing text. For example you may have a dataset (usually called a
**corpus**) where each record is a news article or an email.

There are a number of ways to preprocess a corpus of text data for modeling. One
popular and practical method is called the **bag of words** representation, where
each word is represented by its own feature, and documents are assigned a score
for each word proportional to the number of occurrences in the document.

We want to do this in a way that allows us to compare documents to
each other. Two documents of different lengths will have different word counts,
and therefore be difficult to compare if the counts are left in raw form.
Transforming them into **frequencies** allows us to make comparisons across
documents.

Another important consideration is to minimize the amount of noise that we
build into the preprocessed data. If a common word like "the" occurs frequently
across documents, its usefulness for prediction will be limited, and therefore
we'd like to suppress its influence. We can achieve this by **downsampling** words
that are frequent across documents.

A common pre-processing technique that addresses both of these concerns is called
**tf-idf**, or term frequency-inverse document frequency scoring. Instead of a raw
count, tf-idf assigns a document a score for a given word that's proportional to
the word's frequency in the document, and inversely proportional to the word's
frequency across documents. This makes scores easy to compare and reasonably
noise-free.

Scikit-learn has a lot of functionality to help with pre-processing steps like
these. Take a look at the text classification
[example](http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html)
in the docs and apply these steps to build a naive Bayes text classifier either
using the built-in dataset in the example, or the dataset in `email.csv`.


[Solution](https://github.com/jason137/gads_26/blob/master/example_notebooks/Ex08_TextProcessing_NaiveBayes.ipynb)
