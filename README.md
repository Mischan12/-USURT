Импорты библиотек

python
Copy code
import cv2
from simple_facerec import SimpleFacerec
import smtplib
Импортируются библиотеки OpenCV (cv2) для работы с видео и изображениями, SimpleFacerec для распознавания лиц и smtplib для отправки электронной почты.

Установка адресов электронной почты и пароля

python
Copy code
sender_email = "jkseikvgeg06@gmail.com"
receiver_email = "varvrkyrveotve@gmail.com"
sender_password = "jznurwnizdkxazzy"
Устанавливаются адреса электронной почты отправителя и получателя, а также пароль отправителя.

Установка имен конкретных людей

python
Copy code
target_name1 ="Mikhail Puhlyakov" 
target_name2="Irina Anatol'evna"
target_name3="unknown"
Устанавливаются имена конкретных людей, чье обнаружение приведет к отправке письма.

Инициализация SimpleFacerec

python
Copy code
sfr = SimpleFacerec()
sfr.load_encoding_images("C:/Users/Mischan/Desktop/VKR/images/")
Создается объект SimpleFacerec и загружаются изображения для обучения модели распознавания лиц.

Установка видеокамеры

python
Copy code
cap = cv2.VideoCapture(0)
Устанавливается видеокамера (индекс 0 означает стандартную камеру устройства).

Флаги отправки сообщений

python
Copy code
message_sent1 = False  
message_sent2 = False  
Устанавливаются флаги, указывающие, было ли уже отправлено сообщение для target_name1 и target_name2 соответственно.

Чтение кадра с камеры и отображение

python
Copy code
ret, frame = cap.read()
cv2.imshow('Camera', frame)
Читается кадр с камеры и отображается в окне с камерой.

Цикл чтения кадров с камеры и распознавания лиц

python
Copy code
while True:
    ret, frame = cap.read()
   ...
Начинается бесконечный цикл чтения кадров с камеры и распознавания лиц.

Распознавание лиц

python
Copy code
face_locations, face_names = sfr.detect_known_faces(frame)
for face_loc, name in zip(face_locations, face_names):
    y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
    cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
Распознаются лица на кадре, имена лиц выводятся на экран, а также рисуется прямоугольник вокруг лица.

Отправка писем

python
Copy code
if name == target_name1 and not message_sent1:
   ...
elif name == target_name2 and not message_sent2:
   ...
elif name!= target_name1 and name!= target_name2 and name!= target_name3:
   ...
Если обнаружено лицо, соответствующее одному из имен, и сообщение еще не было отправлено, то отправляется письмо с соответствующим текстом.

Завершение программы

python
Copy code
key = cv2.waitKey(1)
if key == 27:
    break
cap.release()
cv2.destroyAllWindows()
Программа завершается, если пользователь нажмет клавишу Esc (код 27). Затем освобождается ресурс видеокамеры и закрыты все окна.




