from recognizeimg import RecognizeImg
path = 'cat.jpg'
windowName = 'Cat'
fileName = 'haarcascade_frontalcatface_extended.xml'
rec = RecognizeImg(path)

rec.GetCoordinates(fileName)
print(rec.MultiScale)
rec.HighLigth()

newPath = 'sunglasses1.png'
newPhotoPath = 'cat_with_sunglasses1.png'
windowName = 'Cat with sunglasses1'
rec.AddImage(newPath, newPhotoPath)
rec.ShowImg(windowName)
