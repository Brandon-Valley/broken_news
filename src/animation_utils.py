import cv2
import os

SCRIPT_PARENT_DIR_PATH = os.path.abspath(os.path.dirname(__file__))
IMGS_DIR_PATH = os.path.join(SCRIPT_PARENT_DIR_PATH, '..', 'imgs')

FRAME_1_FILE_PATH = os.path.join(IMGS_DIR_PATH, 't1.png')
FRAME_2_FILE_PATH = os.path.join(IMGS_DIR_PATH, 't1_bw.png')


frames = [cv2.imread(FRAME_1_FILE_PATH),
          cv2.imread(FRAME_2_FILE_PATH),
          cv2.imread(FRAME_1_FILE_PATH),
          cv2.imread(FRAME_2_FILE_PATH),
          cv2.imread(FRAME_1_FILE_PATH)
         ]

height, width, _ = frames[0].shape
out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'DIVX'), 1, (width, height))
[out.write(f) for f in frames]
out.release()

print('done')