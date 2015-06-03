# Bloom Filter

A basic filter to test whether or not en element is in a set. You can read more about Bloom Filters [here](http://en.wikipedia.org/wiki/Bloom_filter). This repository is also an exploration into the unittest module in Python 3

For now I am using 2, 10 bit hashes, which means that the words can be at most 1024 characters long. Currently the hashing function is very poor (any two words which are anagrams will collide), but it is just used as a proof of concept, the more important functionality lies in the contains and add functions.
