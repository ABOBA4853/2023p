import cv2
from PIL import Image
class RecognizeImg:
    def __init__(self, path:str):
        self.Path = path
        self.Image = cv2.imread(self.Path)
        self.MultiScale = []
    def ShowImg(self, name:str):
        cv2.imshow(name, self.Image)
        cv2.waitKey()
    def GetCoordinates(self, fileName:str):
        cascade = cv2.CascadeClassifier(fileName)
        self.MultiScale = cascade.detectMultiScale(self.Image)
    def HighLigth(self):
        for (x, y, w, h) in self.MultiScale:
            cv2.rectangle(self.Image, (x,y), (x + w, y + h), (0,0,255), 10)
    def AddImage(self, path:str, newPhotoPath:str):
        try:
            fLayout = Image.open(self.Path)
            sLayout = Image.open(path)
            converted_fLayout = fLayout.convert('RGBA')
            converted_sLayout = sLayout.convert('RGBA')
            for (x, y, w, h) in self.MultiScale:
                converted_sLayout = converted_sLayout.resize((w, int(h / 4)))
                converted_fLayout.paste(converted_sLayout, (x, int(y + h / 3)), converted_sLayout)
                converted_fLayout.save(newPhotoPath)
                self.Image = cv2.imread(newPhotoPath)
        except Exception as ex:
            print(ex)

