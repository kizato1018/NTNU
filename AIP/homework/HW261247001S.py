import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QGraphicsView, QMenuBar, QMenu, QStatusBar, QSizePolicy, QFileDialog, QGraphicsPixmapItem, QGraphicsScene
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QPixmap, QImage
from PyQt6 import QtCore
import cv2
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.backends.backend_agg import FigureCanvasAgg


class Ui_AIP61247001S(object):
    def setupUi(self, AIP61247001S):
        AIP61247001S.setObjectName("AIP61247001S")
        AIP61247001S.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=AIP61247001S)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalWidget.setGeometry(QtCore.QRect(0, 0, 801, 80))
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(40, 0, 0, 0)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rotate_switch_button = QtWidgets.QPushButton(parent=self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotate_switch_button.sizePolicy().hasHeightForWidth())
        self.rotate_switch_button.setSizePolicy(sizePolicy)
        self.rotate_switch_button.setMinimumSize(QtCore.QSize(100, 50))
        self.rotate_switch_button.setSizeIncrement(QtCore.QSize(0, 0))
        self.rotate_switch_button.setBaseSize(QtCore.QSize(0, 0))
        self.rotate_switch_button.setIconSize(QtCore.QSize(16, 16))
        self.rotate_switch_button.setObjectName("rotate_swtich_button")
        self.horizontalLayout.addWidget(self.rotate_switch_button)
        self.histogram_switch_button = QtWidgets.QPushButton(parent=self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.histogram_switch_button.sizePolicy().hasHeightForWidth())
        self.histogram_switch_button.setSizePolicy(sizePolicy)
        self.histogram_switch_button.setMinimumSize(QtCore.QSize(100, 50))
        self.histogram_switch_button.setSizeIncrement(QtCore.QSize(0, 0))
        self.histogram_switch_button.setBaseSize(QtCore.QSize(0, 0))
        self.histogram_switch_button.setIconSize(QtCore.QSize(16, 16))
        self.histogram_switch_button.setObjectName("histogram_switch_button")
        self.horizontalLayout.addWidget(self.histogram_switch_button)
        self.noise_generation_switch_button = QtWidgets.QPushButton(parent=self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noise_generation_switch_button.sizePolicy().hasHeightForWidth())
        self.noise_generation_switch_button.setSizePolicy(sizePolicy)
        self.noise_generation_switch_button.setMinimumSize(QtCore.QSize(100, 50))
        self.noise_generation_switch_button.setSizeIncrement(QtCore.QSize(0, 0))
        self.noise_generation_switch_button.setBaseSize(QtCore.QSize(0, 0))
        self.noise_generation_switch_button.setIconSize(QtCore.QSize(16, 16))
        self.noise_generation_switch_button.setObjectName("noise_generation_swich_button")
        self.horizontalLayout.addWidget(self.noise_generation_switch_button)
        self.widget = QtWidgets.QWidget(parent=self.horizontalWidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 80, 800, 500))
        self.stackedWidget.setObjectName("stackedWidget")
        self.image_rotate_page = QtWidgets.QWidget()
        self.image_rotate_page.setObjectName("image_rotate_page")
        self.image_rotate_widget = QtWidgets.QWidget(parent=self.image_rotate_page)
        self.image_rotate_widget.setEnabled(True)
        self.image_rotate_widget.setGeometry(QtCore.QRect(0, 0, 800, 499))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_rotate_widget.sizePolicy().hasHeightForWidth())
        self.image_rotate_widget.setSizePolicy(sizePolicy)
        self.image_rotate_widget.setAcceptDrops(False)
        self.image_rotate_widget.setAutoFillBackground(False)
        self.image_rotate_widget.setObjectName("image_rotate_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.image_rotate_widget)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.rotate_src_view = ImageView(parent=self.image_rotate_widget)
        self.rotate_src_view.setProperty("isClickable", True)
        self.rotate_src_view.setObjectName("rotate_src_view")
        self.gridLayout.addWidget(self.rotate_src_view, 3, 0, 1, 1)
        self.rotate_dst_view = ImageView(parent=self.image_rotate_widget)
        self.rotate_dst_view.setProperty("isClickable", False)
        self.rotate_dst_view.setObjectName("rotate_dst_view")
        self.gridLayout.addWidget(self.rotate_dst_view, 3, 2, 1, 1)
        self.verticalWidget = QtWidgets.QWidget(parent=self.image_rotate_widget)
        self.verticalWidget.setMinimumSize(QtCore.QSize(30, 0))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(-1, 120, -1, 120)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rotate_button = QtWidgets.QPushButton(parent=self.verticalWidget)
        self.rotate_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotate_button.sizePolicy().hasHeightForWidth())
        self.rotate_button.setSizePolicy(sizePolicy)
        self.rotate_button.setMinimumSize(QtCore.QSize(120, 60))
        self.rotate_button.setObjectName("rotate_button")
        self.verticalLayout.addWidget(self.rotate_button)
        self.gridLayout.addWidget(self.verticalWidget, 3, 1, 1, 1)
        self.horizontalWidget1 = QtWidgets.QWidget(parent=self.image_rotate_widget)
        self.horizontalWidget1.setMinimumSize(QtCore.QSize(0, 20))
        self.horizontalWidget1.setObjectName("horizontalWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rotate_open_button = QtWidgets.QPushButton(parent=self.horizontalWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotate_open_button.sizePolicy().hasHeightForWidth())
        self.rotate_open_button.setSizePolicy(sizePolicy)
        self.rotate_open_button.setMinimumSize(QtCore.QSize(80, 40))
        self.rotate_open_button.setObjectName("rotate_open_button")
        self.horizontalLayout_2.addWidget(self.rotate_open_button)
        self.rotate_clear_button = QtWidgets.QPushButton(parent=self.horizontalWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotate_clear_button.sizePolicy().hasHeightForWidth())
        self.rotate_clear_button.setSizePolicy(sizePolicy)
        self.rotate_clear_button.setMinimumSize(QtCore.QSize(80, 40))
        self.rotate_clear_button.setObjectName("rotate_clear_button")
        self.horizontalLayout_2.addWidget(self.rotate_clear_button)
        self.gridLayout.addWidget(self.horizontalWidget1, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rotate_save_button = QtWidgets.QPushButton(parent=self.image_rotate_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotate_save_button.sizePolicy().hasHeightForWidth())
        self.rotate_save_button.setSizePolicy(sizePolicy)
        self.rotate_save_button.setMinimumSize(QtCore.QSize(80, 40))
        self.rotate_save_button.setObjectName("rotate_save_button")
        self.horizontalLayout_3.addWidget(self.rotate_save_button)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 2, 1, 1)
        self.stackedWidget.addWidget(self.image_rotate_page)
        self.histogram_page = QtWidgets.QWidget()
        self.histogram_page.setObjectName("histogram_page")
        self.histogram_widget = QtWidgets.QWidget(parent=self.histogram_page)
        self.histogram_widget.setEnabled(True)
        self.histogram_widget.setGeometry(QtCore.QRect(0, 0, 800, 499))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.histogram_widget.sizePolicy().hasHeightForWidth())
        self.histogram_widget.setSizePolicy(sizePolicy)
        self.histogram_widget.setAcceptDrops(False)
        self.histogram_widget.setAutoFillBackground(False)
        self.histogram_widget.setObjectName("histogram_widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.histogram_widget)
        self.gridLayout_3.setContentsMargins(20, 20, 20, 20)
        self.gridLayout_3.setHorizontalSpacing(20)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.histogram_save_button = QtWidgets.QPushButton(parent=self.histogram_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.histogram_save_button.sizePolicy().hasHeightForWidth())
        self.histogram_save_button.setSizePolicy(sizePolicy)
        self.histogram_save_button.setMinimumSize(QtCore.QSize(80, 40))
        self.histogram_save_button.setObjectName("histogram_save_button")
        self.horizontalLayout_7.addWidget(self.histogram_save_button)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 0, 1, 1, 1)
        self.histogram_src_view = ImageView(parent=self.histogram_widget)
        self.histogram_src_view.setProperty("isClickable", True)
        self.histogram_src_view.setObjectName("histogram_src_view")
        self.gridLayout_3.addWidget(self.histogram_src_view, 3, 0, 1, 1)
        self.histogram_dst_view = ImageView(parent=self.histogram_widget)
        self.histogram_dst_view.setProperty("isClickable", False)
        self.histogram_dst_view.setObjectName("histogram_dst_view")
        self.gridLayout_3.addWidget(self.histogram_dst_view, 3, 1, 1, 1)
        self.horizontalWidget_3 = QtWidgets.QWidget(parent=self.histogram_widget)
        self.horizontalWidget_3.setMinimumSize(QtCore.QSize(0, 20))
        self.horizontalWidget_3.setObjectName("horizontalWidget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.histogram_open_button = QtWidgets.QPushButton(parent=self.horizontalWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.histogram_open_button.sizePolicy().hasHeightForWidth())
        self.histogram_open_button.setSizePolicy(sizePolicy)
        self.histogram_open_button.setMinimumSize(QtCore.QSize(80, 40))
        self.histogram_open_button.setObjectName("histogram_open_button")
        self.horizontalLayout_6.addWidget(self.histogram_open_button)
        self.histogram_clear_button = QtWidgets.QPushButton(parent=self.horizontalWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.histogram_clear_button.sizePolicy().hasHeightForWidth())
        self.histogram_clear_button.setSizePolicy(sizePolicy)
        self.histogram_clear_button.setMinimumSize(QtCore.QSize(80, 40))
        self.histogram_clear_button.setObjectName("histogram_clear_button")
        self.horizontalLayout_6.addWidget(self.histogram_clear_button)
        self.gridLayout_3.addWidget(self.horizontalWidget_3, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.histogram_page)
        AIP61247001S.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=AIP61247001S)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        AIP61247001S.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=AIP61247001S)
        self.statusbar.setObjectName("statusbar")
        AIP61247001S.setStatusBar(self.statusbar)
        self.action_open_image = QtGui.QAction(parent=AIP61247001S)
        self.action_open_image.setObjectName("action_open_image")
        self.action_save_image = QtGui.QAction(parent=AIP61247001S)
        self.action_save_image.setObjectName("action_save_image")
        self.action_clear_image = QtGui.QAction(parent=AIP61247001S)
        self.action_clear_image.setObjectName("action_clear_image")
        self.menuFile.addAction(self.action_open_image)
        self.menuFile.addAction(self.action_clear_image)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_save_image)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(AIP61247001S)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(AIP61247001S)

    def retranslateUi(self, AIP61247001S):
        _translate = QtCore.QCoreApplication.translate
        AIP61247001S.setWindowTitle(_translate("AIP61247001S", "AIP61247001S"))
        self.rotate_switch_button.setText(_translate("AIP61247001S", "Image Rotate"))
        self.histogram_switch_button.setText(_translate("AIP61247001S", "Histogram"))
        self.noise_generation_switch_button.setText(_translate("AIP61247001S", "Noise Generation"))
        self.rotate_button.setText(_translate("AIP61247001S", "Rotate"))
        self.rotate_open_button.setText(_translate("AIP61247001S", "Open"))
        self.rotate_clear_button.setText(_translate("AIP61247001S", "Clear"))
        self.rotate_save_button.setText(_translate("AIP61247001S", "Save"))
        self.histogram_save_button.setText(_translate("AIP61247001S", "Save"))
        self.histogram_open_button.setText(_translate("AIP61247001S", "Open"))
        self.histogram_clear_button.setText(_translate("AIP61247001S", "Clear"))
        self.menuFile.setTitle(_translate("AIP61247001S", "File"))
        self.action_open_image.setText(_translate("AIP61247001S", "Open Image"))
        self.action_open_image.setShortcut(_translate("AIP61247001S", "Ctrl+O"))
        self.action_save_image.setText(_translate("AIP61247001S", "Save Image"))
        self.action_save_image.setShortcut(_translate("AIP61247001S", "Ctrl+S"))
        self.action_clear_image.setText(_translate("AIP61247001S", "Clear Image"))
        self.action_clear_image.setShortcut(_translate("AIP61247001S", "Ctrl+L"))

