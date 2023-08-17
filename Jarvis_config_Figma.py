from PyQt5 import QtCore, QtGui, QtWidgets
from res_rc import *

class Ui_Jarvis(object):
    def setupUi(self, Jarvis):
        Jarvis.setObjectName("Jarvis")
        Jarvis.setEnabled(True)
        Jarvis.resize(1200, 850)
        Jarvis.setMinimumSize(QtCore.QSize(1200, 850))
        Jarvis.setMaximumSize(QtCore.QSize(1200, 850))

        Jarvis.setWindowFlag( QtCore.Qt.FramelessWindowHint )
        Jarvis.setAttribute( QtCore.Qt.WA_TranslucentBackground )

        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setBold(True)
        font.setWeight(75)
        Jarvis.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Jarvis.setWindowIcon(icon)
        Jarvis.setStyleSheet("background: rgba( 0,0,0,0 );")
        Jarvis.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        Jarvis.setTabShape(QtWidgets.QTabWidget.Rounded)
        Jarvis.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(Jarvis)
        self.centralwidget.setMinimumSize(QtCore.QSize(1200, 850))
        self.centralwidget.setMaximumSize(QtCore.QSize(1200, 850))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.left_panel = QtWidgets.QLabel(self.centralwidget)
        self.left_panel.setGeometry(QtCore.QRect(0, 50, 450, 800))
        self.left_panel.setStyleSheet("background: url(:/Jarvis/Night/left-panel.png);")
        self.left_panel.setText("")
        self.left_panel.setObjectName("left_panel")
        self.menu = QtWidgets.QPushButton(self.centralwidget)
        self.menu.setGeometry(QtCore.QRect(22, 50, 406, 81))
        self.menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu.setStyleSheet("background: url(:/Jarvis/Night/Menu.png);\n"
"border-radius: 0px;")
        self.menu.setText("")
        self.menu.setObjectName("menu")
        self.history = QtWidgets.QTextBrowser(self.centralwidget)
        self.history.setGeometry(QtCore.QRect(475, 70, 700, 500))
        self.history.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.history.setStyleSheet("background: url(:/Jarvis/Night/History-b.png);\n"
"border-radius: 15px;")
        self.history.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.history.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.history.setObjectName("history")
        self.weather = QtWidgets.QLabel(self.centralwidget)
        self.weather.setGeometry(QtCore.QRect(475, 655, 344, 182))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.weather.setFont(font)
        self.weather.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.weather.setStyleSheet("background: url(:/Jarvis/Night/Weather.png);\n"
"color: rgba(255,255,255,0.8);\n"
"font-size: 20px;")
        self.weather.setText("")
        self.weather.setAlignment(QtCore.Qt.AlignCenter)
        self.weather.setObjectName("weather")
        self.now_time = QtWidgets.QLabel(self.centralwidget)
        self.now_time.setGeometry(QtCore.QRect(831, 655, 344, 182))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.now_time.setFont(font)
        self.now_time.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.now_time.setStyleSheet("background: url(:/Jarvis/Night/Time.png);\n"
"color: rgba(255,255,255,0.8);")
        self.now_time.setText("")
        self.now_time.setAlignment(QtCore.Qt.AlignCenter)
        self.now_time.setObjectName("now_time")
        self.jarvis = QtWidgets.QPushButton(self.centralwidget)
        self.jarvis.setGeometry(QtCore.QRect(175, 354, 100, 29))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(99)
        self.jarvis.setFont(font)
        self.jarvis.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.jarvis.setStyleSheet("font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 900;\n"
"font-size: 24px;\n"
"line-height: 29px;\n"
"color: rgba(255,255,255,0.8);\n"
"border-radius: 0px;\n"
"background: rgba(0,0,0,0);")
        self.jarvis.setObjectName("jarvis")
        self.setting = QtWidgets.QPushButton(self.centralwidget)
        self.setting.setGeometry(QtCore.QRect(157, 435, 136, 29))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(99)
        self.setting.setFont(font)
        self.setting.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setting.setStyleSheet("font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 900;\n"
"font-size: 24px;\n"
"line-height: 29px;\n"
"color: rgba(255,255,255,0.8);\n"
"border-radius: 0px;\n"
"background: rgba(0,0,0,0);")
        self.setting.setObjectName("setting")
        self.list = QtWidgets.QPushButton(self.centralwidget)
        self.list.setGeometry(QtCore.QRect(167, 516, 117, 29))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(99)
        self.list.setFont(font)
        self.list.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.list.setStyleSheet("font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 900;\n"
"font-size: 24px;\n"
"line-height: 29px;\n"
"color: rgba(255,255,255,0.8);\n"
"border-radius: 0px;\n"
"background: rgba(0,0,0,0);")
        self.list.setObjectName("list")
        self.console = QtWidgets.QLineEdit(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(630, 585, 391, 51))
        self.console.setStyleSheet("color: white;\n"
"font-size: 20px;\n"
"background: rgba( 0, 0,255,0.5 );\n"
"padding: 10px;\n"
"border-radius: 10px;")
        self.console.setClearButtonEnabled(False)
        self.console.setObjectName("console")
        self.interface_color = QtWidgets.QLineEdit(self.centralwidget)
        self.interface_color.setGeometry(QtCore.QRect(769, 175, 280, 41))
        self.interface_color.setStyleSheet("color: white;\n"
"font-size: 20px;\n"
"background: rgba( 0, 0,255,0.5 );\n"
"padding: 10px;\n"
"border-radius: 8px;\n"
"font-weight: 500;")
        self.interface_color.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.interface_color.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.interface_color.setDragEnabled(False)
        self.interface_color.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.interface_color.setClearButtonEnabled(False)
        self.interface_color.setObjectName("interface_color")
        self.save_settings = QtWidgets.QPushButton(self.centralwidget)
        self.save_settings.setGeometry(QtCore.QRect(750, 430, 141, 51))
        self.save_settings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_settings.setStyleSheet("color: white;\n"
"background: rgba( 0,0,0,0 );\n"
"font-weight: 700;\n"
"font-size: 20px;")
        self.save_settings.setCheckable(False)
        self.save_settings.setAutoDefault(False)
        self.save_settings.setObjectName("save_settings")
        self.city_name = QtWidgets.QLineEdit(self.centralwidget)
        self.city_name.setGeometry(QtCore.QRect(649, 126, 340, 41))
        self.city_name.setStyleSheet("color: white;\n"
"font-size: 20px;\n"
"background: rgba( 0, 0,255,0.5 );\n"
"padding: 10px;\n"
"border-radius: 8px;\n"
"font-weight: 500;")
        self.city_name.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.city_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.city_name.setDragEnabled(False)
        self.city_name.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.city_name.setClearButtonEnabled(False)
        self.city_name.setObjectName("city_name")
        self.border_px = QtWidgets.QLineEdit(self.centralwidget)
        self.border_px.setGeometry(QtCore.QRect(779, 225, 280, 41))
        self.border_px.setStyleSheet("color: white;\n"
"font-size: 20px;\n"
"background: rgba( 0, 0,255,0.5 );\n"
"padding: 10px;\n"
"border-radius: 8px;\n"
"font-weight: 500;")
        self.border_px.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.border_px.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.border_px.setDragEnabled(False)
        self.border_px.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.border_px.setClearButtonEnabled(False)
        self.border_px.setObjectName("border_px")
        self.city = QtWidgets.QLabel(self.centralwidget)
        self.city.setGeometry(QtCore.QRect(549, 110, 101, 71))
        self.city.setStyleSheet("color: white;\n"
"font-size: 20px;\n"
"font-weight: 700;\n"
"background: rgba(0,0,0,0);\n"
"padding-left: 20px;")
        self.city.setObjectName("city")
        self.width_border = QtWidgets.QLabel(self.centralwidget)
        self.width_border.setEnabled(True)
        self.width_border.setGeometry(QtCore.QRect(549, 210, 231, 71))
        self.width_border.setStyleSheet("color: white;\n"
"font-size: 20px;\n"
"font-weight: 700;\n"
"background: rgba(0,0,0,0);\n"
"padding-left: 20px;")
        self.width_border.setObjectName("width_border")
        self.input_check = QtWidgets.QLabel(self.centralwidget)
        self.input_check.setGeometry(QtCore.QRect(570, 300, 511, 121))
        self.input_check.setStyleSheet("color: white;\n"
"font-size: 20px;\n"
"font-weight: 700;\n"
"background: rgba(0,0,0,0);\n"
"")
        self.input_check.setText("")
        self.input_check.setTextFormat(QtCore.Qt.AutoText)
        self.input_check.setScaledContents(False)
        self.input_check.setAlignment(QtCore.Qt.AlignCenter)
        self.input_check.setObjectName("input_check")
        self.color_interface = QtWidgets.QLabel(self.centralwidget)
        self.color_interface.setGeometry(QtCore.QRect(540, 160, 221, 71))
        self.color_interface.setStyleSheet("color: white;\n"
"font-size: 20px;\n"
"font-weight: 700;\n"
"background: rgba(0,0,0,0);\n"
"padding-left: 20px;")
        self.color_interface.setObjectName("color_interface")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(0, 790, 111, 61))
        self.exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit.setStyleSheet("font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 900;\n"
"font-size: 22px;\n"
"line-height: 29px;\n"
"color: rgba(255,255,255,0.8);\n"
"border-radius: 0px;\n"
"background: rgba(0,0,0,0);")
        self.exit.setCheckable(False)
        self.exit.setAutoDefault(False)
        self.exit.setObjectName("exit")
        self.commands = QtWidgets.QTextBrowser(self.centralwidget)
        self.commands.setGeometry(QtCore.QRect(475, 70, 700, 500))
        self.commands.setStyleSheet("background: url(:/Jarvis/Night/History-b.png);\n"
"border-radius: 15px;")
        self.commands.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.commands.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.commands.setObjectName("commands")
        self.about = QtWidgets.QTextBrowser(self.centralwidget)
        self.about.setGeometry(QtCore.QRect(475, 70, 700, 500))
        self.about.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.about.setStyleSheet("background: url(:/Jarvis/Night/History-b.png);\n"
"border-radius: 15px;")
        self.about.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.about.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.about.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.about.setObjectName("about")
        self.menu2 = QtWidgets.QPushButton(self.centralwidget)
        self.menu2.setGeometry(QtCore.QRect(210, 140, 29, 24))
        self.menu2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menu2.setStyleSheet("background: url(:/Jarvis/Night/Jarvis.png);\n"
"border-radius: 0px;")
        self.menu2.setText("")
        self.menu2.setObjectName("menu2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1200, 50))
        self.label.setStyleSheet("background: url(:/Jarvis/Night/Bar.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 1200, 800))
        self.label_2.setStyleSheet("background: url(:/Jarvis/Night/Main.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1124, 15, 20, 20))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("border-radius: 0px;\n"
"background: url(:/Jarvis/Night/Sp.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1154, 15, 20, 20))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-radius: 0px;\n"
"background: url(:/Jarvis/Night/Close.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.addons = QtWidgets.QPushButton(self.centralwidget)
        self.addons.setGeometry(QtCore.QRect(145, 597, 161, 29))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(99)
        self.addons.setFont(font)
        self.addons.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addons.setStyleSheet("font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 900;\n"
"font-size: 24px;\n"
"line-height: 29px;\n"
"color: rgba(255,255,255,0.8);\n"
"border-radius: 0px;\n"
"background: rgba(0,0,0,0);")
        self.addons.setObjectName("addons")
        self.addon = QtWidgets.QTextBrowser(self.centralwidget)
        self.addon.setGeometry(QtCore.QRect(475, 70, 700, 760))
        self.addon.setStyleSheet("background: url(:/Jarvis/Night/History-hh.png);\n"
"border-radius: 15px;")
        self.addon.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.addon.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.addon.setObjectName("addon")
        self.tele = QtWidgets.QLabel(self.centralwidget)
        self.tele.setGeometry(QtCore.QRect(570, 360, 511, 121))
        self.tele.setStyleSheet("color: white;\n"
"font-size: 20px;\n"
"font-weight: 700;\n"
"background: rgba(0,0,0,0);")
        self.tele.setText("")
        self.tele.setTextFormat(QtCore.Qt.AutoText)
        self.tele.setScaledContents(False)
        self.tele.setAlignment(QtCore.Qt.AlignCenter)
        self.tele.setObjectName("tele")
        self.paths = QtWidgets.QPushButton(self.centralwidget)
        self.paths.setGeometry(QtCore.QRect(752, 500, 141, 51))
        self.paths.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.paths.setStyleSheet("color: white;\n"
"background: rgba( 0,0,0,0 );\n"
"font-weight: 700;\n"
"font-size: 20px;\n"
"text-align: center;")
        self.paths.setCheckable(False)
        self.paths.setAutoDefault(False)
        self.paths.setObjectName("paths")
        self.color_interface_2 = QtWidgets.QLabel(self.centralwidget)
        self.color_interface_2.setGeometry(QtCore.QRect(550, 5, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.color_interface_2.setFont(font)
        self.color_interface_2.setStyleSheet("color: white;\n"
"font-size: 20px;\n"
"font-weight: 700;\n"
"background: rgba(0,0,0,0);")
        self.color_interface_2.setObjectName("color_interface_2")
        self.add_programm = QtWidgets.QPushButton(self.centralwidget)
        self.add_programm.setGeometry(QtCore.QRect(752, 70, 141, 51))
        self.add_programm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_programm.setStyleSheet("color: white;\n"
"background: rgba( 0,0,0,0 );\n"
"font-weight: 700;\n"
"font-size: 20px;\n"
"text-align: center;")
        self.add_programm.setCheckable(False)
        self.add_programm.setAutoDefault(False)
        self.add_programm.setObjectName("add_programm")
        self.label_2.raise_()
        self.history.raise_()
        self.commands.raise_()
        self.left_panel.raise_()
        self.menu.raise_()
        self.weather.raise_()
        self.now_time.raise_()
        self.jarvis.raise_()
        self.setting.raise_()
        self.list.raise_()
        self.console.raise_()
        self.exit.raise_()
        self.menu2.raise_()
        self.label.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.addons.raise_()
        self.about.raise_()
        self.save_settings.raise_()
        self.width_border.raise_()
        self.input_check.raise_()
        self.interface_color.raise_()
        self.border_px.raise_()
        self.city.raise_()
        self.city_name.raise_()
        self.color_interface.raise_()
        self.paths.raise_()
        self.color_interface_2.raise_()
        self.add_programm.raise_()
        self.addon.raise_()
        self.tele.raise_()
        Jarvis.setCentralWidget(self.centralwidget)

        self.retranslateUi(Jarvis)
        QtCore.QMetaObject.connectSlotsByName(Jarvis)

    def retranslateUi(self, Jarvis):
        _translate = QtCore.QCoreApplication.translate
        Jarvis.setWindowTitle(_translate("Jarvis", "Jarvis"))
        self.jarvis.setText(_translate("Jarvis", "Главная"))
        self.setting.setText(_translate("Jarvis", "Настройки"))
        self.list.setText(_translate("Jarvis", "Команды"))
        self.save_settings.setText(_translate("Jarvis", "Сохранить"))
        self.city.setText(_translate("Jarvis", "Город:"))
        self.width_border.setText(_translate("Jarvis", "Ширина барьеров:"))
        self.color_interface.setText(_translate("Jarvis", "Цвет интерфейса:"))
        self.exit.setText(_translate("Jarvis", "Выход"))
        self.commands.setHtml(_translate("Jarvis", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20px;\"><br /></p></body></html>"))
        self.about.setHtml(_translate("Jarvis", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.addons.setText(_translate("Jarvis", "Дополнения"))
        self.addon.setHtml(_translate("Jarvis", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20px;\"><br /></p></body></html>"))
        self.paths.setText(_translate("Jarvis", "Программы"))
        self.color_interface_2.setText(_translate("Jarvis", "Jarvis"))
        self.add_programm.setText(_translate("Jarvis", "Добавить"))