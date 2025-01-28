import cv2
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout,
    QComboBox, QWidget, QMessageBox
)
from PyQt5.QtCore import Qt

class CameraTestApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Camera Test Application")
        self.setGeometry(200, 200, 400, 300)

        # Central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Camera selection combo box
        self.camera_label = QLabel("Select a camera:")
        self.camera_combo = QComboBox()
        self.layout.addWidget(self.camera_label)
        self.layout.addWidget(self.camera_combo)

        # Test camera button
        self.test_button = QPushButton("Test Camera")
        self.test_button.clicked.connect(self.test_camera)
        self.layout.addWidget(self.test_button)

        # Close button
        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.close)
        self.layout.addWidget(self.close_button)

        # Populate camera list
        self.populate_camera_list()

    def populate_camera_list(self):
        self.camera_combo.clear()
        index = 0
        while True:
            cap = cv2.VideoCapture(index)
            if cap.isOpened():
                self.camera_combo.addItem(f"Camera {index}")
                cap.release()
            else:
                break
            index += 1

        if self.camera_combo.count() == 0:
            QMessageBox.critical(self, "Error", "No cameras found.")

    def test_camera(self):
        selected_index = self.camera_combo.currentIndex()
        if selected_index == -1:
            QMessageBox.warning(self, "Warning", "No camera selected.")
            return

        camera = cv2.VideoCapture(selected_index)
        if not camera.isOpened():
            QMessageBox.critical(self, "Error", "Cannot access the selected camera.")
            return

        while True:
            ret, frame = camera.read()
            if not ret:
                QMessageBox.critical(self, "Error", "Failed to capture frame.")
                break

            cv2.imshow("Camera Test - Press ESC to Close", frame)

            key = cv2.waitKey(1)
            if key == 27:  # ESC key to exit
                break

        camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    app = QApplication([])
    window = CameraTestApp()
    window.show()
    app.exec_()
