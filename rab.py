import cv2
from simple_facerec import SimpleFacerec
import smtplib

# Установка адрес электронной почты отправителя, адрес электронной почты получателя и пароль отправителя
sender_email = "jkseikvgeg06@gmail.com"
receiver_email = "varvrkyrveotve@gmail.com"
sender_password = "jznurwnizdkxazzy"

# Установите имена конкретных людей, чье обнаружение приведет к отправке письма
target_name1 ="Mikhail Puhlyakov" 
target_name2="Irina Anatol'evna"
target_name3="unknown"

sfr = SimpleFacerec()
sfr.load_encoding_images("C:/Users/Mischan/Desktop/VKR/images/")

cap = cv2.VideoCapture(0)
message_sent1 = False  # Флаг, указывающий, было ли уже отправлено сообщение для target_name1
message_sent2 = False  # Флаг, указывающий, было ли уже отправлено сообщение для target_name2

# Ожидание открытия окна с камерой
ret, frame = cap.read()
cv2.imshow('Camera', frame)

while True:
    ret, frame = cap.read()

    # Фиксация лица
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

    # Отображение кадра с камеры в реальном времени
    cv2.imshow('Camera', frame)

    # Если конкретное имя обнаружено, отправьте письмо, если это еще не было сделано
    if name == target_name1 and not message_sent1:
            message = f"Subject:Пухляков Михаил обнаружен!\n\nПухляков Михаил вышел на работу. Ранее были выявлены нарушения. "
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, receiver_email, message.encode('utf-8'))
            message_sent1 = True  # Установка флаг в True, чтобы не отправлять сообщение снова
    elif name == target_name2 and not message_sent2:
            message = f"Subject:Ирина Анатольевна обнаружена!\n\nИрина Анатольевна Лучший дипломный руководитель "
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, receiver_email, message.encode('utf-8'))
            message_sent2 = True  # Установка флаг в True, чтобы не отправлять сообщение снова
    elif name != target_name1 and name != target_name2 and name != target_name3:
            message = f"Subject:Unknown Person Detected!\n\n Неизвестный проник на территорию."
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, receiver_email, message.encode('utf-8'))

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()