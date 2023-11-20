import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QGraphicsView, QMenuBar, QMenu, QStatusBar, QSizePolicy, QFileDialog, QGraphicsPixmapItem, QGraphicsScene
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QPixmap, QImage
from PyQt6 import QtCore
import cv2
import numpy as np
from copy import deepcopy

class ImageView(QGraphicsView):
    def __init__(self, parent: QWidget, Clickable=False):
        super().__init__(parent)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setScene(QGraphicsScene())
        self.image = None
        self.isClickable = Clickable
        self.clicked = False
        
    def mousePressEvent(self, event):
        if self.isClickable and not self.clicked:
            self.parentWidget().parent().open_image()
            # self.open_image()
            if self.image is not None:
                self.clicked = True

    def open_image(self):
        self.parentWidget().parent().clear_image()
        fname = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "${HOME}",
            "Image Files (*.jpg *.jpeg *.png *.bmp *.ppm)",
        )
        if fname[0]:
            print(fname[0])
            self.image = cv2.imdecode(np.fromfile(fname[0],dtype=np.uint8), cv2.IMREAD_UNCHANGED)
            # cv2.imshow("test", self.image)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            self.update()

        # print("open image end.")
        return

    def save_image(self):
        if not self.scene().items():
            return
        fname = QFileDialog.getSaveFileName(
            self,
            "Save File",
            "${HOME}/image",
            "Image Files (*.jpg *.jpeg *.png *.bmp *.ppm)",
        )
        if fname[0] and fname[0].split('.'):
            output_type = "."+fname[0].split('.')[-1]
            output_image = self.image
            if output_type == ".ppm":
                if len(self.image.shape) == 2:
                    output_image = cv2.cvtColor(self.image, cv2.COLOR_GRAY2BGR)
                elif self.image.shape[2] == 4:
                    output_image = cv2.cvtColor(self.image, cv2.COLOR_BGRA2BGR)

            cv2.imencode(ext=output_type, img=output_image)[1].tofile(fname[0])
    
    def setImage(self, image):
        if image is not None:
            self.image = deepcopy(image)

    def update(self):
        if self.image is not None:
            # Convert the OpenCV image to a QImage
            if len(self.image.shape) == 2:
                height, width = self.image.shape
                channel = 1
            else:
                height, width, channel = self.image.shape
            # print("channel:", channel)
            bytes_per_line = channel * width
            if channel == 3:
                q_image = QImage(self.image.data, width, height, bytes_per_line, QImage.Format.Format_BGR888)
            elif channel == 4:
                q_image = QImage(self.image.data, width, height, bytes_per_line, QImage.Format.Format_RGBA8888).rgbSwapped()
            elif channel == 1:
                q_image = QImage(self.image.data, width, height, bytes_per_line, QImage.Format.Format_Grayscale8)



            # Convert QImage to QPixmap and display it in QGraphicsView
            pixmap = QPixmap.fromImage(q_image)
            pixmap = pixmap.scaled(self.geometry().size())
            pixmap_item = QGraphicsPixmapItem(pixmap)
            # scene = QGraphicsScene()
            # scene.addItem(pixmap_item)
            # self.setScene(scene)
            if self.scene().items():
                self.scene().removeItem(self.scene().items()[0])
            self.scene().addItem(pixmap_item)
        else:
            print("image is none")
            pass
    
        # print("update image end.")
        return 
    
    def clear(self):
        self.image = None
        if self.scene().items():
            self.scene().removeItem(self.scene().items()[0])
        self.clicked = False

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle("AIP61247001S")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.src_view = ImageView(central_widget, Clickable=True)
        self.src_view.setGeometry(40, 160, 256, 256)

        self.dst_view = ImageView(central_widget)
        self.dst_view.setGeometry(480, 160, 256, 256)

        self.action_layout_widget = QWidget(self)
        self.action_layout_widget.setGeometry(0, 60, 801, 80)
        action_layout = QHBoxLayout(self.action_layout_widget)
        action_layout.setSpacing(20)

        self.clear_button = QPushButton("Clear", self)
        self.clear_button.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum))
        action_layout.addWidget(self.clear_button)

        self.rotate_button = QPushButton("Rotate", self)
        self.rotate_button.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum))
        action_layout.addWidget(self.rotate_button)

        menubar = QMenuBar(self)
        menubar.setGeometry(0, 0, 800, 20)
        self.setMenuBar(menubar)

        menu_file = QMenu("File", self)
        menubar.addMenu(menu_file)

        action_open_image = QAction("Open Image", self)
        action_open_image.setShortcut("Ctrl+O")
        menu_file.addAction(action_open_image)

        menu_file.addSeparator()

        action_save_image = QAction("Save", self)
        action_save_image.setShortcut("Ctrl+S")
        menu_file.addAction(action_save_image)

        statusbar = QStatusBar(self)
        self.setStatusBar(statusbar)

        action_open_image.triggered.connect(self.open_image)
        action_save_image.triggered.connect(self.save_image)
        self.rotate_button.clicked.connect(self.rotate_image)
        self.clear_button.clicked.connect(self.clear_image)
        

    @QtCore.pyqtSlot()
    def open_image(self):
        self.src_view.open_image()
        self.dst_view.setImage(self.src_view.image)
    @QtCore.pyqtSlot()
    def save_image(self):
        self.dst_view.save_image()
    @QtCore.pyqtSlot()
    def rotate_image(self):
        self.dst_view.image = rotate_image(self.dst_view.image)
        self.dst_view.update()
    @QtCore.pyqtSlot()
    def clear_image(self):
        self.src_view.clear()
        self.dst_view.clear()

def rotate_image(image):
    if image is not None:
        # Specify the rotation angle in degrees
        angle = 180  # Example: Rotate 90 degrees
        # print(image.shape)
        # print(image.cols)
        # print(image.rows)
        # Get the image dimensions
        height, width = image.shape[:2]
        

        # Define the rotation matrix
        rotation_matrix = cv2.getRotationMatrix2D((width / 2 - 1, height / 2 - 1), angle, 1)

        # Apply the rotation to the image
        rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
        
        return rotated_image
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
