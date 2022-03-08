
from google_images_download import google_images_download 
from sms.file_system_utils import file_system_utils as fsu


import os # TEMP
SCRIPT_PARENT_DIR_PATH = os.path.abspath(os.path.dirname(__file__)) # temp !!!!!!!!!!!!!!!!!
test_img_dl_path = SCRIPT_PARENT_DIR_PATH + '//' + 'test_google_img_dl_dir'

def get_google_img_of_each_frame_l(num_frames, fps, script_str, num_google_imgs_per_sec):
    
    def dl_google_imgs(keywords_str, num_imgs, img_dl_dir_path, print_urls = False):
        
        response = google_images_download.googleimagesdownload()   #class instantiation
        
        args = {
                 # "keywords"        : keywords_str,
                 "keywords"        : keywords_str.replace(' ', '+'),
                 "limit"           : num_imgs,
                 "image_directory" : img_dl_dir_path,
                 "print_urls"      : print_urls
                }
        
        print('  Downloading google images...')
        response.download(args)   #passing the arguments to the function
        # print(paths)   #printing absolute paths of the downloaded images

    
    print('num_frames: ', num_frames)
    voice_clip_num_sec = num_frames / fps
    print('  Calculated length of voice_clip_num_sec to be # sec: ', voice_clip_num_sec)
    
    # round down
    num_google_imgs_needed = int(voice_clip_num_sec * num_google_imgs_per_sec)\
    
    print('Clearing imgs from prev. run if needed...')
    fsu.delete_if_exists(test_img_dl_path)
    fsu.make_dir_if_not_exist(test_img_dl_path)
    
    print('  Getting {} images from google...'.format(num_google_imgs_needed))
    dl_google_imgs(script_str, num_google_imgs_needed, test_img_dl_path)
    
    
if __name__ == '__main__':
    print('in main')
    # import main
    # main.main()
    #
    #
    # num_frames = 310
    # fps = 24
    # # script_str = "Breaking news! Russian customs officials said they had detained a star American basketball player after finding hashish oil in her luggage at an airport near Moscow. The Russian news agency has identified the player as Brittney Griner."
    # # script_str = "Breaking,news,Russian,customs"
    # script_str = "Polar bears,baloons,Beaches"
    # num_google_imgs_per_sec = 0.5
    #
    # get_google_img_of_each_frame_l(num_frames, fps, script_str, num_google_imgs_per_sec)
    
    from google_images_download import google_images_download   #importing the library

    response = google_images_download.googleimagesdownload()   #class instantiation
    
    arguments = {"keywords":"Polar bears,baloons,Beaches","limit":20,"print_urls":True}   #creating list of arguments
    paths = response.download(arguments)   #passing the arguments to the function
    print(paths)   #printing absolute paths of the downloaded images

    
    print('done')