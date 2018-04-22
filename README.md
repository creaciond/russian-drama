# Stage Directions in Russian Drama


> <h3> Stage directions, quite literally, don't count. </h3>
>   
> In: Hardin L. Aasand (ed.): *Stage Directions in Hamlet. New essays and new directions.* Madison et al. 2003, p. 226. 

## What's in the repo?

| File/folder      | What's inside |
| ------------- | ------------- |
| [csv/](./csv) | Folder with `csv` files containing datasets |
| [directions-basic.ipynb](./directions-basic.ipynb)| Extracting some basic information about plays |
| [means-merged-fetures.ipynb](./means-merged-fetures.ipynb)| Mean POS counts, merging with another dataset |
| [basic-clustering.ipynb](./basic-clustering.ipynb)| First attempts to normalize directions, plot them and run clustering|
| [plot-plays.ipynb](./plot-plays.ipynb)| Drawing different plots visualising the data we got|



## What is this all about?
This is a repo with the code to my 3rd year coursework. Its title is _Linguistic Analysis of Stage Directions in Russian Drama from the 18th to the 20th Century_, so it's going to be all stage directions and all linguistic :)

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
