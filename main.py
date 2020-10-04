import os


def create_projectdir(directory):
    if not os.path.exists(directory):
        print("Creating Directory.. " + directory)
        os.makedirs(directory)
    else:
        print("Directory Already Exists!!")


def write_file(path, data):
    with open(path, 'w') as f:
        f.writelines(data)


# create_projectdir('websites')
def createdatafiles(proj_name, base_url):
    queue = proj_name + '/queues.txt'
    crawled = proj_name + '/crawles.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.exists(crawled):
        write_file(crawled, '')


def append_to_file(path, data):
    with open(path, 'a') as f:
        f.write(data + '\n')


def delete_file_contents(path):
    with open(path, 'w'):
        pass


# createdatafiles('websites', 'https://jjnanthakumar.github.io/')
def file_to_set(fname):
    data = set()
    with open(fname, 'rt') as f:
        for line in f:
            data.add(line.replace('\n', ''))
    return data


def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)
