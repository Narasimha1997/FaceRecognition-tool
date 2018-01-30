import numpy
import face_recognition
import os
from threading import Thread


class Encode(Thread):

    def __init__(self, image_file, target_dir):
        Thread.__init__(self)
        self.image_file = image_file
        self.target_dir = target_dir
        pass
    
    def save_array(self, encodings, image_file_name):
        if not os.path.exists(self.target_dir):
            os.mkdir(self.target_dir)
        numpy.save(self.target_dir+'/'+image_file_name, encodings)
    
    def run(self):
        #generate encoding and save them as numpy arrays:
        face_name = (self.image_file.split('/')[1]).split('.')[0]
        print('Encoding face for: ', face_name)
        image = face_recognition.load_image_file(self.image_file)
        encodings = face_recognition.face_encodings(image)
        self.save_array(numpy.array(encodings), image_file_name = face_name)
        print('Finished encoding', face_name)

def encode_all_faces():
    for file_ in os.listdir('./KnownFaces'):
        if file_.endswith('.jpg') or file_.endswith('.png'):
            Encode(image_file = ('KnownFaces/'+file_), target_dir = 'Encodings').start()


def encode_single(filename):
    if  not os.path.exists(os.path.join('KnownFaces', filename)):
        print('No such image, (face) found')
        return
    Encode(image_file = os.path.join('KnownFaces', filename), target_dir = 'Encodings').start()


class InitlaizeEncodingsOfKnownFaces():
    #Should be executed synchronously
    #returns a array of dicts, containing <"FaceName" : embedding_vector> as Key, Values
    def __init__(self, encoding_directory):
        self.encoding_directory = encoding_directory

    def genEncodings(self):
        encodings = []
        for files in os.listdir(self.encoding_directory):
            FNAME  = files.split('.')[0]
            encodings.append(
                {FNAME : numpy.load(self.encoding_directory+'/'+files)}
            )
        return encodings
    

            