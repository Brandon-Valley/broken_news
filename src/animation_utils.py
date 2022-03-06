import cv2
import os
import subprocess

SCRIPT_PARENT_DIR_PATH = os.path.abspath(os.path.dirname(__file__))
IMGS_DIR_PATH = os.path.join(SCRIPT_PARENT_DIR_PATH, '..', 'imgs')
MOUTH_SHAPE_DAT_FILE_PATH = os.path.join(SCRIPT_PARENT_DIR_PATH, '..', 'imgs')

MOUTH_SHAPE_IMG_FILE_PATH_MBP  = os.path.join(IMGS_DIR_PATH, 'test_a.png')
MOUTH_SHAPE_IMG_FILE_PATH_ETC  = os.path.join(IMGS_DIR_PATH, 'test_b.png')
MOUTH_SHAPE_IMG_FILE_PATH_E    = os.path.join(IMGS_DIR_PATH, 'test_c.png')
MOUTH_SHAPE_IMG_FILE_PATH_AI   = os.path.join(IMGS_DIR_PATH, 'test_d.png')
MOUTH_SHAPE_IMG_FILE_PATH_O    = os.path.join(IMGS_DIR_PATH, 'test_e.png')
MOUTH_SHAPE_IMG_FILE_PATH_U    = os.path.join(IMGS_DIR_PATH, 'test_f.png')
MOUTH_SHAPE_IMG_FILE_PATH_FV   = os.path.join(IMGS_DIR_PATH, 'test_g.png')
MOUTH_SHAPE_IMG_FILE_PATH_L    = os.path.join(IMGS_DIR_PATH, 'test_h.png')
MOUTH_SHAPE_IMG_FILE_PATH_REST = os.path.join(IMGS_DIR_PATH, 'test_x.png')



def test0():
    FRAME_1_FILE_PATH = os.path.join(IMGS_DIR_PATH, 't1.png')
    FRAME_2_FILE_PATH = os.path.join(IMGS_DIR_PATH, 't1_bw.png')
    
    
    frames = [cv2.imread(FRAME_1_FILE_PATH),
              cv2.imread(FRAME_2_FILE_PATH),
              cv2.imread(FRAME_1_FILE_PATH),
              cv2.imread(FRAME_2_FILE_PATH),
              cv2.imread(FRAME_1_FILE_PATH)
             ]
    
    fps = 1
    height, width, _ = frames[0].shape
    out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, (width, height))
    [out.write(f) for f in frames]
    out.release()
    
    
def write_mouth_shape_dat_file(in_voice_file_path, out_dat_path, fps):
    cmd = 'rhubarb -o {} {} -f dat --datFrameRate {} --datUsePrestonBlair'.format(out_dat_path, in_voice_file_path, fps)
    subprocess.call(cmd)
    

def animate_fish_head_test():  
    # write_mouth_shape_dat_file()
    pass
    
    
if __name__ == "__main__":
    print('start')
    # animate_fish_head_test()
    in_voice_file_path = os.path.join(SCRIPT_PARENT_DIR_PATH, 'fish.wav')
    out_dat_path = os.path.join(SCRIPT_PARENT_DIR_PATH, 'mouth_shapes.dat')
    fps = 24
    write_mouth_shape_dat_file(in_voice_file_path, out_dat_path, fps)

    print('done')