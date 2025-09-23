import shutil
import os

def del_files():
    shutil.rmtree('./uploads/rgb')
    shutil.rmtree('./uploads/nir')
    # shutil.rmtree('./uploads/ndvi') 
    os.mkdir('./uploads/rgb')
    os.mkdir('./uploads/nir')
    # os.mkdir('./uploads/ndvi')
