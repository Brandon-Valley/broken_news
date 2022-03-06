import cv2
import os
import subprocess

# from sms.txt_logger import txt_logger
from sms.logger import txt_logger

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
    
def get_mouth_shape_frame_dl_from_dat_file(in_dat_path):
    print('Creating mouth_shape_frame_dl from ', in_dat_path)
    line_l = txt_logger.read(in_dat_path)
    # print(line_l)

    mouth_shape_frame_dl = []
    
    # ignore 1st line
    for line in line_l[1:-1]:
        frame_num_str, mouth_shape_str = line.split(' ')
        
        mouth_shape_frame_dl.append(
                                        {
                                            'frame_num'  : int(frame_num_str),
                                            'mouth_shape': mouth_shape_str.upper()
                                        }
            
                                    )
    return mouth_shape_frame_dl

def animate_fish_head_test():  
    # write_mouth_shape_dat_file()
    pass
    
    
if __name__ == "__main__":
    print('start')
    # animate_fish_head_test()
    in_voice_file_path = os.path.join(SCRIPT_PARENT_DIR_PATH, 'fish.wav')
    out_dat_path = os.path.join(SCRIPT_PARENT_DIR_PATH, 'mouth_shapes.dat')
    fps = 24
    # write_mouth_shape_dat_file(in_voice_file_path, out_dat_path, fps)
    mouth_shape_frame_dl = get_mouth_shape_frame_dl_from_dat_file(out_dat_path)
    print(mouth_shape_frame_dl)

    print('done')