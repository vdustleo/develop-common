# -*- coding: utf-8 -*-
import os
import random

def read_random_size(filepath, start, size):
    f = open(file_path, 'rb')
    f.seek(start, os.SEEK_CUR)
    k = f.read(size)
    print f.tell()
    f.close()
    return k

if __name__ == "__main__":
    file_path = u'e:\GHOST\C_WIN7.GHO'
    file_path = u'e:\\music\\ape\\[一致公认最发烧人声试音天碟3蔡琴HDCD].CDImage.ape'

    file_size = os.path.getsize(file_path)
    print(file_size)
    rint = random.randint(1, 100000)
    rint_size = random.randrange(1, 10) * 1024
    print rint, rint_size
    read_random_size(file_path, rint,  rint_size)
