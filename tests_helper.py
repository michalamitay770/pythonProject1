import os


def is_sentence_has_more_than_half_duplications(sentence):
    wordsList = sentence.split()
    my_dict = {}
    for word in wordsList:
        if word in my_dict.keys():
            if my_dict[word] + 1 >= len(wordsList) // 2:
                return True
            else:
                my_dict[word] = my_dict[word] + 1
        else:
            my_dict[word] = 1
    return False


def clean_path_and_executes_super_hero_creator(path, number):
    for f in os.listdir(path):
        os.remove(os.path.join(path, f))
    shell = 'python super_hero_creator.py ' + path + ' ' + str(number)
    print("Shell", shell)
    os.system(shell)


def get_all_super_hero_json_files_at_path(path):
    json_files_list = []
    for root, dirs, files in os.walk(path):
        for filename in files:
            if filename.startswith("SuperHero") and filename.endswith(".json"):
                json_files_list.append(filename)
    return json_files_list
