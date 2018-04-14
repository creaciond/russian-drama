# Stage Directions in Russian Drama
3rd year coursework

## What's in the repo?

| File/folder      | What's inside |
| ------------- | ------------- |
| [csv/](./csv) | Folder with `csv` files containing datasets |
| [directions-basic](./directions-basic.ipynb)|  Jupyter notebook: extracting some basic information about plays|
| [means-merged-fetures](./means-merged-fetures.ipynb)| Jupyter notebook: mean POS counts, and merging with another dataset |
|[basic-clustering](./basic-clustering.ipynb)|First attempts to normalize directions, plot them and run clustering|



## What is this all about?
This is a repo with the code to my 3rd year coursework. Its title is _Linguistic Evolution of Stage Directions Between the 18th and 20th Centuries_, so it's going to be all stage directions and all linguistic :)

### What I want to achieve
A great result would be the classification of stage directions according to TEI-5 markup convention. It looks as this:

* setting,
* entrance,
* exit,
* business,
* novelistic,
* delivery,
* modifier,
* location,
* mixed.

More info here: http://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-stage.html

## "Roadmap" and current state-of-affairs
- [x] get the corpus from the repository
- [x] extract basic information
- [x] get mean values of different parts-of-speech
- [ ] _in process:_ try visualize the data (because why not)
- [ ] _in process:_ annotate some directions
- [ ] try run a Decision Tree / Random Forest / PCA / kNN / something else
- [ ] write a paper
- [ ] present it

### Deadlines
1. _Somewhere around **May 18th**_ — sharing the paper with the reviewer,
2. __May 23rd__ — uploading the paper into the system,
3. __May 25th__ — presentation.

## Source corpus
I'm using RusDraCor. It can be explored on its [site](https://dracor.org/rus), and it's also possible to download it from its [Github repository](https://github.com/dracor-org/rusdracor).
