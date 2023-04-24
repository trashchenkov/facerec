import cv2
import face_recognition

# Загрузка изображения с известными лицами и их имена
image_of_me = face_recognition.load_image_file('face.png')
my_face_encoding = face_recognition.face_encodings(image_of_me)[0]
known_face_encodings = [my_face_encoding]
known_face_names = ["Sergei"]

# Инициализация переменных
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

# Считывание видеопотока
video_capture = cv2.VideoCapture(0)

while True:
    # Захват каждого кадра видеопотока
    ret, frame = video_capture.read()


    if process_this_frame:
        # Обнаружение всех лиц и их кодирование
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)


        face_names = []
        for face_encoding in face_encodings:
            # Сравнение лица с известными лицами
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # Если найдено совпадение, выбираем имя известного лица
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Отображение результатов на кадре
    for (top, right, bottom, left), name in zip(face_locations, face_names):


        # Рисование прямоугольника вокруг лица и отображение имени
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (0, 255, 255), 1)

    # Отображение кадра
    cv2.imshow('Video', frame)

    # Прерывание цикла при нажатии на клавишу 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()

