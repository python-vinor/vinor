import os


def scandir(absolute_path):
    file_token = ''
    for root, dirs, files in os.walk(absolute_path):
        tree = {d: scandir(os.path.join(root, d)) for d in dirs}
        tree.update({f: file_token for f in files})
        return tree  # note we discontinue iteration trough os.walk
