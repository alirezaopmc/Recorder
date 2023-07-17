# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import icons_rc

class Ui_RecorderWidget(object):
    def setupUi(self, RecorderWidget):
        if not RecorderWidget.objectName():
            RecorderWidget.setObjectName(u"RecorderWidget")
        RecorderWidget.resize(800, 600)
        RecorderWidget.setMinimumSize(QSize(800, 600))
        RecorderWidget.setMaximumSize(QSize(800, 600))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(140, 219, 253, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(197, 237, 254, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(70, 110, 126, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(93, 146, 168, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 127))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush8 = QBrush(QColor(70, 110, 126, 127))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        RecorderWidget.setPalette(palette)
        self.verticalLayout = QVBoxLayout(RecorderWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.root = QGroupBox(RecorderWidget)
        self.root.setObjectName(u"root")
        self.gridLayout = QGridLayout(self.root)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.root)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout_2.addWidget(self.progressBar, 1, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.groupBox = QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName(u"groupBox")

        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)

        self.cl_player_files = QComboBox(self.groupBox_3)
        self.cl_player_files.setObjectName(u"cl_player_files")
        self.cl_player_files.setMinimumSize(QSize(300, 0))
        self.cl_player_files.setMaximumSize(QSize(9000, 16777215))

        self.gridLayout_3.addWidget(self.cl_player_files, 1, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setBold(True)
        self.label_4.setFont(font)

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 2, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.groupBox_3)


        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 2)


        self.gridLayout.addWidget(self.widget, 0, 0, 4, 8)

        self.cl_audio_output = QComboBox(self.root)
        self.cl_audio_output.setObjectName(u"cl_audio_output")
        self.cl_audio_output.setMinimumSize(QSize(200, 0))

        self.gridLayout.addWidget(self.cl_audio_output, 4, 5, 1, 1)

        self.pb_stop = QPushButton(self.root)
        self.pb_stop.setObjectName(u"pb_stop")
        self.pb_stop.setEnabled(False)
        icon = QIcon()
        icon.addFile(u":/Main/icons/icons8-stop-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_stop.setIcon(icon)

        self.gridLayout.addWidget(self.pb_stop, 4, 1, 1, 1)

        self.pb_play_n_pause = QPushButton(self.root)
        self.pb_play_n_pause.setObjectName(u"pb_play_n_pause")
        icon1 = QIcon()
        icon1.addFile(u":/Main/icons/icons8-play-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_play_n_pause.setIcon(icon1)

        self.gridLayout.addWidget(self.pb_play_n_pause, 4, 7, 1, 1)

        self.l_audio_input = QLabel(self.root)
        self.l_audio_input.setObjectName(u"l_audio_input")

        self.gridLayout.addWidget(self.l_audio_input, 4, 2, 1, 1)

        self.cl_audio_input = QComboBox(self.root)
        self.cl_audio_input.setObjectName(u"cl_audio_input")
        self.cl_audio_input.setMinimumSize(QSize(200, 0))
        self.cl_audio_input.setMaximumSize(QSize(200, 16777215))
        self.cl_audio_input.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.gridLayout.addWidget(self.cl_audio_input, 4, 3, 1, 1)

        self.pb_record = QPushButton(self.root)
        self.pb_record.setObjectName(u"pb_record")
        self.pb_record.setEnabled(True)
        icon2 = QIcon()
        icon2.addFile(u":/Main/icons/icons8-record-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_record.setIcon(icon2)

        self.gridLayout.addWidget(self.pb_record, 4, 0, 1, 1)

        self.label = QLabel(self.root)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 4, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 4, 6, 1, 1)


        self.verticalLayout.addWidget(self.root)


        self.retranslateUi(RecorderWidget)

        QMetaObject.connectSlotsByName(RecorderWidget)
    # setupUi

    def retranslateUi(self, RecorderWidget):
        RecorderWidget.setWindowTitle(QCoreApplication.translate("RecorderWidget", u"Bareghe Voice Recorder", None))
        self.root.setTitle("")
        self.label_2.setText(QCoreApplication.translate("RecorderWidget", u"00:00", None))
        self.groupBox_2.setTitle("")
        self.groupBox.setTitle("")
        self.groupBox_3.setTitle("")
        self.label_3.setText(QCoreApplication.translate("RecorderWidget", u"File", None))
        self.label_4.setText(QCoreApplication.translate("RecorderWidget", u"Player", None))
        self.pb_stop.setText(QCoreApplication.translate("RecorderWidget", u"Stop", None))
        self.pb_play_n_pause.setText(QCoreApplication.translate("RecorderWidget", u"Play", None))
        self.l_audio_input.setText(QCoreApplication.translate("RecorderWidget", u"Input", None))
        self.cl_audio_input.setCurrentText("")
        self.cl_audio_input.setPlaceholderText("")
        self.pb_record.setText(QCoreApplication.translate("RecorderWidget", u"Record", None))
        self.label.setText(QCoreApplication.translate("RecorderWidget", u"Output", None))
    # retranslateUi

