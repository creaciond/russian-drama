import os
import re


def save_directions(directions, dir_folder, file_name):
    play_name = file_name[:-4]
    dir_path = dir_folder + os.sep + play_name + ".txt"
    with open(dir_path, "w", encoding="utf-8") as dir_file:
        dir_file.write("\n".join(directions))
    print("directions from {} saved to {}".format(play_name, dir_path))


def extract_directions(play_path):
    reg_direction = re.compile("<stage.*?>(.*?)<\/stage>", flags=re.MULTILINE)
    reg_spaces = re.compile("\s{2,}")
    with open(play_path, "r", encoding="utf-8") as play_source:
        play = play_source.read()
    play = reg_spaces.sub(" ", play)
    directions = re.findall(reg_direction, play)
    return directions


def crawl_corpus_for_directions(corpus_path, directions_path):
    plays = [file for file in os.listdir(corpus_path) if file.endswith(".xml")]
    for play in plays:
        directions = extract_directions(corpus_path + os.sep + play)
        save_directions(directions, directions_path, play)


def main():
    corpus_path = ".." + os.sep + "RusDraCor"
    # path for data
    directions_path = ".." + os.sep + "directions"
    if not os.path.exists(directions_path):
        os.mkdir(directions_path)
    # extract directions and save them
    crawl_corpus_for_directions(corpus_path, directions_path)


if __name__ == "__main__":
    main()