import face_recognition
import cv2
from Encodings import InitlaizeEncodingsOfKnownFaces 
import itertools

video_capture = cv2.VideoCapture(0)

known_face_names = []; known_face_encodings = []

#simple preprocessor to load encodings:
face_data = InitlaizeEncodingsOfKnownFaces('Encodings').genEncodings()
for faces in face_data:
    for name, encoding in faces.items():
        known_face_encodings.append(list(encoding[0])); known_face_names.append(name)



face_locations = []
face_encodings = []
face_names = []
process_this_frame = True


while True:

    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "No Name!!"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255, 0, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite('TestOutput.jpg', frame)
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()