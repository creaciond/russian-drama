# Stage Directions in Russian Drama


> <h3> Stage directions, quite literally, don't count. </h3>
>   
> In: Hardin L. Aasand (ed.): *Stage Directions in Hamlet. New essays and new directions.* Madison et al. 2003, p. 226.

## What is this all about?
This is a repo with the code to my 3rd year coursework. Its title is _Linguistic Analysis of Stage Directions in Russian Drama from the 18th to the 20th Century_, so it's going to be all stage directions and all linguistic :)

Check out my slides for EADH 2018 conference [here](https://drive.google.com/file/d/18eLKz6-E2wqjUUZNo5NrnwOSb00WfUNx/view?usp=sharing); basically, they cover everything I did for this course paper. 

### Work objectives
1. Perform some neat corpus analysis on the Russian Drama Corpus.

2. A great result would be the classification of stage directions according to the [TEI-5 markup standard](http://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-stage.html). According to it, stage directions have 9 types:

    * setting,
    * entrance,
    * exit,
    * business,
    * novelistic,
    * delivery,
    * modifier,
    * location,
    * mixed.

## What's in the repo?

|                        File/folder                          |                                What's inside                        |
| ----------------------------------------------------------- | ------------------------------------------------------------------- |
| [csv/](./csv)                                               | Comma-separated files with datasets                                 |
| [figures/](./figures)                                       | Figures from [plot-plays.ipynb](./plot-plays.ipynb)                 |
| [requirements.txt](./requirements.txt)                      | List of packages required to run the notebooks                      |
| [directions-basic.ipynb](./directions-basic.ipynb)          | Extracting some basic information about plays                       |
| [means-merged-features.ipynb](./means-merged-features.ipynb)| Mean POS counts, merging with another dataset                       |
| [plot-plays.ipynb](./plot-plays.ipynb)                      | Drawing different plots visualising the data we got                 |
| [classification.ipynb](./classification.ipynb)              | Classifying the directions into TEI-P5 types                        |
| [frequent-pos.ipynb](./frequent-pos.ipynb)                  | Most frequent parts of speech in the corpus                         |

### Dependencies
All the dependencies are listed in `requirements.txt`. As a sidenote: the majority of the packages are shipped with Anaconda. If you have it installed, you'll only need to install `nltk` by yourself, and also to download NLTK data after that. In Python, this should be as follows:

```python
import nltk
nltk.download()
```

## "Roadmap" and current state-of-affairs
- [x] get the corpus from the repository
- [x] extract basic information
- [x] get mean values of different parts-of-speech
- [x] try visualize the data (because why not)
- [x] annotate some directions
- [x] do machine learning experiments: ran kNN, Decision Tree, and Random Forest in [classification.ipynb](./classification.ipynb). 
- [x] write a paper
- [x] present the paper and the results with the handouts

### Deadlines
1. __May 18th__ — sharing the paper with the reviewer,
2. __May 22nd__ — uploading the paper into the system,
3. __May 25th__ — presentation.

## Source corpus
I'm using RusDraCor. It can be explored on its [site](https://dracor.org/rus), and it's also possible to download it from its [Github repository](https://github.com/dracor-org/rusdracor).
