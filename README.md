# SBU_elasticSearch
SBU project for the course "Information Retrieval"

The data used here is the top 100 news crawled from [this site](https://www.asriran.com/)

This code re-orders the results from searching query in the text, so that the order is as close as possible to the results from searching in the titles.

This is done by using optimizations such as _gradient descent_ (written in "manual.py") or _scipy.optimize_ (written in "ez.py") which are placed in the "ai" folder.
The data these optimization functions work with is the data we receive from [pytrec_eval](https://github.com/cvangysel/pytrec_eval)
