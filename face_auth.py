import cv2


def authenticate_user():
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    cap = cv2.VideoCapture(0)

    print("Camera starting... Look at the camera 👀")

    authenticated = False
    frame_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Camera error")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # Draw rectangle (visual feedback)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            authenticated = True

        cv2.imshow("Face Authentication", frame)

        frame_count += 1

        # Wait for key or auto-detect face
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # If face detected for few frames → authenticate
        if authenticated and frame_count > 20:
            print("Face detected ✔ Access Granted")
            break

    cap.release()
    cv2.destroyAllWindows()

    return authenticated