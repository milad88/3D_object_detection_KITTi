from read_point_cloud import *

LABELS_PATH = 'data_object_image_2/label_2'

IMAGE_TRAIN_PATH = 'data_object_image_2/training'
IMAGE_TEST_PATH = 'data_object_image_2/testing'

LIDAR_TRAIN_PATH = 'data_object_velodyne/training/velodyne'
LIDAR_TEST_PATH = 'data_object_velodyne/testing/velodyne'

CALIBRATION_TRAIN_PATH = 'data_scene_flow_calib/training/calib_velo_to_cam'
CALIBRATION_TEST_PATH = 'data_scene_flow_calib/testing/calib_velo_to_cam'
def load_data(n: int = None):
    data = []
    labels = []
    for i in range(n):
        x = get_lidar(LIDAR_TRAIN_PATH, i)
        y = get_label(LABELS_PATH, i)
        data.append(x)
        labels.append(y)
    return data, labels


if __name__ == '__main__':
    data, labels = load_data(100)
    print('end')
