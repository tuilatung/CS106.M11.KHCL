import os
import shutil

directories = [
    "00Uncorrelated",
    "01WeaklyCorrelated",
    "02StronglyCorrelated",
    "03InverseStronglyCorrelated",
    "04AlmostStronglyCorrelated",
    "05SubsetSum",
    "06UncorrelatedWithSimilarWeights",
    "07SpannerUncorrelated",
    "08SpannerWeaklyCorrelated",
    "09SpannerStronglyCorrelated",
    "10MultipleStronglyCorrelated",
    "11ProfitCeiling",
    "12Circle"
    ]

sub_folders = [
    "n00050",
    "n00100",
    "n00500",
    "n01000",
    "n05000"
]

sub_sub_folder = "R10000" # the sub folder needs to remove


"""
    IMPORTANT: This script is for the full dataset that is cloned from 
        https://github.com/likr/kplib
"""

dir_dataset = os.path.join("e:\CS106.M11.KHCL\Assignment_2", "kplib")

def remove(path):
    """ param <path> could either be relative or absolute. """
    if os.path.isfile(path) or os.path.islink(path):
        os.remove(path)  # remove the file
    elif os.path.isdir(path):
        shutil.rmtree(path)  # remove dir and all contains
    else:
        raise ValueError("file {} is not a file or dir.".format(path))


def remove_directories():
    # for remove directories
    for item in directories:
        for sub_item in sub_folders:
            remove(os.path.join(dir_dataset, item, sub_item, sub_sub_folder))
            print("=================DONE==================")


def remove_files():
    # for remove files
    for item in directories:
        for sub_item in sub_folders:
            tmp = os.path.join(dir_dataset, item, sub_item, "R01000")
            for file in os.listdir(tmp):
                if file != "s000.kp": # except s000.kp file
                    remove(os.path.join(tmp, file))


def count_all_files():
    count = 0
    for item in directories:
        for sub_item in sub_folders:
            tmp = os.path.join(dir_dataset, item, sub_item, "R01000");
            for file in os.listdir(tmp):
                count += 1
    print(count)

# Driver code
if __name__ == '__main__':
    # remove_directories()
    # remove_files()
    count_all_files() # make sure the total are 65 files. Because 13 x 5 = 65 (every folder we get 5 test cases)


