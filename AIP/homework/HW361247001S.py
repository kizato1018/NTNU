import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QGraphicsView, QMenuBar, QMenu, QStatusBar, QSizePolicy, QFileDialog, QGraphicsPixmapItem, QGraphicsScene
from PyQt6.QtCore import Qt, QObject, QEvent
from PyQt6.QtGui import QAction, QPixmap, QImage
from PyQt6 import QtCore
import cv2
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.backends.backend_agg import FigureCanvasAgg
from numba import jit

class Ui_AIP61247001S(object):
    def setupUi(self, AIP61247001S):
        AIP61247001S.setObjectName("AIP61247001S")
        AIP61247001S.resize(839, 754)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AIP61247001S.sizePolicy().hasHeightForWidth())
        AIP61247001S.setSizePolicy(sizePolicy)
        AIP61247001S.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(parent=AIP61247001S)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(750, 520))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setContentsMargins(40, -1, -1, -1)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
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
        self.rotate_switch_button.setObjectName("rotate_switch_button")
        self.horizontalLayout_2.addWidget(self.rotate_switch_button)
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
        self.horizontalLayout_2.addWidget(self.histogram_switch_button)
        self.noise_generation_switch_button = QtWidgets.QPushButton(parent=self.horizontalWidget)
        self.noise_generation_switch_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noise_generation_switch_button.sizePolicy().hasHeightForWidth())
        self.noise_generation_switch_button.setSizePolicy(sizePolicy)
        self.noise_generation_switch_button.setMinimumSize(QtCore.QSize(100, 50))
        self.noise_generation_switch_button.setSizeIncrement(QtCore.QSize(0, 0))
        self.noise_generation_switch_button.setBaseSize(QtCore.QSize(0, 0))
        self.noise_generation_switch_button.setIconSize(QtCore.QSize(16, 16))
        self.noise_generation_switch_button.setCheckable(False)
        self.noise_generation_switch_button.setChecked(False)
        self.noise_generation_switch_button.setDefault(False)
        self.noise_generation_switch_button.setFlat(False)
        self.noise_generation_switch_button.setObjectName("noise_generation_switch_button")
        self.horizontalLayout_2.addWidget(self.noise_generation_switch_button)
        self.widget = QtWidgets.QWidget(parent=self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2.addWidget(self.widget)
        self.gridLayout.addWidget(self.horizontalWidget, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.image_rotate_page = QtWidgets.QWidget()
        self.image_rotate_page.setObjectName("image_rotate_page")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.image_rotate_page)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.image_rotate_widget = QtWidgets.QWidget(parent=self.image_rotate_page)
        self.image_rotate_widget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_rotate_widget.sizePolicy().hasHeightForWidth())
        self.image_rotate_widget.setSizePolicy(sizePolicy)
        self.image_rotate_widget.setAcceptDrops(False)
        self.image_rotate_widget.setAutoFillBackground(False)
        self.image_rotate_widget.setObjectName("image_rotate_widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.image_rotate_widget)
        self.gridLayout_4.setContentsMargins(20, 20, 20, 20)
        self.gridLayout_4.setHorizontalSpacing(20)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.rotate_dst_view = ImageView(parent=self.image_rotate_widget)
        self.rotate_dst_view.setProperty("isClickable", False)
        self.rotate_dst_view.setObjectName("rotate_dst_view")
        self.gridLayout_4.addWidget(self.rotate_dst_view, 3, 2, 1, 1)
        self.horizontalWidget_3 = QtWidgets.QWidget(parent=self.image_rotate_widget)
        self.horizontalWidget_3.setMinimumSize(QtCore.QSize(0, 20))
        self.horizontalWidget_3.setObjectName("horizontalWidget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.rotate_open_button = QtWidgets.QPushButton(parent=self.horizontalWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotate_open_button.sizePolicy().hasHeightForWidth())
        self.rotate_open_button.setSizePolicy(sizePolicy)
        self.rotate_open_button.setMinimumSize(QtCore.QSize(80, 40))
        self.rotate_open_button.setObjectName("rotate_open_button")
        self.horizontalLayout_5.addWidget(self.rotate_open_button)
        self.rotate_clear_button = QtWidgets.QPushButton(parent=self.horizontalWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotate_clear_button.sizePolicy().hasHeightForWidth())
        self.rotate_clear_button.setSizePolicy(sizePolicy)
        self.rotate_clear_button.setMinimumSize(QtCore.QSize(80, 40))
        self.rotate_clear_button.setObjectName("rotate_clear_button")
        self.horizontalLayout_5.addWidget(self.rotate_clear_button)
        self.gridLayout_4.addWidget(self.horizontalWidget_3, 0, 0, 1, 1)
        self.rotate_src_view = ImageView(parent=self.image_rotate_widget)
        self.rotate_src_view.setProperty("isClickable", True)
        self.rotate_src_view.setObjectName("rotate_src_view")
        self.gridLayout_4.addWidget(self.rotate_src_view, 3, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.rotate_save_button = QtWidgets.QPushButton(parent=self.image_rotate_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotate_save_button.sizePolicy().hasHeightForWidth())
        self.rotate_save_button.setSizePolicy(sizePolicy)
        self.rotate_save_button.setMinimumSize(QtCore.QSize(80, 40))
        self.rotate_save_button.setObjectName("rotate_save_button")
        self.horizontalLayout_6.addWidget(self.rotate_save_button)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 0, 2, 1, 1)
        self.verticalWidget = QtWidgets.QWidget(parent=self.image_rotate_widget)
        self.verticalWidget.setMinimumSize(QtCore.QSize(30, 0))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setContentsMargins(-1, 120, -1, 120)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rotate_button = QtWidgets.QPushButton(parent=self.verticalWidget)
        self.rotate_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotate_button.sizePolicy().hasHeightForWidth())
        self.rotate_button.setSizePolicy(sizePolicy)
        self.rotate_button.setMinimumSize(QtCore.QSize(120, 60))
        self.rotate_button.setObjectName("rotate_button")
        self.verticalLayout_2.addWidget(self.rotate_button)
        self.gridLayout_4.addWidget(self.verticalWidget, 3, 1, 1, 1)
        self.gridLayout_7.addWidget(self.image_rotate_widget, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.image_rotate_page)
        self.histogram_page = QtWidgets.QWidget()
        self.histogram_page.setObjectName("histogram_page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.histogram_page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.histogram_widget = QtWidgets.QWidget(parent=self.histogram_page)
        self.histogram_widget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.histogram_widget.sizePolicy().hasHeightForWidth())
        self.histogram_widget.setSizePolicy(sizePolicy)
        self.histogram_widget.setAcceptDrops(False)
        self.histogram_widget.setAutoFillBackground(False)
        self.histogram_widget.setObjectName("histogram_widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.histogram_widget)
        self.gridLayout_5.setContentsMargins(20, 20, 20, 20)
        self.gridLayout_5.setHorizontalSpacing(20)
        self.gridLayout_5.setObjectName("gridLayout_5")
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
        self.gridLayout_5.addLayout(self.horizontalLayout_7, 0, 1, 1, 1)
        self.histogram_src_view = ImageView(parent=self.histogram_widget)
        self.histogram_src_view.setProperty("isClickable", True)
        self.histogram_src_view.setObjectName("histogram_src_view")
        self.gridLayout_5.addWidget(self.histogram_src_view, 3, 0, 1, 1)
        self.histogram_dst_view = ImageView(parent=self.histogram_widget)
        self.histogram_dst_view.setProperty("isClickable", False)
        self.histogram_dst_view.setObjectName("histogram_dst_view")
        self.gridLayout_5.addWidget(self.histogram_dst_view, 3, 1, 1, 1)
        self.horizontalWidget_4 = QtWidgets.QWidget(parent=self.histogram_widget)
        self.horizontalWidget_4.setMinimumSize(QtCore.QSize(0, 20))
        self.horizontalWidget_4.setObjectName("horizontalWidget_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalWidget_4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.histogram_open_button = QtWidgets.QPushButton(parent=self.horizontalWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.histogram_open_button.sizePolicy().hasHeightForWidth())
        self.histogram_open_button.setSizePolicy(sizePolicy)
        self.histogram_open_button.setMinimumSize(QtCore.QSize(80, 40))
        self.histogram_open_button.setObjectName("histogram_open_button")
        self.horizontalLayout_8.addWidget(self.histogram_open_button)
        self.histogram_clear_button = QtWidgets.QPushButton(parent=self.horizontalWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.histogram_clear_button.sizePolicy().hasHeightForWidth())
        self.histogram_clear_button.setSizePolicy(sizePolicy)
        self.histogram_clear_button.setMinimumSize(QtCore.QSize(80, 40))
        self.histogram_clear_button.setObjectName("histogram_clear_button")
        self.horizontalLayout_8.addWidget(self.histogram_clear_button)
        self.gridLayout_5.addWidget(self.horizontalWidget_4, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.histogram_widget, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.histogram_page)
        self.noise_generation_page = QtWidgets.QWidget()
        self.noise_generation_page.setObjectName("noise_generation_page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.noise_generation_page)
        self.gridLayout_3.setContentsMargins(0, 0, 0, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.noise_generation_widget = QtWidgets.QWidget(parent=self.noise_generation_page)
        self.noise_generation_widget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noise_generation_widget.sizePolicy().hasHeightForWidth())
        self.noise_generation_widget.setSizePolicy(sizePolicy)
        self.noise_generation_widget.setAcceptDrops(False)
        self.noise_generation_widget.setAutoFillBackground(False)
        self.noise_generation_widget.setObjectName("noise_generation_widget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.noise_generation_widget)
        self.gridLayout_6.setContentsMargins(20, 20, 20, 20)
        self.gridLayout_6.setHorizontalSpacing(20)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalWidget_5 = QtWidgets.QWidget(parent=self.noise_generation_widget)
        self.horizontalWidget_5.setMinimumSize(QtCore.QSize(0, 20))
        self.horizontalWidget_5.setObjectName("horizontalWidget_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalWidget_5)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.noise_generation_open_button = QtWidgets.QPushButton(parent=self.horizontalWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noise_generation_open_button.sizePolicy().hasHeightForWidth())
        self.noise_generation_open_button.setSizePolicy(sizePolicy)
        self.noise_generation_open_button.setMinimumSize(QtCore.QSize(80, 40))
        self.noise_generation_open_button.setObjectName("noise_generation_open_button")
        self.horizontalLayout_9.addWidget(self.noise_generation_open_button)
        self.noise_generation_clear_button = QtWidgets.QPushButton(parent=self.horizontalWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noise_generation_clear_button.sizePolicy().hasHeightForWidth())
        self.noise_generation_clear_button.setSizePolicy(sizePolicy)
        self.noise_generation_clear_button.setMinimumSize(QtCore.QSize(80, 40))
        self.noise_generation_clear_button.setMaximumSize(QtCore.QSize(80, 16777215))
        self.noise_generation_clear_button.setObjectName("noise_generation_clear_button")
        self.horizontalLayout_9.addWidget(self.noise_generation_clear_button)
        self.gridLayout_6.addWidget(self.horizontalWidget_5, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.noise_generation_generate_button = QtWidgets.QPushButton(parent=self.noise_generation_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noise_generation_generate_button.sizePolicy().hasHeightForWidth())
        self.noise_generation_generate_button.setSizePolicy(sizePolicy)
        self.noise_generation_generate_button.setMinimumSize(QtCore.QSize(40, 40))
        self.noise_generation_generate_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.noise_generation_generate_button.setObjectName("noise_generation_generate_button")
        self.horizontalLayout_10.addWidget(self.noise_generation_generate_button)
        self.noise_generation_save_button = QtWidgets.QPushButton(parent=self.noise_generation_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noise_generation_save_button.sizePolicy().hasHeightForWidth())
        self.noise_generation_save_button.setSizePolicy(sizePolicy)
        self.noise_generation_save_button.setMinimumSize(QtCore.QSize(80, 40))
        self.noise_generation_save_button.setObjectName("noise_generation_save_button")
        self.horizontalLayout_10.addWidget(self.noise_generation_save_button)
        self.gridLayout_6.addLayout(self.horizontalLayout_10, 0, 2, 1, 1)
        self.noise_generation_src_view = ImageView(parent=self.noise_generation_widget)
        self.noise_generation_src_view.setProperty("isClickable", True)
        self.noise_generation_src_view.setObjectName("noise_generation_src_view")
        self.gridLayout_6.addWidget(self.noise_generation_src_view, 3, 0, 1, 1)
        self.noise_generation_dst_view = ImageView(parent=self.noise_generation_widget)
        self.noise_generation_dst_view.setProperty("isClickable", False)
        self.noise_generation_dst_view.setObjectName("noise_generation_dst_view")
        self.gridLayout_6.addWidget(self.noise_generation_dst_view, 3, 2, 1, 1)
        self.noise_generation_noise_view = ImageView(parent=self.noise_generation_widget)
        self.noise_generation_noise_view.setProperty("isClickable", False)
        self.noise_generation_noise_view.setObjectName("noise_generation_noise_view")
        self.gridLayout_6.addWidget(self.noise_generation_noise_view, 3, 1, 1, 1)
        self.noise_generation_src_histogram_view = ImageView(parent=self.noise_generation_widget)
        self.noise_generation_src_histogram_view.setProperty("isClickable", False)
        self.noise_generation_src_histogram_view.setObjectName("noise_generation_src_histogram_view")
        self.gridLayout_6.addWidget(self.noise_generation_src_histogram_view, 4, 0, 1, 1)
        self.noise_generation_noise_histogram_view = ImageView(parent=self.noise_generation_widget)
        self.noise_generation_noise_histogram_view.setProperty("isClickable", False)
        self.noise_generation_noise_histogram_view.setObjectName("noise_generation_noise_histogram_view")
        self.gridLayout_6.addWidget(self.noise_generation_noise_histogram_view, 4, 1, 1, 1)
        self.noise_generation_dst_histogram_view = ImageView(parent=self.noise_generation_widget)
        self.noise_generation_dst_histogram_view.setProperty("isClickable", False)
        self.noise_generation_dst_histogram_view.setObjectName("noise_generation_dst_histogram_view")
        self.gridLayout_6.addWidget(self.noise_generation_dst_histogram_view, 4, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.noise_generation_option = QtWidgets.QComboBox(parent=self.noise_generation_widget)
        self.noise_generation_option.setMinimumSize(QtCore.QSize(140, 0))
        self.noise_generation_option.setObjectName("noise_generation_option")
        self.noise_generation_option.addItem("")
        self.noise_generation_option.addItem("")
        self.verticalLayout.addWidget(self.noise_generation_option)
        self.noise_input_widget = QtWidgets.QStackedWidget(parent=self.noise_generation_widget)
        self.noise_input_widget.setObjectName("noise_input_widget")
        self.gaussian_noise_input_page = QtWidgets.QWidget()
        self.gaussian_noise_input_page.setObjectName("gaussian_noise_input_page")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.gaussian_noise_input_page)
        self.horizontalLayout.setContentsMargins(12, 0, 0, 0)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_4 = QtWidgets.QWidget(parent=self.gaussian_noise_input_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout.addWidget(self.widget_4)
        self.label = QtWidgets.QLabel(parent=self.gaussian_noise_input_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.gaussian_sd_input = QtWidgets.QDoubleSpinBox(parent=self.gaussian_noise_input_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gaussian_sd_input.sizePolicy().hasHeightForWidth())
        self.gaussian_sd_input.setSizePolicy(sizePolicy)
        self.gaussian_sd_input.setMinimum(0.01)
        self.gaussian_sd_input.setMaximum(99999999.0)
        self.gaussian_sd_input.setSingleStep(0.1)
        self.gaussian_sd_input.setProperty("value", 1.0)
        self.gaussian_sd_input.setObjectName("gaussian_sd_input")
        self.horizontalLayout.addWidget(self.gaussian_sd_input)
        self.widget_3 = QtWidgets.QWidget(parent=self.gaussian_noise_input_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout.addWidget(self.widget_3)
        self.noise_input_widget.addWidget(self.gaussian_noise_input_page)
        self.salt_noise_input_page = QtWidgets.QWidget()
        self.salt_noise_input_page.setObjectName("salt_noise_input_page")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.salt_noise_input_page)
        self.horizontalLayout_3.setContentsMargins(0, 0, 15, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_5 = QtWidgets.QWidget(parent=self.salt_noise_input_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_3.addWidget(self.widget_5)
        self.salt_percent_input = QtWidgets.QDoubleSpinBox(parent=self.salt_noise_input_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.salt_percent_input.sizePolicy().hasHeightForWidth())
        self.salt_percent_input.setSizePolicy(sizePolicy)
        self.salt_percent_input.setMinimum(0.0)
        self.salt_percent_input.setMaximum(100.0)
        self.salt_percent_input.setProperty("value", 0.0)
        self.salt_percent_input.setObjectName("salt_percent_input")
        self.horizontalLayout_3.addWidget(self.salt_percent_input)
        self.label_2 = QtWidgets.QLabel(parent=self.salt_noise_input_page)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.widget_2 = QtWidgets.QWidget(parent=self.salt_noise_input_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3.addWidget(self.widget_2)
        self.noise_input_widget.addWidget(self.salt_noise_input_page)
        self.verticalLayout.addWidget(self.noise_input_widget)
        self.gridLayout_6.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.gridLayout_6.setRowStretch(0, 1)
        self.gridLayout_6.setRowStretch(3, 10)
        self.gridLayout_6.setRowStretch(4, 10)
        self.gridLayout_3.addWidget(self.noise_generation_widget, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.noise_generation_page)
        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)
        AIP61247001S.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=AIP61247001S)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 839, 36))
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
        self.stackedWidget.setCurrentIndex(2)
        self.noise_input_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AIP61247001S)

    def retranslateUi(self, AIP61247001S):
        _translate = QtCore.QCoreApplication.translate
        AIP61247001S.setWindowTitle(_translate("AIP61247001S", "AIP61247001S"))
        self.rotate_switch_button.setText(_translate("AIP61247001S", "Image Rotate"))
        self.histogram_switch_button.setText(_translate("AIP61247001S", "Histogram"))
        self.noise_generation_switch_button.setText(_translate("AIP61247001S", "Noise Generation"))
        self.rotate_open_button.setText(_translate("AIP61247001S", "Open"))
        self.rotate_clear_button.setText(_translate("AIP61247001S", "Clear"))
        self.rotate_save_button.setText(_translate("AIP61247001S", "Save"))
        self.rotate_button.setText(_translate("AIP61247001S", "Rotate"))
        self.histogram_save_button.setText(_translate("AIP61247001S", "Save"))
        self.histogram_open_button.setText(_translate("AIP61247001S", "Open"))
        self.histogram_clear_button.setText(_translate("AIP61247001S", "Clear"))
        self.noise_generation_open_button.setText(_translate("AIP61247001S", "Open"))
        self.noise_generation_clear_button.setText(_translate("AIP61247001S", "Clear"))
        self.noise_generation_generate_button.setText(_translate("AIP61247001S", "Generate"))
        self.noise_generation_save_button.setText(_translate("AIP61247001S", "Save"))
        self.noise_generation_option.setItemText(0, _translate("AIP61247001S", "Gaussian"))
        self.noise_generation_option.setItemText(1, _translate("AIP61247001S", "Salt and pepper"))
        self.label.setText(_translate("AIP61247001S", "σ:"))
        self.label_2.setText(_translate("AIP61247001S", "%"))
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
        fname = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "${HOME}",
            "Image Files (*.jpg *.jpeg *.png *.bmp *.ppm)",
        )
        if fname[0]:
            clear_image()
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

class ResizeEventFilter(QObject):
    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.Resize:
            new_size = event.size()
            new_width = new_size.width()
            new_height = new_size.height()

            print(f"Window resized to width: {new_width}, height: {new_height}")
            update_views()

        return super().eventFilter(watched, event)

def setupScript(ui:Ui_AIP61247001S):
    global AIP61247001S
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
    ui.noise_generation_open_button.clicked.connect(open_image)
    ui.noise_generation_clear_button.clicked.connect(clear_image)
    ui.noise_generation_save_button.clicked.connect(save_image)
    ui.noise_generation_option.currentIndexChanged.connect(noise_generate_mode_change)
    ui.noise_generation_generate_button.clicked.connect(noise_generate)


def update_views():
    page = ui.stackedWidget.currentIndex()
    if page == 0:
        ui.rotate_src_view.update()
        ui.rotate_dst_view.update()
    elif page == 1:
        ui.histogram_src_view.update()
        ui.histogram_dst_view.update()
    elif page == 2:
        ui.noise_generation_src_view.update()
        ui.noise_generation_noise_view.update()
        ui.noise_generation_dst_view.update()
        ui.noise_generation_src_histogram_view.update()
        ui.noise_generation_noise_histogram_view.update()
        ui.noise_generation_dst_histogram_view.update()
@QtCore.pyqtSlot()
def open_image():
    page = ui.stackedWidget.currentIndex()
    if page == 0:
        ui.rotate_src_view.open_image()
    elif page == 1:
        ui.histogram_src_view.open_image()
        ui.histogram_dst_view.setImage(histogram_image(ui.histogram_src_view.image))
        ui.histogram_dst_view.update()
    elif page == 2:
        ui.noise_generation_src_view.open_image()
        ui.noise_generation_src_histogram_view.setImage(histogram_image(ui.noise_generation_src_view.image))
        ui.noise_generation_src_histogram_view.update()
@QtCore.pyqtSlot()
def save_image():
    page = ui.stackedWidget.currentIndex()
    if page == 0:
        ui.rotate_dst_view.save_image()
    elif page == 1:
        ui.histogram_dst_view.save_image()
    elif page == 2:
        ui.noise_generation_dst_view.save_image()
@QtCore.pyqtSlot()
def clear_image():
    page = ui.stackedWidget.currentIndex()
    if page == 0:
        ui.rotate_src_view.clear()
        ui.rotate_dst_view.clear()
    elif page == 1:
        ui.histogram_src_view.clear()
        ui.histogram_dst_view.clear()
    elif page == 2:
        ui.noise_generation_src_view.clear()
        ui.noise_generation_src_histogram_view.clear()
        ui.noise_generation_noise_view.clear()
        ui.noise_generation_noise_histogram_view.clear()
        ui.noise_generation_dst_view.clear()
        ui.noise_generation_dst_histogram_view.clear()
@QtCore.pyqtSlot()
def switch_page(page):
    ui.stackedWidget.setCurrentIndex(page)
    print(ui.stackedWidget.currentIndex())
@QtCore.pyqtSlot()
def rotate():
    if ui.rotate_src_view.image is None:
        return
    if ui.rotate_dst_view.image is None:
        ui.rotate_dst_view.setImage(ui.rotate_src_view.image)
    ui.rotate_dst_view.setImage(rotate_image(ui.rotate_dst_view.image))
    ui.rotate_dst_view.update()
@QtCore.pyqtSlot()
def noise_generate_mode_change():
    ui.noise_input_widget.setCurrentIndex(ui.noise_generation_option.currentIndex())
@QtCore.pyqtSlot()
def noise_generate():
    if ui.noise_generation_src_view.image is None:
        return
    if ui.noise_generation_option.currentIndex() == 0:
        # Gaussian Noise
        noise, noisy_image = gaussian_noise(ui.noise_generation_src_view.image, ui.gaussian_sd_input.value())
    elif ui.noise_generation_option.currentIndex() == 1:
        # Salt and pepper Noise
        noise, noisy_image = salt_and_pepper_noise(ui.noise_generation_src_view.image, ui.salt_percent_input.value())
    ui.noise_generation_noise_view.setImage(noise)
    ui.noise_generation_noise_histogram_view.setImage(histogram_image(noise))
    ui.noise_generation_dst_view.setImage(noisy_image)
    ui.noise_generation_dst_histogram_view.setImage(histogram_image(noisy_image))
    ui.noise_generation_noise_view.update()
    ui.noise_generation_noise_histogram_view.update()
    ui.noise_generation_dst_view.update()
    ui.noise_generation_dst_histogram_view.update()

    


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
    if len(image.shape) == 2 or image.shape[2] == 1:
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
    plt.ylabel('Frequency', fontsize=14, color='black')

    ax1 = plt.subplot(gs[1])
    plt.imshow(gradient, cmap="gray", aspect='auto')
    cbar = plt.colorbar(orientation='horizontal', cax=ax1)
    # ax1.set_xlim(0, 256)

    plt.xticks(ax1.get_xticks())
    plt.xlim(0, 256)
    plt.xlabel('Intensity', fontsize=14, color='black')

    plt.tight_layout()

    canvas = FigureCanvasAgg(fig)
    canvas.draw()  # Draw the canvas, cache the renderer

    image_flat = np.frombuffer(canvas.tostring_argb(), dtype='uint8')
    hist_image = image_flat.reshape(*reversed(canvas.get_width_height()), 4)
    hist_image = hist_image[:, :, ::-1]
    hist_image = hist_image[:, :, :3]
    
    return hist_image

@jit
def gaussian_noise_process(height, width, channel, sigma, noise, noisy_image):
    for z in range(channel):
        for y in range(height):
            for x in range(0, width, 2):
                r1, r2 = np.random.rand(), np.random.rand()

                z1 = sigma * np.cos(2 * np.pi * r2) * np.sqrt(-2 * np.log(r1))
                z2 = sigma * np.sin(2 * np.pi * r2) * np.sqrt(-2 * np.log(r1))

                noise[y, x, z] = z1 + 127
                noisy_image[y, x, z] = noisy_image[y, x, z] + z1

                if x + 1 < width:
                    noise[y, x + 1, z] = z2 + 127
                    noisy_image[y, x + 1, z] = noisy_image[y, x + 1, z] + z2

# @jit
def gaussian_noise(image, sigma: float):
    if image is None:
        return
    if len(image.shape) == 2:
        height, width = image.shape
        channel = 1
    else:
        height, width, channel = image.shape

    G = 256 

    noise = np.zeros((height, width, channel), dtype=np.uint8)
    noisy_image = np.copy(image)
    noisy_image = np.reshape(noisy_image, (height, width, channel))

    gaussian_noise_process(height, width, channel, sigma, noise, noisy_image)    
    # for z in range(channel):
    #     for y in range(height):
    #         for x in range(0, width, 2):
    #             r1, r2 = np.random.rand(), np.random.rand()

    #             z1 = sigma * np.cos(2 * np.pi * r2) * np.sqrt(-2 * np.log(r1))
    #             z2 = sigma * np.sin(2 * np.pi * r2) * np.sqrt(-2 * np.log(r1))

    #             noise[y, x, z] = z1
    #             noisy_image[y, x, z] = noisy_image[y, x, z] + z1

    #             if x + 1 < width:
    #                 noise[y, x + 1, z] = z2
    #                 noisy_image[y, x + 1, z] = noisy_image[y, x + 1, z] + z2


    noise = np.clip(noise, 0, G - 1)
    noisy_image = np.clip(noisy_image, 0, G - 1)

    return noise, noisy_image

def salt_and_pepper_noise(image, percentage:float):
    if image is None:
        return
    if len(image.shape) == 2:
        height, width = image.shape
        channel = 1
    else:
        height, width, channel = image.shape

    noise = np.zeros((height, width, channel), dtype=np.uint8)
    noise.fill(127)
    noisy_image = np.copy(image)
    noisy_image = np.reshape(noisy_image, (height, width, channel))

    num_pixels = int(percentage / 100 * height * width)

    salt_coords = [np.random.randint(0, height, num_pixels//2), np.random.randint(0, width, num_pixels//2)]
    pepper_coords = [np.random.randint(0, height, num_pixels//2), np.random.randint(0, width, num_pixels//2)]

    noise[salt_coords[0], salt_coords[1], :] = 255
    noise[pepper_coords[0], pepper_coords[1], :] = 0
    noisy_image[salt_coords[0], salt_coords[1], :] = 255
    noisy_image[pepper_coords[0], pepper_coords[1], :] = 0

    return noise, noisy_image

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AIP61247001S = QtWidgets.QMainWindow()
    ui = Ui_AIP61247001S()
    ui.setupUi(AIP61247001S)
    setupScript(ui)
    resize_event_filter = ResizeEventFilter()
    AIP61247001S.installEventFilter(resize_event_filter)
    AIP61247001S.show()
    sys.exit(app.exec())
