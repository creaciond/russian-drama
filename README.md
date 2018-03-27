# Stage Directions in Russian Drama
3rd year coursework

## What's in the repo?

| Notebook      | What's inside |
| ------------- | ------------- |
| [directions-basic](./directions-basic.ipynb)|  Extracting some basic information about plays|
| [means-merged-fetures](./means-merged-fetures.ipynb)| Mean POS counts, and merging with another dataset |


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

## Current state-of-affairs
- [x] get the corpus from the repository
- [x] extract basic information
- [x] get mean values of different parts-of-speech
- [ ] _in process:_ annotate some directions
- [ ] try run a Decision Tree / Random Forest
- [ ] write a paper
- [ ] nail it while presenting

## Source corpus
I'm using RusDraCor. It can be explored on its [site](https://dracor.org/rus), and it's also possible to download it from its [Github repository](https://github.com/dracor-org/rusdracor).