class ImageView(QGraphicsView):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setScene(QGraphicsScene())
        self.image = None
        self.q_image = None
        self.clicked = False
        
    def mousePressEvent(self, event):
        if self.property('isClickable') and not self.clicked:
            print("click")
            # self.parentWidget().parent().open_image()
            open_image()
            if self.image is not None:
                self.clicked = True

    def open_image(self):
        clear_image()
        fname = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "${HOME}",
            "Image Files (*.jpg *.jpeg *.png *.bmp *.ppm)",
        )
        if fname[0]:
            image = cv2.imdecode(np.fromfile(fname[0],dtype=np.uint8), cv2.IMREAD_UNCHANGED)
            self.setImage(image)
            self.update()
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
            if len(self.image.shape) == 2:
                height, width = self.image.shape
                channel = 1
            else:
                height, width, channel = self.image.shape
            bytes_per_line = channel * width
            if channel == 3:
                self.q_image = QImage(self.image.data, width, height, bytes_per_line, QImage.Format.Format_BGR888)
            elif channel == 4:
                self.q_image = QImage(self.image.data, width, height, bytes_per_line, QImage.Format.Format_RGBA8888).rgbSwapped()
            elif channel == 1:
                self.q_image = QImage(self.image.data, width, height, bytes_per_line, QImage.Format.Format_Grayscale8)
            self.clicked = True

    def update(self):
        if self.q_image is not None:
            pixmap = QPixmap.fromImage(self.q_image)
            pixmap = pixmap.scaled(self.geometry().size())
            pixmap_item = QGraphicsPixmapItem(pixmap)
            if self.scene().items():
                self.scene().removeItem(self.scene().items()[0])
            self.scene().addItem(pixmap_item)
        else:
            print("image is none")
            pass
        return 
    
    def clear(self):
        self.image = None
        self.q_image = None
        if self.scene().items():
            self.scene().removeItem(self.scene().items()[0])
        self.clicked = False

