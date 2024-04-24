from mineget import Loader
from mineget import printing
import requests
import os
import rich

class Downloader:
    def __init__(self): pass
    
    def _download_file(self, url: str, save_to: str = 'downloaded_file'):
        if os.path.exists(save_to):
            if os.path.isfile(save_to):
                rich.print(printing.get_overwriting_warning(
                    os.path.realpath(save_to)
                ), end=' ')
                if not printing.input_y_or_n():
                    rich.print(printing.get_quitting_message())
                    raise KeyboardInterrupt
            elif os.path.isdir(save_to):
                rich.print(printing.format_as_error(printing.get_folder_error()))
                rich.print(printing.get_quitting_message())
                raise KeyboardInterrupt
            
        with requests.get(url, stream=True) as request:
            request.raise_for_status()
            with open(save_to, 'wb') as file_:
                for chunk in request.iter_content(chunk_size=1024):
                    file_.write(chunk) # TODO
                
    
    def download(self, name: str, version: str, loader: Loader) -> None: pass
