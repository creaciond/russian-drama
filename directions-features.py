from pymorphy2.tokenizers import simple_word_tokenize
from pymorphy2 import MorphAnalyzer
import os


def count_words(directions):
    len_dirs = []
    for dir in directions:
        len_dirs.append(len(simple_word_tokenize(dir)))
    return len_dirs


def count_POS(directions):
    morph = MorphAnalyzer()
    nouns = []
    adjectives = []
    verbs = []
    adverbs = []
    interjections = []
    for direction in directions:
        dir_nouns = 0
        dir_adjs = 0
        dir_verbs = 0
        dir_advbs = 0
        dir_intjs = 0
        words = simple_word_tokenize(direction)
        for word in words:
            this_pos = morph.parse(word)[0].tag.POS
            if "NOUN" == this_pos:
                dir_nouns += 1
                # nouns[i] = (nouns[i] + 1) if nouns[i] else 1
            elif ("ADJF" == this_pos) or ("ADJS" == this_pos):
                # adjectives[i] = (adjectives[i] + 1) if adjectives[i] else 1
                dir_adjs += 1
            elif ("VERB" == this_pos) or ("INFN" == this_pos):
                # verbs[i] = (verbs[i] + 1) if verbs[i] else 1
                dir_verbs += 1
            elif "ADVB" == this_pos:
                # adverbs[i] = (adverbs[i] + 1) if adverbs[i] else 1
                dir_advbs += 1
            elif "INTJ" == this_pos:
                # interjections[i] = (interjections[i] + 1) if interjections[i] else 1
                dir_intjs += 1
        nouns.append(dir_nouns)
        adjectives.append(dir_adjs)
        verbs.append(dir_verbs)
        adverbs.append(dir_advbs)
        interjections.append(dir_intjs)
    return nouns, adjectives, verbs, adverbs, interjections


def save_data(data_folder, name, directions, length, nouns, adjs, verbs, advbs, intjs):
    file_name = name[:-4]
    data_path = data_folder + os.sep + file_name + ".tsv"
    with open(data_path, "w", encoding="utf-8") as data_file:
        for i in range(len(directions)):
            line = "{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(directions[i], length[i], nouns[i], adjs[i], verbs[i], advbs[i], intjs[i])
            if i == len(directions) - 1:
                line = line.strip("\n")
            data_file.write(line)
    print("data from file {} saved to {}".format(file_name[:file_name.index("_")], data_path))


def main():
    directions_folder = ".." + os.sep + "directions"
    # create folder for data (if not any)
    data_folder = ".." + os.sep + "data"
    if not os.path.exists(data_folder):
        os.mkdir(data_folder)

    for dir_file in [file for file in os.listdir(directions_folder) if file.endswith(".txt")]:
        # read directions
        with open(directions_folder + os.sep + dir_file, "r", encoding="utf-8") as dir_src:
            directions = [line.strip("\n") for line in dir_src.readlines()]

        # extract numbers
        directions_length = count_words(directions)
        nouns, adjectives, verbs, adverbs, interjections = count_POS(directions)

        # save
        save_data(data_folder, dir_file, directions, directions_length, nouns, adjectives, verbs, adverbs, interjections)




if __name__ == "__main__":
    main()