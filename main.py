import json
import os
from tests_helper import *

def test1_validate_created_files_number(path, number):
    json_files_count = 0
    logs_files_count = 0
    for root, dirs, files in os.walk(path):
        for filename in files:
            if filename.startswith("SuperHero"):
                if filename.endswith(".json"):
                    json_files_count += 1
                elif filename.endswith(".log"):
                    logs_files_count += 1
    assert json_files_count == number and logs_files_count == number


def test2_validate_id_grather_or_equals_to_one(path):
    json_files_list = get_all_super_hero_json_files_at_path(path)
    for filename in json_files_list:
        f = open(path + "/" + filename)
        data = json.load(f)
        assert data["id"] >= 1


def test3_validate_isEvil_field(path):
    json_files_list = get_all_super_hero_json_files_at_path(path)
    for filename in json_files_list:
        f = open(path + "/" + filename)
        data = json.load(f)
        print(filename)
        if is_sentence_has_more_than_half_duplications(data["Catchphrase"]) == True:
            assert data["IsEvil"] == True
        else:
            assert data["IsEvil"] == False

#main
path = "/Users/michal.amitay/PycharmProjects/pythonProject1/target"
number = 4
clean_path_and_executes_super_hero_creator(path, number)
print("test1- validate created files number result:")
test1_validate_created_files_number(path, number)
print("test2- validate that there is no superhero with id smaller than 1:")
test2_validate_id_grather_or_equals_to_one(path)
print("test3- Validate isEvil field:")
test3_validate_isEvil_field(path)