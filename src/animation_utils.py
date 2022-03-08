import cv2
import os
import subprocess
import ffmpeg

import get_google_img_of_each_frame_l

from sms.logger import txt_logger

SCRIPT_PARENT_DIR_PATH = os.path.abspath(os.path.dirname(__file__))
IMGS_DIR_PATH = os.path.join(SCRIPT_PARENT_DIR_PATH, '..', 'imgs')
MOUTH_SHAPE_IMGS_DIR_PATH = os.path.join(IMGS_DIR_PATH, 'mouth_shape_imgs')

RUN_DIR_PATH  = os.path.abspath(os.path.join(SCRIPT_PARENT_DIR_PATH, '..', 'run'))
NO_AUDIO_VID_PATH         = os.path.join(RUN_DIR_PATH, 'no_audio_vid.avi')
MOUTH_SHAPE_DAT_FILE_PATH = os.path.join(RUN_DIR_PATH, 'mouth_shapes.dat')

MOUTH_SHAPE_IMG_PATH_D = {
                            'MBP'  : os.path.abspath(os.path.join(MOUTH_SHAPE_IMGS_DIR_PATH, 'test_a.png')),
                            'ETC'  : os.path.abspath(os.path.join(MOUTH_SHAPE_IMGS_DIR_PATH, 'test_b.png')),
                            'E'    : os.path.abspath(os.path.join(MOUTH_SHAPE_IMGS_DIR_PATH, 'test_c.png')),
                            'AI'   : os.path.abspath(os.path.join(MOUTH_SHAPE_IMGS_DIR_PATH, 'test_d.png')),
                            'O'    : os.path.abspath(os.path.join(MOUTH_SHAPE_IMGS_DIR_PATH, 'test_e.png')),
                            'U'    : os.path.abspath(os.path.join(MOUTH_SHAPE_IMGS_DIR_PATH, 'test_f.png')),
                            'FV'   : os.path.abspath(os.path.join(MOUTH_SHAPE_IMGS_DIR_PATH, 'test_g.png')),
                            'L'    : os.path.abspath(os.path.join(MOUTH_SHAPE_IMGS_DIR_PATH, 'test_h.png')),
                            'REST' : os.path.abspath(os.path.join(MOUTH_SHAPE_IMGS_DIR_PATH, 'test_x.png'))
                         }
   
    
def write_mouth_shape_dat_file(in_voice_file_path, out_dat_path, fps):
    cmd = 'rhubarb -o {} {} -f dat --datFrameRate {} --datUsePrestonBlair'.format(out_dat_path, in_voice_file_path, fps)
    subprocess.call(cmd)
    
def get_mouth_shape_of_each_frame_l_from_dat_file(in_dat_path):
    print('Creating mouth_shape_frame_dl from ', in_dat_path)
    line_l = txt_logger.read(in_dat_path)
    # print(line_l)

    mouth_shape_frame_dl = []
    
    # ignore 1st line
    for line in line_l[1:]:
        frame_num_str, mouth_shape_str = line.split(' ')
        
        mouth_shape_frame_dl.append(
                                        {
                                            'frame_num'  : int(frame_num_str),
                                            'mouth_shape': mouth_shape_str.upper()
                                        }
        
                                    )
    print(mouth_shape_frame_dl)
        
        
    # build mouth_shape_of_each_frame_l
    mouth_shape_of_each_frame_l = []
    for dl_num, dl in enumerate(mouth_shape_frame_dl):
        if dl_num != len(mouth_shape_frame_dl) - 1:
            next_dl = mouth_shape_frame_dl[dl_num + 1]
            num_cur_mouth_shape_frames = next_dl['frame_num'] - dl['frame_num']
            # print('num_cur_mouth_shape_frames: ', num_cur_mouth_shape_frames)
            
            for x in range(num_cur_mouth_shape_frames):
                mouth_shape_of_each_frame_l.append(dl['mouth_shape'])
        
        
    return mouth_shape_of_each_frame_l

