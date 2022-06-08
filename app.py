from genericpath import isfile
from dotenv import load_dotenv
from os import getenv, unlink, listdir
from os.path import join, isfile
import logging
from mega import Mega

# Set up logging
logging.basicConfig(filename='logs.txt', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Setting up object for mega drive
load_dotenv()
EMAIL = getenv('EMAIL')
PASSWORD = getenv('PASSWORD')

mega = Mega()
m = mega.login(EMAIL, PASSWORD)

def main():
    # getting the contents of the folders (to be uploaded)
    youtube_raw_path = "C:/Users/djang/Videos/youtube_raw/"
    youtube_raw_files =  [join(youtube_raw_path, f) for f in listdir(youtube_raw_path) if isfile(join(youtube_raw_path, f)) ]

    youtube_finished_path = "C:/Users/djang/Videos/youtube_finished/"
    youtube_finished_files =  [join(youtube_finished_path, f) for f in listdir(youtube_finished_path) if isfile(join(youtube_finished_path, f)) ]

    # Uploading the files 
    try:
        mega_youtube_raw_folder = m.find('youtube_raw')
        mega_youtube_finished_folder = m.find('youtube_finished')

        for f in youtube_raw_files:
            m.upload(f, mega_youtube_raw_folder[0])
            unlink(f)

        for f in youtube_finished_files:
            m.upload(f, mega_youtube_finished_folder[0])
            unlink(f)

    except Exception as e:
        logging.error(e)


if __name__ == "__main__":
    main()