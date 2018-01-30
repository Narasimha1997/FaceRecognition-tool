import cv2

NAME = "Sudha"

camera = cv2.VideoCapture(0)
import Encodings

while True:

    _, frame = camera.read()
    cv2.imwrite("KnownFaces/"+NAME+'.jpg', frame)
    cv2.imshow("Press q to save, quit and generate encoding", frame)
    if cv2.waitKey(20) & 0xFF = ord('q'):
        Encodings.encode_single(filename = 'KnownFaces/'+NAME+'.jpg')
        print('Image captured and finsished generating encoding for it, now run RealTime.py')


