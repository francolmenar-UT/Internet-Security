from os import system
from func import list_files
import re
from const import *

PRE_PROCESSED = False
PROCESSED = True
HUGE = False


def construct_pre():
    """
    Create the preprocessed files from the raw data
    :return:
    """
    files = list_files(raw_folder)

    for file_i in files:
        id_file = file_i.split(".")[1]  # Get the id of the file
        new_id_file = "pre" + id_file  # Get the id of the file
        cmd = nf_r + raw_folder + file_i + " > " + pre_folder + new_id_file + ".txt"  # Construct the command
        system(cmd)  # Execute


def construct_processed():
    """
    Create the processed files from the preprocessed files
    :return:
    """
    files = list_files(pre_folder)

    for file_i in files:
        if (file_i == ".DS_Store"):
            continue
        id_file = "pro" + file_i.split(".")[0]  # Get the id of the file

        text = open(pre_folder + file_i, 'r+').read()  # read file

        # Remove the arrow
        new_str = re.sub("->", '  ', text)

        # Remove the white spaces of the headers of the columns
        for i in range(len(old_header)):
            new_str = new_str.replace(old_header[i], no_space_header[i])

        # Add a new header
        new_str = new_str.replace(no_space_header[0], new_header[0] + ";" + new_header[1])

        new_str = new_str.replace('\n', "$")
        # Remove the white spaces and add ";" instead
        new_str = ';'.join(new_str.split())
        new_str = new_str.replace("$", '\n')

        file = open(post_folder + id_file + ".txt", "w")
        file.seek(0)
        file.write(new_str)
        file.truncate()
        file.close()


def construct_huge():
    files = list_files(post_folder)
    huge_str = ""

    output_file = open(huge_folder + huge_file, "w")
    output_file.seek(0)

    for i in range(len(files)):
        new_str = open(post_folder + files[0], 'r+').read()  # read file

        if i != 0:
            for j in range(len(new_header)):
                new_str = new_str.replace(new_header[j] + ";", "")

        output_file.write(new_str)
    output_file.close()


if PRE_PROCESSED: construct_pre()
if PROCESSED: construct_processed()
if HUGE: construct_huge()
