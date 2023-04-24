import face_recognition
import cv2

image_of_me = face_recognition.load_image_file('face.png')
my_face_encoding = face_recognition.face_encodings(image_of_me)[0]
print(my_face_encoding)