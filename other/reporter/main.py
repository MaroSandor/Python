import os
from fpdf import FPDF
from datetime import datetime
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QTextEdit,
    QVBoxLayout, QComboBox, QWidget, QMessageBox, QListWidget, QListWidgetItem, QDialog, QGridLayout
)
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5.QtCore import Qt, QTimer
import cv2


class PhotoCaptureDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fotó készítése")
        self.setGeometry(100, 100, 600, 500)
        self.photo = None

        # Layout
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # Camera selection
        self.camera_label = QLabel("Kamera kiválasztása:")
        self.camera_combo = QComboBox()
        self.camera_combo.currentIndexChanged.connect(self.on_camera_change)
        self.layout.addWidget(self.camera_label, 0, 0, 1, 2)
        self.layout.addWidget(self.camera_combo, 0, 1, 1, 2)

        # Camera preview
        self.preview_label = QLabel("Kamera előnézet:")
        self.camera_preview = QLabel()
        self.camera_preview.setFixedSize(400, 300)
        self.camera_preview.setStyleSheet("border: 1px solid black;")
        self.layout.addWidget(self.preview_label, 1, 0, 1, 4)
        self.layout.addWidget(self.camera_preview, 2, 0, 1, 4)

        # Captured photo preview
        self.captured_label = QLabel("Készített fotó:")
        self.captured_preview = QLabel()
        self.captured_preview.setFixedSize(400, 300)
        self.captured_preview.setStyleSheet("border: 1px solid black;")
        self.layout.addWidget(self.captured_label, 3, 0, 1, 4)
        self.layout.addWidget(self.captured_preview, 4, 0, 1, 4)

        # Buttons
        self.take_photo_button = QPushButton("Fotó készítése")
        self.ok_button = QPushButton("OK")
        self.discard_button = QPushButton("Elvetés")
        self.cancel_button = QPushButton("Mégse")

        self.layout.addWidget(self.take_photo_button, 5, 0)
        self.layout.addWidget(self.ok_button, 5, 1)
        self.layout.addWidget(self.discard_button, 5, 2)
        self.layout.addWidget(self.cancel_button, 5, 3)

        # Connections
        self.take_photo_button.clicked.connect(self.take_photo)
        self.ok_button.clicked.connect(self.accept_photo)
        self.discard_button.clicked.connect(self.discard_photo)
        self.cancel_button.clicked.connect(self.close)

        # Camera setup
        self.capture = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_preview)
        self.populate_camera_list()
        self.start_camera_preview()

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

    def on_camera_change(self):
        self.start_camera_preview()

    def start_camera_preview(self):
        selected_camera_index = self.camera_combo.currentIndex()
        if selected_camera_index == -1:
            QMessageBox.warning(self, "Figyelmeztetés", "Nincs kiválasztott kamera.")
            return

        if self.capture:
            self.capture.release()

        self.capture = cv2.VideoCapture(selected_camera_index)
        if not self.capture.isOpened():
            QMessageBox.critical(self, "Hiba", "Nem lehet elérni a kiválasztott kamerát.")
            return

        self.timer.start(30)  # Refresh every 30ms

    def update_preview(self):
        if self.capture and self.capture.isOpened():
            ret, frame = self.capture.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
                qimg = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(qimg)
                self.camera_preview.setPixmap(pixmap.scaled(400, 300, Qt.KeepAspectRatio))

    def take_photo(self):
        if self.capture and self.capture.isOpened():
            ret, frame = self.capture.read()
            if ret:
                self.photo = frame
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
                qimg = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(qimg)
                self.captured_preview.setPixmap(pixmap.scaled(400, 300, Qt.KeepAspectRatio))
            else:
                QMessageBox.critical(self, "Hiba", "Nem sikerült a fotó készítése.")

    def accept_photo(self):
        if self.photo is None:
            QMessageBox.warning(self, "Figyelmeztetés", "Nincs készített fotó.")
            return
        self.done(1)

    def discard_photo(self):
        self.photo = None
        self.captured_preview.clear()
        QMessageBox.information(self, "Fotó elvetve", "A fotó el lett vetve.")

    def closeEvent(self, event):
        if self.capture:
            self.capture.release()
        self.timer.stop()
        cv2.destroyAllWindows()
        super().closeEvent(event)


class ReportApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Reporter")
        self.setGeometry(200, 200, 800, 600)

        # Central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layouts
        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        # Issue selection
        self.issue_label = QLabel("Probléma kiválasztása:")
        self.issue_combo = QComboBox()
        self.issue_combo.addItems(["Hálózati hiba", "Hardver hiba", "Szoftver hiba", "Egyéb"])
        self.main_layout.addWidget(self.issue_label)
        self.main_layout.addWidget(self.issue_combo)

        # Additional comment
        self.comment_label = QLabel("Megjegyzés hozzáadása:")
        self.comment_text = QTextEdit()
        self.main_layout.addWidget(self.comment_label)
        self.main_layout.addWidget(self.comment_text)

        # Photo management
        self.photo_label = QLabel("Fotók kezelése:")
        self.photo_list = QListWidget()
        self.attach_button = QPushButton("Fotó csatolása")
        self.attach_button.clicked.connect(self.attach_photo)
        self.main_layout.addWidget(self.photo_label)
        self.main_layout.addWidget(self.photo_list)
        self.main_layout.addWidget(self.attach_button)

        # Export button
        self.export_button = QPushButton("Exportálás PDF-be")
        self.export_button.clicked.connect(self.export_to_pdf)
        self.main_layout.addWidget(self.export_button)

        # Placeholder for photos
        self.photos = []

    def attach_photo(self):
        dialog = PhotoCaptureDialog()
        if dialog.exec_():
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            photo_name = f"photo_{timestamp}.jpg"
            cv2.imwrite(photo_name, dialog.photo)
            self.photos.append(photo_name)

            # Add an icon to the photo list
            item = QListWidgetItem()
            icon = QIcon(photo_name)
            item.setIcon(icon)
            item.setText(photo_name)
            item.setToolTip("Kattints a fotó megtekintéséhez")
            item.setData(Qt.UserRole, photo_name)

            self.photo_list.addItem(item)
            self.photo_list.itemClicked.connect(self.view_photo)

    def view_photo(self, item):
        photo_path = item.data(Qt.UserRole)
        pixmap = QPixmap(photo_path)

        photo_dialog = QDialog(self)
        photo_dialog.setWindowTitle("Fotó megtekintése")
        layout = QVBoxLayout()

        label = QLabel()
        label.setPixmap(pixmap.scaled(800, 600, Qt.KeepAspectRatio))
        layout.addWidget(label)

        close_button = QPushButton("Bezárás")
        close_button.clicked.connect(photo_dialog.close)
        layout.addWidget(close_button)

        photo_dialog.setLayout(layout)
        photo_dialog.exec_()

    def export_to_pdf(self):
        issue = self.issue_combo.currentText()
        comment = self.comment_text.toPlainText()

        if not issue or not comment:
            QMessageBox.warning(self, "Figyelmeztetés", "Töltsd ki az összes mezőt.")
            return

        pdf = FPDF()
        pdf.add_page()

        # Betűtípus hozzáadása Unicode támogatással
        font_path = os.path.join(os.path.dirname(__file__), "assets/fonts/DejaVuSans.ttf")
        pdf.add_font("DejaVu", fname=font_path, uni=True)
        pdf.set_font("DejaVu", size=12)

        # Stílusos fejléc
        pdf.set_fill_color(200, 220, 255)  # Világoskék háttér
        pdf.cell(0, 10, txt="Hibajegy", ln=True, align='C', fill=True)
        pdf.ln(10)

        # Probléma és megjegyzés hozzáadása
        pdf.set_font("DejaVu", size=10)
        pdf.multi_cell(0, 10, txt=f"Probléma: {issue}\nMegjegyzés:\n{comment}", align='L')

        # Fotók elhelyezése egy oldalon
        if self.photos:
            pdf.ln(10)
            pdf.set_fill_color(220, 220, 220)  # Szürke háttér a "Fotók" részhez
            pdf.cell(0, 10, txt="Csatolt fotók:", ln=True, align='L', fill=True)
            x, y = 10, pdf.get_y() + 5

            for photo in self.photos:
                if y + 60 > 270:  # Ha nincs elég hely, új oldalt kezdünk
                    pdf.add_page()
                    y = 10

                pdf.image(photo, x=x, y=y, w=60)
                x += 65  # Következő kép jobbra
                if x + 60 > 200:  # Ha a sor véget ér, új sorba lépünk
                    x = 10
                    y += 65

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"Hibajegy_{timestamp}.pdf"
        try:
            pdf.output(file_name)
            QMessageBox.information(self, "Siker", f"A hibajegy exportálva lett: {file_name}")
        except Exception as e:
            QMessageBox.critical(self, "Hiba", f"Nem sikerült a PDF exportálása: {str(e)}")

if __name__ == "__main__":
    app = QApplication([])
    window = ReportApp()
    window.show()
    app.exec_()
