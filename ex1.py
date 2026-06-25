import cv2

# โหลด cascade classifier สำหรับการตรวจจับใบหน้า
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# โหลดรูปภาพ
image = cv2.imread('a3.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ตรวจจับใบหน้า
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# วาดกรอบรอบใบหน้าทุกใบหน้าในภาพ
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# แสดงภาพผลลัพธ์
cv2.imshow('Face Detection', image)

# รอการกดปุ่มเพื่อปิดหน้าต่าง
cv2.waitKey(0)
cv2.destroyAllWindows()
