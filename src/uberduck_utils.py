import uberduckapi as ud
import os

from sms.file_system_utils import file_system_utils as fsu

def write_voice_clip(out_audio_file_path, script_str, voice_name_str = 'fish-head'):
    out_audio_file_parent_dir_path = fsu.get_abs_path_to_parent_dir_of_file(out_audio_file_path)
    fsu.make_dir_if_not_exist(out_audio_file_parent_dir_path)
    
    my_duck = ud.UberDuck(os.environ['UBERDUCK_Key'], os.environ['UBERDUCK_Secret'])
    # voice = my_duck.get_voice('fish-head', "... Breaking news! Russian customs officials said they had detained a star American basketball player after finding hashish oil in her luggage at an airport near Moscow. ... ... The Russian news agency has identified the player as Brittney Griner.")
    voice = my_duck.get_voice(voice_name_str, script_str)

    if voice:
        voice.save(out_audio_file_path)
    else:
        raise Exception("ERROR: Voice not read from Uberduck API Correctly")
    
    
if __name__ == "__main__":
    SCRIPT_PARENT_DIR_PATH = os.path.abspath(os.path.dirname(__file__))
    OUT_AUDIO_FILE_PATH = os.path.join(SCRIPT_PARENT_DIR_PATH, 'fish_head_voice_clip_test.mp4')
    script_str = "Breaking news! Russian customs officials said they had detained a star American basketball player after finding hashish oil in her luggage at an airport near Moscow. ... ... The Russian news agency has identified the player as Brittney Griner."
    write_voice_clip(OUT_AUDIO_FILE_PATH, script_str, 'fish-head')
    print('done')