def setupScript(ui:Ui_AIP61247001S):
    ui.noise_generation_switch_button.hide()
    ui.action_open_image.triggered.connect(open_image)
    ui.action_clear_image.triggered.connect(clear_image)
    ui.action_save_image.triggered.connect(save_image)
    ui.rotate_switch_button.clicked.connect(lambda: switch_page(0))
    ui.histogram_switch_button.clicked.connect(lambda: switch_page(1))
    ui.noise_generation_switch_button.clicked.connect(lambda: switch_page(2))
    ui.rotate_open_button.clicked.connect(open_image)
    ui.rotate_clear_button.clicked.connect(clear_image)
    ui.rotate_save_button.clicked.connect(save_image)
    ui.rotate_button.clicked.connect(rotate)
    ui.histogram_open_button.clicked.connect(open_image)
    ui.histogram_clear_button.clicked.connect(clear_image)
    ui.histogram_save_button.clicked.connect(save_image)



@QtCore.pyqtSlot()
def open_image():
    page = ui.stackedWidget.currentIndex()
    if page == 0:
        ui.rotate_src_view.open_image()
        
    elif page == 1:
        ui.histogram_src_view.open_image()
        ui.histogram_dst_view.setImage(histogram_image(ui.histogram_src_view.image))
        ui.histogram_dst_view.update()
