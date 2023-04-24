import cv2
import face_recognition

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    # Преобразование BGR-изображения в RGB-изображение
    rgb_frame = frame[:, :, ::-1]

    # Обнаружение лиц на изображении
    face_locations = face_recognition.face_locations(rgb_frame)

    # Рисование прямоугольников вокруг лиц на кадре
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    face_encodings = face_recognition.face_encodings(frame, face_locations)
    print(face_encodings)
    # Отображение кадра
    cv2.imshow('Video', frame)

    # Выход при нажатии клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождение ресурсов
video_capture.release()
cv2.destroyAllWindows()
