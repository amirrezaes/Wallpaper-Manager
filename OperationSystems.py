import os
import ctypes # for windows api
import subprocess  # for linux and mac

path = os.path.dirname(os.path.abspath(__file__)) + '/images'

class Operationsystem:
    def __init__(self):
        pass

    def add_image(self, image):
        with open(path, 'wb') as file:
            file.write(image)
    def remove_all_images(self):
        for file in os.listdir(path):
            os.remove(os.path.join(path, file))
        


class Windows(Operationsystem):
    def change_bg(self, image):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path+"\\"+image , 0)


class Linux(Operationsystem):
    def change_bg(image):
        subprocess.Popen(f"DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{path + '/' + image}", shell=True)

class Mac(Operationsystem):
    def change_bg(image):
        subprocess.Popen(f"""osascript -e 'tell application "Finder" to set desktop picture to POperationsystemIX file "{path + '/' + image}"'""", shell=True)
