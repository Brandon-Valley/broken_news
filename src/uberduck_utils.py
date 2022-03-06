import uberduckapi as ud
import os

def write_voice_clip(out_audio_file_path, script_str, voice_name_str = 'fish-head'):
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
    script_str = "... Breaking news! Russian customs officials said they had detained a star American basketball player after finding hashish oil in her luggage at an airport near Moscow. ... ... The Russian news agency has identified the player as Brittney Griner."
    # script_str = "Breaking news! Russian customs officials "
    write_voice_clip(OUT_AUDIO_FILE_PATH, script_str, 'fish-head')
    print('done')