@QtCore.pyqtSlot()
def save_image():
    page = ui.stackedWidget.currentIndex()
    if page == 0:
        ui.rotate_dst_view.save_image()
    elif page == 1:
        ui.histogram_dst_view.save_image()
@QtCore.pyqtSlot()
def clear_image():
    page = ui.stackedWidget.currentIndex()
    if page == 0:
        ui.rotate_src_view.clear()
        ui.rotate_dst_view.clear()
    elif page == 1:
        ui.histogram_src_view.clear()
        ui.histogram_dst_view.clear()
@QtCore.pyqtSlot()
def switch_page(page):
    ui.stackedWidget.setCurrentIndex(page)
    print(ui.stackedWidget.currentIndex())
@QtCore.pyqtSlot()
def rotate():
    if ui.rotate_dst_view.image is None:
        ui.rotate_dst_view.setImage(ui.rotate_src_view.image)
    ui.rotate_dst_view.setImage(rotate_image(ui.rotate_dst_view.image))
    ui.rotate_dst_view.update()

def rotate_image(image):
    if image is not None:
        angle = 180
        height, width = image.shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((width / 2 - 1, height / 2 - 1), angle, 1)
        rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
        
        return rotated_image

def histogram_image(image):
    if image is None:
        return
    if len(image.shape) == 2:
        img = deepcopy(image)
    elif image.shape[2] == 3:
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif image.shape[2] == 4:
        img = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)

    gradient = np.linspace(0, 256, 256).reshape(1, -1)

    fig = plt.figure(figsize=(5, 5))
    gs = GridSpec(2, 1, height_ratios=[10, 1], hspace=0)

    ax0 = plt.subplot(gs[0])
    hist, bins = np.histogram(img.ravel(), 256, [0, 256])
    ax0.bar(range(256), hist, color="gray", width=1)
    ax0.set_xlim(-1, 256)
    ax0.set_xticks([])

    ax1 = plt.subplot(gs[1])
    plt.imshow(gradient, cmap="gray", aspect='auto')
    cbar = plt.colorbar(orientation='horizontal', cax=ax1)
    # ax1.set_xlim(0, 256)

    plt.xticks(ax1.get_xticks())
    plt.xlim(0, 256)

    plt.tight_layout()

    canvas = FigureCanvasAgg(fig)
    canvas.draw()  # Draw the canvas, cache the renderer

    image_flat = np.frombuffer(canvas.tostring_argb(), dtype='uint8')
    hist_image = image_flat.reshape(*reversed(canvas.get_width_height()), 4)
    hist_image = hist_image[:, :, ::-1]
    hist_image = hist_image[:, :, :3]
    
    return hist_image


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AIP61247001S = QtWidgets.QMainWindow()
    ui = Ui_AIP61247001S()
    ui.setupUi(AIP61247001S)
    setupScript(ui)
    AIP61247001S.show()
    sys.exit(app.exec())
