import cv2

# Inisialisasi recognizer wajah
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inisialisasi kamera
cap = cv2.VideoCapture(0)

while True:
    # Membaca frame dari kamera
    ret, frame = cap.read()

    # Konversi ke grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Mendeteksi wajah dalam frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Variabel untuk nomor orang
    person_number = 1

    # Menggambar kotak di sekitar wajah yang terdeteksi dan menambahkan deskripsi
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, 'P{}'.format(person_number), (x, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        person_number += 1

    # Menampilkan hasil
    cv2.imshow('Face Recognition', frame)

    # Menghentikan program jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Menutup kamera dan jendela
cap.release()
cv2.destroyAllWindows()
