import os
import numpy as np
from object3d import Object3d


def read_pcd(filepath):
    lidar = []
    with open(filepath, 'rb') as f:
        line = f.readline().strip()
        while line:
            linestr = line.split(" ")
            if len(linestr) == 4:
                linestr_convert = list(map(float, linestr))
                lidar.append(linestr_convert)
            line = f.readline().strip()
    return np.array(lidar)


def load_velo_scan(velo_filename):
    scan = np.fromfile(velo_filename, dtype=np.float32)
    scan = scan.reshape((-1, 4))
    return scan


def get_lidar(path, idx):
    lidar_filename = os.path.join(path, '%06d.bin' % (idx))
    return load_velo_scan(lidar_filename)


def read_label(label_filename):
    lines = [line.rstrip() for line in open(label_filename)]
    objects = [Object3d(line) for line in lines]
    return objects


def get_label(path, idx):
    lidar_filename = os.path.join(path, '%06d.txt' % (idx))
    return read_label(lidar_filename)

# if __name__ == '__main__':
#
#     x = load_velo_scan('data_object_image_2/000000.bin')
#     print('s')