def write_vid_no_audio(mouth_shape_of_each_frame_l, in_voice_file_path, fps, out_vid_path):  
    # build frame_l
    frame_l = []
    for mouth_shape_key in mouth_shape_of_each_frame_l:
        mouth_shape_img_path = MOUTH_SHAPE_IMG_PATH_D[mouth_shape_key]
        frame_l.append(cv2.imread(mouth_shape_img_path))
        
    # print(frame_l)
    height, width, _ = frame_l[0].shape
    out = cv2.VideoWriter(out_vid_path, cv2.VideoWriter_fourcc(*'DIVX'), fps, (width, height))
    [out.write(f) for f in frame_l]
    out.release()
    
    
def add_audio_to_vid(in_vid_no_audio_path, in_audio_path, out_vid_w_audio_path, fps):
#     pass
# def test_ffmpeg(video_path, audio_path, output_path='output-ffmpeg.mp4', fps=24):
    

    print('--- ffmpeg ---')

    video  = ffmpeg.input(in_vid_no_audio_path).video # get only video channel
    audio  = ffmpeg.input(in_audio_path).audio # get only audio channel
    output = ffmpeg.output(video, audio, out_vid_w_audio_path, vcodec='copy', acodec='aac', strict='experimental')
    ffmpeg.run(output, overwrite_output = True)
    

def write_vid_from_voice_clip(in_voice_file_path, fps, script_str, out_vid_path, num_google_imgs_per_sec):
    # NO_AUDIO_VID_PATH
    print('Writing mouth shape dat file: ', MOUTH_SHAPE_DAT_FILE_PATH)
    write_mouth_shape_dat_file(in_voice_file_path, MOUTH_SHAPE_DAT_FILE_PATH, fps)
    
    print('Getting mouth_shape_of_each_frame_l from date file: ', MOUTH_SHAPE_DAT_FILE_PATH)
    mouth_shape_of_each_frame_l = get_mouth_shape_of_each_frame_l_from_dat_file(MOUTH_SHAPE_DAT_FILE_PATH)
    print(mouth_shape_of_each_frame_l)
    
    print('Getting google_img_of_each_frame_l...')
    num_frames = len(mouth_shape_of_each_frame_l)
    google_img_of_each_frame_l = get_google_img_of_each_frame_l.get_google_img_of_each_frame_l(num_frames, fps, script_str, num_google_imgs_per_sec)
    
    print("Writing NO AUDIO vid to: ", NO_AUDIO_VID_PATH)
    write_vid_no_audio(mouth_shape_of_each_frame_l, in_voice_file_path, fps, NO_AUDIO_VID_PATH)
    
    print('Adding Audio...')
    add_audio_to_vid(NO_AUDIO_VID_PATH, in_voice_file_path, out_vid_path, fps)
    
    
    
    
    
if __name__ == "__main__":
    print('start')
    
    in_voice_file_path = os.path.join(SCRIPT_PARENT_DIR_PATH, 'fish.mp4')
    out_dat_path = os.path.join(SCRIPT_PARENT_DIR_PATH, 'mouth_shapes.dat')
    fps = 24
    out_vid_no_audio_path = os.path.join(SCRIPT_PARENT_DIR_PATH, 'fish_vid_no_audio.avi')
    out_vid_w_audio_path    = os.path.join(SCRIPT_PARENT_DIR_PATH, 'fish_vid_final.avi')
    script_str = "Breaking news! Russian customs officials said they had detained"

    
    # # write_mouth_shape_dat_file(in_voice_file_path, out_dat_path, fps)
    # mouth_shape_of_each_frame_l = get_mouth_shape_of_each_frame_l_from_dat_file(out_dat_path)
    # print(mouth_shape_of_each_frame_l)
    #
    # write_vid_no_audio(mouth_shape_of_each_frame_l, in_voice_file_path, fps, out_vid_no_audio_path)
    #
    # add_audio_to_vid(out_vid_no_audio_path, in_voice_file_path, out_vid_w_audio_path, fps)
    
    
    write_vid_from_voice_clip(in_voice_file_path, fps, script_str, out_vid_w_audio_path)

    print('done')