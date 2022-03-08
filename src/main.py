
import os
import uberduck_utils
import animation_utils

from sms.file_system_utils import file_system_utils as fsu


SCRIPT_PARENT_DIR_PATH = os.path.abspath(os.path.dirname(__file__))
RUN_DIR_PATH           = os.path.abspath(os.path.join(SCRIPT_PARENT_DIR_PATH, '..', 'run'))
VOICE_CLIP_FILE_PATH   = os.path.join(RUN_DIR_PATH, 'voice_clip.wav')
FINAL_VID_PATH         = os.path.join(RUN_DIR_PATH, 'final_vid.avi')

if __name__ == "__main__":
    
    # script_str = "Breaking news! Russian customs officials said they had detained a star American basketball player after finding hashish oil in her luggage at an airport near Moscow. The Russian news agency has identified the player as Brittney Griner."
    script_str = "Breaking news! Russian customs officials said they had detained"
    voice_name_str = 'fish-head'
    fps = 24
    
    print('Start')
    
    print('Deleting Run Dir: ', RUN_DIR_PATH)
    fsu.delete_if_exists(RUN_DIR_PATH)
    
    print('Writing voice clip to: ', VOICE_CLIP_FILE_PATH)
    uberduck_utils.write_voice_clip(VOICE_CLIP_FILE_PATH, script_str, voice_name_str)
    
    print('Writing Video from Voice Clip...')
    animation_utils.write_vid_from_voice_clip(VOICE_CLIP_FILE_PATH, fps, FINAL_VID_PATH)
    
    print('Done, final vid: ', FINAL_VID_PATH)