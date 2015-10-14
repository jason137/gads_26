<!-- author: Jason Dolatshahi -->

# lec 6 exercises
## machine learning

Complete these exercises in groups of 2 or 3. Try to make your responses as
simple as possible.

### no computers

1) Define the following terms:
- generalization error
- cross-validation
- unsupervised learning
- supervised learning
- overfitting

2) There is a subtle (but important) statistical issue lurking beneath the
surface of our discussion of the train/test split. What is it?

### yes computers

3) Load the small dataset in `trucks.csv` into Python. Perform a (70/30) train/test
split and output your results.

Note that you can shuffle a DataFrame called `df` like this:  

    new_index = np.random.permutation(df.index))   
    df = df.reindex(new_index)
