"""
######################
##                  ##
##  ShadowDarkness  ##
##                  ##
######################"""


# ░░░░░██╗░█████╗░██████╗░██╗░░░██╗██╗░██████╗
# ░░░░░██║██╔══██╗██╔══██╗██║░░░██║██║██╔════╝
# ░░░░░██║███████║██████╔╝╚██╗░██╔╝██║╚█████╗░
# ██╗░░██║██╔══██║██╔══██╗░╚████╔╝░██║░╚═══██╗
# ╚█████╔╝██║░░██║██║░░██║░░╚██╔╝░░██║██████╔╝
# ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═════╝░

# PYQT5 Библиотеки START
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QLineEdit, QDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QTextCursor, QTextDocument
from PyQt5.QtGui import QTextCharFormat, QTextCursor
from PyQt5.QtCore import QMetaType
# PYQT5 Библиотеки START

# UI Дизайн START
from Jarvis_config_Figma import *
# UI Дизайн END

# TELEGRAM Библиотеки START
from tele_bot_config import *
import telebot
from telebot import types
import platform
# TELEGRAM Библиотеки END

import os
import subprocess
import winreg
import threading
import sys
import json
import struct
from bs4 import BeautifulSoup
import requests
import webbrowser
import pyaudio
from config import *
import configparser
import pyautogui
import time
from datetime import datetime
from colorama import init, Fore
from vosk import Model, KaldiRecognizer
from playsound import playsound
from num2words import num2words
from random import randint

weather_text = "" # Текст погоды

config = configparser.ConfigParser() # Инитилизация библиотеки для чтения user_config.ini
config.read( "user_config.ini" ) # Чтение user_config.ini
 
programs = config.items( "Paths" ) # Получение знайчений из [Paths]

user_playlist = config.get( "Params", "you_playlist" ) # Получение значения из [Params] you_playlist
user_playlist = str( user_playlist ).strip( "\"\"" ) # Удаление кавычек

line_border = config.getboolean( "Params", "line_border_color" ) # Получение цвета линий
acces_weather = config.getboolean( "Params", "weather_acces" ) # Получение bool погоды, если false погода отключена, если true, то погода включена

telegram_api = config.get( "Api", "telegram_bot_key" ) # Получение Api ключа тг бота
telegram_api = str( telegram_api ).strip( "\"\"" ) # Удаление кавычек

event_enter = False # Переменая для события нажатия кнопки ENTER

downing_time = config.get( "Params", "shutdown" ) # Получение времени выключения пк в секундах
downing_time = str( downing_time ).strip( "\"\"" ) # Удаление кавычек

you_city = config.get( "Params", "you_city" ) # Получение названия города из user_config.ini
you_city = you_city.strip( "\"\"" ) # Удаление кавычек

url_weather = f"https://wttr.in/{ you_city }?format=%C+%t&lang=ru&forecast" # Url погоды
update_weather = False # Переменная для обновления погоды

video_yt = "https://www.youtube.com/watch?v=" # Ссылка для открытия YouTube видосов, добавить id видео и всё

# Начальные значения Джарвиса
STARTED = True
JARVIS = True
NUM_JARVIS = 0

CHANGE_COLOR = False

init()
# Начальные значения Джарвиса

# Функция рандомных чисел, возвращает число, на вход от какого до какого. Пример: randomazer( 1, 10 )
def randomazer( num1, num2 ):
    return randint( num1, num2 )
# Функция рандомных чисел, возвращает число, на вход от какого до какого. Пример: randomazer( 1, 10 )

# Функция воспроизведения аудио, src - путь к аудио
def playsound_play( src ):
    playsound( src )
# Функция воспроизведения аудио, src - путь к аудио

# Функция для получения погоды и её отображения в интерфейсе
def request_( url ):
    response_ = requests.get( url ) # Заходит на сайт погоды и получает погоду вашего города
    global self_instance
    global weather_text
    global update_weather

    if ( update_weather == False ):
        if response_.status_code == 200: # Проверка если сайт работает
            global weather_text
            weather_text = response_.content.decode( "utf-8" ) # Получает текст погоды в utf-8
            print( weather_text ) # Пишит в консоль погоду полностью
            print( len( weather_text ) ) # Пишит всю длину погоды ( мне нужно было для тестов )

            if len( weather_text ) < 26: # Если длина текста погоды меньше 26
                # ТЕСТЫ
                # weather_text = f"\"{ weather_text }\""
                # weather_text = weather_text.strip( "\"\"" )
                # gui.Update_Weather( self_instance, f"{ weather_text[:25] }\n{ weather_text[-17:] }" )
                # ТЕСТЫ
                gui.Update_Weather( self_instance, weather_text ) # Выводит текст погоды в интерфейс
    
            if len( weather_text ) > 26: # Если длина текста погоды больше 26
                set_weather = len( weather_text ) // 2 # Делит длину текста погоды на 2 без остатка
                if set_weather > 30: # Если больше 30
                    # СТИЛЬ
                    self_instance.ui.weather.setStyleSheet( f"""background: url(:/Jarvis/Night/Weather.png);
                          border: { border_size } solid { color_interface };
                          border-radius: 20px;
                          color: { color_interface };
                          font-family: 'Inter';
                          font-style: normal;
                          font-weight: 900;
                          font-size: 16px;
                          line-height: 29px;""" )
                    # СТИЛЬ
                    gui.Update_Weather( self_instance, f"{ weather_text[:set_weather] }\n{ weather_text[set_weather:] }" ) # Пишит погоду в интерфейс в раздёленном формате ( маленький текст )
                else:
                    gui.Update_Weather( self_instance, f"{ weather_text[:set_weather] }\n{ weather_text[set_weather:] }" ) # Пишит погоду в интерфейс в раздёленном формате ( нормальный текст )
            update_weather = True # Устанавливает значение, что погода написанна в интерфейс
    
    if response_.status_code != 200: # Если сайт погоды не работает
        gui.Update_Weather( self_instance, "Ошибка" ) # Пишит в интерфейс погоды слово "Ошибка"
        update_weather = False # Устанавливаем значение, что погода не написанна в интерфейс
# Функция для получения погоды и её отображения в интерфейсе

def get_now_time(): # Получение времени
    now = datetime.now() # Получение времени
    times_ = now.strftime( "%H:%M:%S" ) # Форматирует время в часы:минуты:секунды
    return times_ # Возвращает время

def get_now_minute(): # Получение времени в минутах и секундах
    now = datetime.now() # Получение времени
    times_ = now.strftime( "%M:%S" ) # Форматирует время в минуты:секунды
    return times_ # Возвращает время

def get_now_second(): # Получение времени в секундах
    now = datetime.now() # Получение времени
    times_ = now.strftime( "%S" ) # Форматирует время в секунды
    return times_ # Возвращает время

def updater_time_now(): # Функция обновления времени в интерфейсе
    global self_instance # Нужно для работы с элементами энтерфейса
    while True: # Цикл
        time.sleep( 0.1 ) # Ждёт 1 миллисикунду
        now = datetime.now() # Получает время
        time_ = now.strftime( "%H:%M:%S" ) # Форматирует время в часы:минуты:секунды

        gui.Update_Now_Time( self_instance, time_ ) # Обновляет текст времени

def cancel_shutdown(): # Функция отмены действия выключения пк
    global self_instance
    global cmd
    global user_text
    global telegram_mode

    cmd = ""

    is_running = True # Идёт действие таймера выключения пк

    for i in range( int( downing_time ), 0, -1 ): # Время выключения пк
        if telegram_mode == False:
            if user_text in ( "отмена", "отменить" ):
                print( f"{ Fore.GREEN }Действие отменено{ Fore.RESET }" )
                gui.Get_To_History( f"JARVIS SECURITY: Действие отменено", 1 )
                playsound_play( f"Jarvis Sound Pack\\What I was thinking, we usually have fun.wav" )
                gui.Get_To_History( f"Jarvis: О чем я думал, обычно у нас все веселенькое.", 1 )
                is_running = False

        if cmd != "":
            if cmd in ( "отмена", "cancel", "cancl", "canc" ):
                print( f"{ Fore.GREEN }Действие отменено{ Fore.RESET }" )
                gui.Get_To_History( f"JARVIS SECURITY: Действие отменено", 1 )
                playsound_play( f"Jarvis Sound Pack\\What I was thinking, we usually have fun.wav" )
                gui.Get_To_History( f"Jarvis: О чем я думал, обычно у нас все веселенькое.", 1 )
                is_running = False

        if telegram_mode == True:
            if cmd in ( "отмена", "cancel", "cancl", "canc" ):
                print( f"{ Fore.GREEN }Действие отменено{ Fore.RESET }" )
                gui.Get_To_History( f"JARVIS SECURITY: Действие отменено", 1 )
                playsound_play( f"Jarvis Sound Pack\\What I was thinking, we usually have fun.wav" )
                gui.Get_To_History( f"Jarvis: О чем я думал, обычно у нас все веселенькое.", 1 )
                is_running = False

        if event_command != "":
            i -= 1
            gui.Get_To_History( f"JARVIS SECURITY: Осталось { i } секунд", 1 )
            print( f"Осталось: { i } секунд" )
            time.sleep( 1 )

            if i == 1: # Если время выключения 1 секунд
                time.sleep( 1 ) # Ждёт 1 секунду
                print( "Выключение" ) # Пишит в консоль слово "Выключение"
                gui.Close_Jarvis( self_instance ) # Закрытие Джарвиса
                is_running = False # Заверение подсчёта времени
                os.system( "shutdown /h" ) # Выключает пк ( гибернация )

        if not is_running: # Если пользователь отменил выключение
            break # Остановка подсчёта времени и продолжение работы Джарвиса

def event_cancel( downin_time, event, func ): # Функция по созданию события выключения
    global event_command
    event_command = event

    print( f"Новое событие: { event } из { func }\n" ) # Пишит в консоль событие и что его вызвало

    if ( event == "shutdown_h" ): # Проверяет, что пользователь создал событие выключения 
        ev_cancel.start() # Начинает поток подсчёта времени, чтобы не тормозить основные функции Джарвиса

ev_cancel = threading.Thread( target=cancel_shutdown ) # Создание потока
ev_cancel.daemon = True # В инете нашёл, разрешает завершать

def Set_History( self, msg ): # Функция добавления истории
    self.ui.history.append( msg )

class Clear( QThread ): # Класс очищения истории, нашёл в инете, так как сам не понял
    signal = pyqtSignal( str )

    def __init__( self, parent=None ):
        super( Clear, self ).__init__( parent )

    def run( self ):
        doc = QTextDocument()
        cursor = QTextCursor( doc )

        cursor.insertText( "" )
        new_text = doc.toPlainText()

        self.signal.emit( new_text )

i = False # Тестовая перменная, но это не точно! :)

class gui( QtWidgets.QMainWindow ): # Основной класс интерфейса Джарвиса
    def __init__( self, parent=None ): # Инитилизирует интерфейс
        super().__init__( parent ) # Инитилизирует интерфейс
        # Глобальные перменные
        global self_instance
        
        global colvo_jarvis
        global colvo_setting
        global colvo_commands
        
        global jarvis_mode
        global widget_size
        global setting_mode
        global list_mode
        global addon_mode
        global save_
        # Глобальные переменные

        # Установка значений
        save_ = 1

        colvo_jarvis = 0
        colvo_setting = 0
        colvo_commands = 0

        widget_size = False

        jarvis_mode = True
        setting_mode = False
        list_mode = False
        addon_mode = False
        # Установка значений

        self.ui = Ui_Jarvis() # Берёт весь интерфейс из файлы
        self.ui.setupUi( self ) # Устанавливает интерфейс

        self_instance = self # Создал переменную для работы с интерфейсом за пределами класса

        self.ui.label.mouseMoveEvent = self.MoveWindow # Кастомное передвижение окна

        self.ui.tele.hide()

        self.ui.pushButton_2.clicked.connect( lambda: self.showMinimized() ) # Если нажат жёлтый круг, то окно сворачивается
        self.ui.pushButton.clicked.connect( self.exit_pressed ) # Закрытие программы

        # Основные функции для кнопок

        self.ui.jarvis.clicked.connect( self.info_pressed )

        self.ui.menu.clicked.connect( self.menu_pressed )
        self.ui.menu2.clicked.connect( self.menu2_pressed )

        self.ui.menu2.hide()

        self.ui.list.clicked.connect( self.list_pressed )

        # self.ui.add_programm.clicked.connect( self.add_path )
        self.ui.add_programm.hide()

        self.ui.addons.clicked.connect( self.addons_pressed )
        self.ui.addon.hide()

        self.ui.setting.clicked.connect( self.setting_pressed )
        self.ui.paths.clicked.connect( self.program_paths )
        self.ui.paths.hide()
        
        self.ui.city = self.findChild( QtWidgets.QLabel, "city" )
        self.ui.city_name.returnPressed.connect( self.on_return_pressed_city )
        self.ui.color_interface = self.findChild( QtWidgets.QLabel, "color_interface" )
        self.ui.interface_color.returnPressed.connect( self.on_return_pressed_interface_color )
        self.ui.width_border = self.findChild( QtWidgets.QLabel, "width_border" )
        self.ui.border_px.returnPressed.connect( self.on_return_pressed_border_px )
        self.ui.input_check = self.findChild( QtWidgets.QLabel, "input_check" )

        self.ui.save_settings.clicked.connect( self.save_settings_pressed )

        self.ui.city.hide()
        self.ui.city_name.hide()
        self.ui.color_interface.hide()
        self.ui.interface_color.hide()
        self.ui.width_border.hide()
        self.ui.border_px.hide()
        self.ui.input_check.hide()
        self.ui.save_settings.hide()

        self.ui.exit.clicked.connect( self.exit_pressed )

        self.ui.jarvis = self.findChild( QtWidgets.QPushButton, "jarvis" )
        self.ui.list = self.findChild( QtWidgets.QPushButton, "list" )
        self.ui.setting = self.findChild( QtWidgets.QPushButton, "setting" )

        self.ui.exit = self.findChild( QtWidgets.QPushButton, "exit" )

        self.ui.history = self.findChild( QtWidgets.QTextBrowser, "history" )
        self.ui.about = self.findChild( QtWidgets.QTextBrowser, "about" )
        self.ui.commands = self.findChild( QtWidgets.QTextBrowser, "commands" )

        self.ui.weather = self.findChild( QtWidgets.QLabel, "weather" )

        self.ui.console.returnPressed.connect( self.on_return_pressed )

        self.ui.now_time = self.findChild( QtWidgets.QLabel, "now_time" )

        self.ui.about.hide()
        self.ui.commands.hide()

        self.clear_thread = Clear( self )
        self.clear_thread.signal.connect( self.update_text_editor )

        gui.Init_Theme( self )
         
    def MoveWindow( self, event ): # Функция перемещения окна
        self.move( self.pos() + event.globalPos() - self.clickPosition )
        self.clickPosition = event.globalPos()
        event.accept()

    def mousePressEvent( self, event ): # Функция позиции мыши
        self.clickPosition = event.globalPos()

    def Init_Theme( self ): # Инит темы
        # Данные из user_config.ini
        default_color_interface = config.get( "Params", "default_color_interface" ) 
        default_border_size = config.get( "Params", "default_border_size" )
        # Данные из user_config.ini

        global color_interface

        color_interface = default_color_interface.strip( "\"\"" )

        global border_size
        border_size = default_border_size.strip( "\"\"" )

        # Устанавливаем стиль каждого объекта

        self.ui.jarvis.setStyleSheet( """font-family: 'Inter';
                                          font-style: normal;
                                          font-weight: 900;
                                          font-size: 24px;
                                          line-height: 29px;
                                          color: rgba(255,255,255,0.8);
                                          border-radius: 0px;
                                          background: rgba(0,0,0,0);""" )

        if line_border == True:
            self.ui.left_panel.setStyleSheet( f"""background: url(:/Jarvis/Night/left-panel.png);
                                                  border: { border_size } solid { color_interface };
                                                  border-top-right-radius: 60px;
                                                  border-bottom-right-radius: 60px;""" )

            self.ui.about.setStyleSheet( f"""background: url(:/Jarvis/Night/History-b.png);
                                        border: { border_size } solid { color_interface };
                                        border-radius: 15px;""" )

            self.ui.commands.setStyleSheet( f"""background: url(:/Jarvis/Night/History-b.png);
                                               border: { border_size } solid { color_interface };
                                               border-radius: 15px;
                                               color: white;""" )

            self.ui.addon.setStyleSheet( f"""background: url(:/Jarvis/Night/History-hh.png);
            border: { border_size } solid { color_interface };
            border-radius: 15px;""" )
                
            self.ui.weather.setStyleSheet( f"""background: url(:/Jarvis/Night/Weather.png);
                                              border: { border_size } solid { color_interface };
                                              border-radius: 20px;
                                              color: { color_interface };
                                              font-family: 'Inter';
                                              font-style: normal;
                                              font-weight: 900;
                                              font-size: 20px;
                                              line-height: 29px;""" )

            self.ui.now_time.setStyleSheet( f"""background: url(:/Jarvis/Night/Time.png);
                                           border: { border_size } solid { color_interface };
                                           border-radius: 20px;
                                           color: { color_interface };""" )

        if line_border == False:
            self.ui.left_panel.setStyleSheet( f"""background: url(:/Jarvis/Night/left-panel.png);
                                                  border-top-right-radius: 60px;
                                                  border-bottom-right-radius: 60px;""" )

            self.ui.about.setStyleSheet( f"""background: url(:/Jarvis/Night/History-b.png);
                                        border-radius: 15px;""" )

            self.ui.commands.setStyleSheet( f"""background: url(:/Jarvis/Night/History-b.png);
                                               border-radius: 15px;
                                               color: white;""" )

            self.ui.addon.setStyleSheet( "background: url(:/Jarvis/Night/History-hh.png);\n"
            "border-radius: 15px;" )
                
            self.ui.weather.setStyleSheet( f"""background: url(:/Jarvis/Night/Weather.png);
                                              border-radius: 20px;
                                              color: { color_interface };
                                              font-family: 'Inter';
                                              font-style: normal;
                                              font-weight: 900;
                                              font-size: 20px;
                                              line-height: 29px;""" )

            self.ui.now_time.setStyleSheet( f"""background: url(:/Jarvis/Night/Time.png);
                                           border-radius: 20px;
                                           color: { color_interface };""" )
            
        self.ui.list.setStyleSheet( """font-family: 'Inter';
                                       font-style: normal;
                                       font-weight: 900;
                                       font-size: 24px;
                                       line-height: 29px;
                                       color: rgba(255,255,255,0.8);
                                       border-radius: 0px;
                                       background: rgba(0,0,0,0);""" )

        self.ui.setting.setStyleSheet( """font-family: 'Inter';
                                          font-style: normal;
                                          font-weight: 900;
                                          font-size: 24px;
                                          line-height: 29px;
                                          color: rgba(255,255,255,0.8);
                                          border-radius: 0px;
                                          background: rgba(0,0,0,0);""" )
        if widget_size == True:
            if line_border == True:
                self.ui.history.setStyleSheet( f"""background: url(:/Jarvis/Night/History-b.png);
                                                border: { border_size } solid { color_interface };
                                                border-radius: 15px;

                                                padding: 10px;
                                                padding-top: 5px;
                                                font-family: 'Inter';
                                                font-style: normal;
                                                font-weight: 900;
                                                font-size: 20px;
                                                line-height: 29px;
                                                color: { color_interface };""" )

                self.ui.addon.setStyleSheet( f"""background: url(:/Jarvis/Night/History-hh.png);
                    border: { border_size } solid { color_interface };
                    border-radius: 15px;""" )
                    
            else:
                self.ui.history.setStyleSheet( f"""background: url(:/Jarvis/Night/History-b.png);
                                                border-radius: 15px;

                                                padding: 10px;
                                                padding-top: 5px;
                                                font-family: 'Inter';
                                                font-style: normal;
                                                font-weight: 900;
                                                font-size: 20px;
                                                line-height: 29px;
                                                color: { color_interface };""" )
                self.ui.addon.setStyleSheet( f"""background: url(:/Jarvis/Night/History-hh.png);
                    border-radius: 15px;""" )
        else:
            if line_border == True:
                self.ui.history.setStyleSheet( f"""background: url(:/Jarvis/Night/History-b.png);
                                                border: { border_size } solid { color_interface };
                                                border-radius: 15px;

                                                padding: 10px;
                                                padding-top: 5px;
                                                font-family: 'Inter';
                                                font-style: normal;
                                                font-weight: 900;
                                                font-size: 16px;
                                                line-height: 29px;
                                                color: { color_interface };""" )
            else:
                self.ui.history.setStyleSheet( f"""background: url(:/Jarvis/Night/History-b.png);
                                                border-radius: 15px;

                                                padding: 10px;
                                                padding-top: 5px;
                                                font-family: 'Inter';
                                                font-style: normal;
                                                font-weight: 900;
                                                font-size: 16px;
                                                line-height: 29px;
                                                color: { color_interface };""" )

        self.ui.console.setStyleSheet( f"""color: black;
                                           font-size: 20px;
                                           background: { color_interface };
                                           padding: 10px;
                                           border-radius: 10px;""" )

        self.ui.exit.setStyleSheet( """font-family: 'Inter';
                                       font-style: normal;
                                       font-weight: 900;
                                       font-size: 22px;
                                       line-height: 29px;
                                       color: rgba(255,255,255,0.8);
                                       border-radius: 0px;
                                       background: rgba(0,0,0,0);""" )

        self.ui.city_name.setStyleSheet( f"""color: black;
                                             font-size: 20px;
                                             background: { color_interface };
                                             padding: 10px;
                                             border-radius: 8px;
                                             font-weight: 500;""" )

        self.ui.interface_color.setStyleSheet( f"""color: black;
                                                   font-size: 20px;
                                                   background: { color_interface };
                                                   padding: 10px;
                                                   border-radius: 8px;
                                                   font-weight: 500;""" )

        self.ui.border_px.setStyleSheet( f"""color: black;
                                             font-size: 20px;
                                             background: { color_interface };
                                             padding: 10px;
                                             border-radius: 8px;
                                             font-weight: 500;""" )

        self.ui.input_check.setStyleSheet( """color: white;
                                              font-size: 20px;
                                              font-weight: 700;
                                              background: rgba(0,0,0,0);""" )

        self.ui.save_settings.setStyleSheet( f"""color: { color_interface };
                                                 background: rgba( 0,0,0,0 );
                                                 font-weight: 700;
                                                 font-size: 20px;""" )

        self.ui.paths.setStyleSheet( f"""color: { color_interface };
            background: rgba( 0,0,0,0 );
            font-weight: 700;
            font-size: 20px;
            text-align: center;""" )

        self.ui.commands.setHtml( f"<strong style=\"color: { color_interface };font-family: 'Inter';font-style: normal;font-weight: 900;font-size: 22px;line-height: 29px;\"><center>Команды</center></strong>"
                                  """<div style="margin:10px;font-family: 'Inter';font-style: normal;font-weight: 900;font-size: 22px;line-height: 29px;"><br>Открытие браузера/новой вкладки -  открой браузер, запусти браузер<br><br>
Открытие ютуба -  открой ютуб, ютубчик, ютуб, открой ютюб, ютюбчик, ютюб, включи ютуб, включи ютюб<br><br>
Включение музыки ( YandexMusic ) -  включи музыку, открой яндекс музыку, включи музон, включи музончик<br><br>
Открытие ВК -  открой вк, проверь вк, чекни вк, зайди в вк, зайди во вк, открой века, проверь века, чекни века, зайди в века, зайди во века, зайди в и к, открой языка <br><br>
Плейлист -  мой плэй лист, открой мой плейлист, открой мой плей лист, мой плейлист, включи мой плейлист, включи мою музыку, моя музыка<br><br>
Очистить историю -  очисть историю, очисти историю, освободи историю, удали историю <br><br>
Обзывания -  ты тупой, хотя ты тупой, тупой, ты идиот, идиот<br><br>
Музыка фонк -  запусти уютный вечер, запустить уютный вечер, уютный вечер, активируй уютный вечер<br><br>
Гибернация -  сохранить работу, сохрани проект и заверши работу, сохрани состояние, сохранить состояние, сохрани работу<br><br>
Действие отмены -  отмени действие, отмени последние действие, отмена<br><br>
Остановить/возообновить музыку/видео -  остановить музыку, остановить видео, останови музыку, останови видео, останови звук<br><br>
Открыть на весь экран -  открой на всё окно, открой на весь экран, разверни на весь экран<br><br>
Сворачивание окна -  сверни окно, разверни окно<br><br>
Сворачивание всех окон -  сверни окна, сверни все окна, верни все окна, верни окна, разверни все окна<br><br>
Закрытие окна -  закрой окно, закрой программу, выйди из программы<br><br>
Интернет поиск -  найди что такое, что такое<br><br>
Смена языка -  смени язык, смене язык, поменяй язык, переключи язык, переключи на другой язык<br><br>
Нажатие мышки -  нажми, выбери, выбири, тыкни<br><br>
Голосовой ввод -  напиши<br><br>
Команда для выхода - /close, /exit, /dc<br><br>
Команда для смена цвета - /color, /change_color, /colour, /interface, /theme, /themes</div>""" )

    def info_pressed( self ): # Функция нажатия кнопки
        global jarvis_mode
        global setting_mode
        global list_mode
        global addon_mode
        global colvo_jarvis
        
        jarvis_mode = True
        setting_mode = False
        list_mode = False
        addon_mode = False

        colvo_jarvis += 1

        self.ui.add_programm.hide()
        self.ui.about.hide()
        self.ui.addon.hide()

        self.ui.tele.hide()
        
        self.ui.city.hide()
        self.ui.city_name.hide()
        self.ui.color_interface.hide()
        self.ui.interface_color.hide()
        self.ui.width_border.hide()
        self.ui.border_px.hide()
        self.ui.input_check.hide()
        self.ui.save_settings.hide()
        self.ui.paths.hide()

        self.ui.commands.hide()

        self.ui.history.show()

        self.ui.console.show()
        self.ui.weather.show()
        self.ui.now_time.show()

    def menu_pressed( self ): # Функция смена размера левой панели
        global color_interface
        global widget_size

        global jarvis_mode
        global setting_mode
        global list_mode
        global addon_mode

        global border_size

        self.ui.console.show()
        self.ui.weather.show()
        self.ui.now_time.show()

        self.ui.menu.hide()
        self.ui.menu2.show()
        self.ui.menu2.setGeometry( QtCore.QRect( 130, 90, 29, 24 ) )
        self.ui.left_panel.setGeometry( QtCore.QRect( 0, 50, 290, 800 ) )

        if line_border == True:
            self.ui.left_panel.setStyleSheet( f"""background: url(:/Jarvis/Night/left-panel.png);
                                    border: { border_size } solid { color_interface };
                                    border-top-right-radius: 60px;
                                    border-bottom-right-radius: 60px;""" )

            self.ui.history.setStyleSheet( f"""background: url(:/Jarvis/Night/History-b.png);
            border: { border_size } solid { color_interface };
            border-radius: 15px;
            padding: 10px;
            padding-top: 5px;
            font-family: 'Inter';
            font-style: normal;
            font-weight: 900;
            font-size: 20px;
            line-height: 29px;
            color: { color_interface };""" )
            self.ui.about.setStyleSheet( f"""background: url(:/Jarvis/Night/History-hh.png);
                                            border: { border_size } solid { color_interface };
                                            border-radius: 15px;""" )
            self.ui.commands.setStyleSheet( f"""background: url(:/Jarvis/Night/History-hh.png);
            border: { border_size } solid { color_interface };
            border-radius: 15px;
            color: white;
            font-weight: 700;
            font-size: 20px;""" )

        if line_border == False:
            self.ui.left_panel.setStyleSheet( f"""background: url(:/Jarvis/Night/left-panel.png);
                                    border-top-right-radius: 60px;
                                    border-bottom-right-radius: 60px;""" )

            self.ui.history.setStyleSheet( f"""background: url(:/Jarvis/Night/History-b.png);
            border-radius: 15px;
            padding: 10px;
            padding-top: 5px;
            font-family: 'Inter';
            font-style: normal;
            font-weight: 900;
            font-size: 20px;
            line-height: 29px;
            color: { color_interface };""" )
            self.ui.about.setStyleSheet( f"""background: url(:/Jarvis/Night/History-hh.png);
                                            border-radius: 15px;""" )
            self.ui.commands.setStyleSheet( f"""background: url(:/Jarvis/Night/History-hh.png);
            border-radius: 15px;
            border-radius: 15px;
            color: white;
            font-weight: 700;
            font-size: 20px;""" )

        self.ui.jarvis.setGeometry( QtCore.QRect( 95, 354, 100, 29 ) )
        self.ui.setting.setGeometry( QtCore.QRect( 77, 435, 136, 29 ) )
        self.ui.list.setGeometry( QtCore.QRect( 87, 516, 117, 29 ) )

        self.ui.addons.setGeometry( QtCore.QRect( 65, 597, 161, 29 ) )

        self.ui.history.setGeometry( QtCore.QRect( 315, 70, 860, 500 ) )

        self.ui.about.setGeometry( QtCore.QRect( 315, 70, 860, 760 ) )

        self.ui.commands.setGeometry( QtCore.QRect( 315, 70, 860, 500 ) )
        self.ui.commands.setGeometry( QtCore.QRect( 315, 70, 860, 760 ) )

        self.ui.weather.setGeometry( QtCore.QRect( 315, 655, 344, 182 ) )
        self.ui.console.setGeometry( QtCore.QRect( 550, 585, 391, 51 ) )

        self.ui.city.setGeometry( QtCore.QRect( 509, 110, 101, 71 ) )
        self.ui.city_name.setGeometry( QtCore.QRect( 609, 126, 340, 41 ) )
        self.ui.color_interface.setGeometry( QtCore.QRect( 500, 160, 221, 71 ) )
        self.ui.interface_color.setGeometry( QtCore.QRect( 729, 175, 280, 41 ) )
        self.ui.width_border.setGeometry( QtCore.QRect( 509, 210, 231, 71 ) )
        self.ui.border_px.setGeometry( QtCore.QRect( 749, 225, 280, 41 ) )
        self.ui.input_check.setGeometry( QtCore.QRect( 520, 360, 511, 121 ) )
        self.ui.tele.setGeometry( QtCore.QRect( 520, 360, 511, 121 ) )
        self.ui.save_settings.setGeometry( QtCore.QRect( 690, 670, 141, 51 ) )
        self.ui.paths.move( 692, 730 )

        widget_size = True

        if widget_size == True:
            if jarvis_mode == True:
                self.ui.console.show()
                self.ui.weather.show()
                self.ui.now_time.show()

                self.ui.history.setGeometry( QtCore.QRect( 315, 70, 860, 500 ) )

            if setting_mode == True:
                self.ui.console.hide()
                self.ui.weather.hide()
                self.ui.now_time.hide()

                if line_border == True:
                    self.ui.about.setStyleSheet( f"""background: url(:/Jarvis/Night/History-hh.png);
                    border: { border_size } solid { color_interface };
                    border-top-right-radius: 60px;
                    border-bottom-right-radius: 60px;
                    border-radius: 15px;""" )
                    self.ui.about.setGeometry( QtCore.QRect( 315, 70, 860, 760 ) )
                else:
                    self.ui.about.setStyleSheet( f"""background: url(:/Jarvis/Night/History-hh.png);
                    border-top-right-radius: 60px;
                    border-bottom-right-radius: 60px;
                    border-radius: 15px;""" )
                    self.ui.about.setGeometry( QtCore.QRect( 315, 70, 860, 760 ) )

            if list_mode == True:
                self.ui.console.hide()
                self.ui.weather.hide()
                self.ui.now_time.hide()

                if line_border == True:
                    self.ui.commands.setStyleSheet( f"""background: url(:/Jarvis/Night/History-hh.png);
                    border: { border_size } solid { color_interface };
                    border-radius: 15px;
                    border-radius: 15px;
                    color: white;
                    font-weight: 700;
                    font-size: 20px;""" )
                else:
                    self.ui.commands.setStyleSheet( f"""background: url(:/Jarvis/Night/History-hh.png);
                    border-radius: 15px;
                    border-radius: 15px;
                    color: white;
                    font-weight: 700;
                    font-size: 20px;""" )

                self.ui.commands.setGeometry( QtCore.QRect( 315, 70, 860, 760 ) )

            if addon_mode == True:
                self.ui.console.hide()
                self.ui.weather.hide()
                self.ui.now_time.hide()

                self.ui.input_check.setGeometry( QtCore.QRect( 480, 360, 511, 121 ) )

                if line_border == True:
                    self.ui.addon.setStyleSheet( f"""background: url(:/Jarvis/Night/History-hh.png);
                    border: { border_size } solid { color_interface };
                    border-radius: 15px;""" )
                else:
                    self.ui.addon.setStyleSheet( f"""background: url(:/Jarvis/Night/History-hh.png);
                    border-radius: 15px;""" )
                
                self.ui.addon.setGeometry( QtCore.QRect( 315, 70, 860, 760 ) )

            if addon_mode == False:
                if line_border == True:
                    self.ui.addon.setStyleSheet( f"""background: url(:/Jarvis/Night/History-hh.png);
                    border: { border_size } solid { color_interface };
                    border-radius: 15px;""" )
                else:
                    self.ui.addon.setStyleSheet( f"""background: url(:/Jarvis/Night/History-hh.png);
                    border-radius: 15px;""" )
                
                self.ui.addon.setGeometry( QtCore.QRect( 315, 70, 860, 760 ) )

    def menu2_pressed( self ): # Функция смена размера левой панели
        global color_interface
        global widget_size

        global setting_mode
        global list_mode
        global addon_mode

        global border_size

        self.ui.menu2.hide()
        self.ui.menu.show()
        self.ui.left_panel.setGeometry( QtCore.QRect( 0, 50, 450, 800 ) )

        if line_border == True:
            self.ui.left_panel.setStyleSheet( f"""background: url(:/Jarvis/Night/left-panel.png);
                                                  border: { border_size } solid { color_interface };
                                                  border-top-right-radius: 60px;
                                                  border-bottom-right-radius: 60px;""" )

            self.ui.history.setStyleSheet( f"""background: url(:/Jarvis/Night/History.png);
            border: { border_size } solid { color_interface };
            border-radius: 15px;
            padding: 10px;
            padding-top: 5px;
            font-family: 'Inter';
            font-style: normal;
            font-weight: 900;
            font-size: 16px;
            line-height: 29px;
            color: { color_interface };""" )
            self.ui.about.setStyleSheet( f"""background: url(:/Jarvis/Night/History.png);
            border: { border_size } solid { color_interface };
            border-top-right-radius: 60px;
            border-bottom-right-radius: 60px;
            border-radius: 15px;""" )
            self.ui.commands.setStyleSheet( f"""background: url(:/Jarvis/Night/History.png);
            border: { border_size } solid { color_interface };
            border-radius: 15px;
            border-radius: 15px;
            color: white;""" )

        if line_border == False:
            self.ui.left_panel.setStyleSheet( f"""background: url(:/Jarvis/Night/left-panel.png);
                                                  border-top-right-radius: 60px;
                                                  border-bottom-right-radius: 60px;""" )

            self.ui.history.setStyleSheet( f"""background: url(:/Jarvis/Night/History.png);
            border-radius: 15px;
            padding: 10px;
            padding-top: 5px;
            font-family: 'Inter';
            font-style: normal;
            font-weight: 900;
            font-size: 16px;
            line-height: 29px;
            color: { color_interface };""" )
            self.ui.about.setStyleSheet( f"""background: url(:/Jarvis/Night/History.png);
            border-top-right-radius: 60px;
            border-bottom-right-radius: 60px;
            border-radius: 15px;""" )
            self.ui.commands.setStyleSheet( f"""background: url(:/Jarvis/Night/History.png);
            border-radius: 15px;
            border-radius: 15px;
            color: white;""" )

        self.ui.jarvis.setGeometry( QtCore.QRect( 175, 354, 100, 29 ) )
        self.ui.setting.setGeometry( QtCore.QRect( 157, 435, 136, 29 ) )
        self.ui.list.setGeometry( QtCore.QRect( 167, 516, 117, 29 ) )

        self.ui.addon.setGeometry( QtCore.QRect( 475, 70, 700, 760 ) )
        self.ui.addons.setGeometry( QtCore.QRect( 145, 597, 161, 29 ) )

        self.ui.history.setGeometry( QtCore.QRect( 475, 70, 700, 500 ) )
        self.ui.about.setGeometry( QtCore.QRect( 475, 70, 700, 500 ) )
        self.ui.commands.setGeometry( QtCore.QRect( 475, 70, 700, 500 ) )

        self.ui.weather.setGeometry( QtCore.QRect( 475, 655, 344, 182 ) )
        self.ui.console.setGeometry( QtCore.QRect( 630, 585, 391, 51 ) )

        self.ui.city.setGeometry( QtCore.QRect( 549, 110, 101, 71 ) )
        self.ui.city_name.setGeometry( QtCore.QRect( 649, 126, 340, 41 ) )
        self.ui.color_interface.setGeometry( QtCore.QRect( 540, 160, 221, 71 ) )
        self.ui.interface_color.setGeometry( QtCore.QRect( 769, 175, 280, 41 ) )
        self.ui.width_border.setGeometry( QtCore.QRect( 549, 210, 231, 71 ) )
        self.ui.border_px.setGeometry( QtCore.QRect( 779, 225, 280, 41 ) )
        self.ui.input_check.setGeometry( QtCore.QRect( 570, 300, 511, 121 ) )
        self.ui.tele.setGeometry( QtCore.QRect( 570, 360, 511, 121 ) )
        self.ui.save_settings.setGeometry( QtCore.QRect( 750, 430, 141, 51 ) )
        self.ui.paths.move( 752, 500 )

        widget_size = False

        if widget_size == False:
            if addon_mode == True:
                self.ui.console.hide()
                self.ui.weather.hide()
                self.ui.now_time.hide()
            else:
                self.ui.console.show()
                self.ui.weather.show()
                self.ui.now_time.show()

    def keyPressEvent( self, event ): # Функция обработки события нажатие enter
        global event_enter
        event_enter = False
        if ( event_enter == False ):
            if event.key() == Qt.Key_Enter: # == Qt.Key_Return or event.key()
                self.on_return_pressed()
                event_enter = True

    def on_return_pressed( self ): # Функция проверки прописных команд
        global cmd

        cmd = self.ui.console.text() # Получение введённого текста

        if ( cmd == "/clear" or cmd == "cls" or cmd == "clear" ):
            gui.Clear_History( self )

        if ( cmd in exit_jarvis ):
            global my_thread
            global thread_time
            playsound_play( f"sound\\thanks.wav" )
            time.sleep( 0.4 )
            QtWidgets.QApplication.closeAllWindows()
            time.sleep( 0.4 )

        if cmd == "InitTheme" or cmd == "inittheme" or cmd == "ThemeInit":
            gui.Init_Theme( self_instance )
        
        if ( cmd in open_brouser ):
            playsound_play( f"sound\\ok2.wav" )
            gui.Get_To_History( "Jarvis: Загружаю, сэр!", 1 )
            webbrowser.get().open_new_tab( "https://www.yandex.ru/" )

        if ( cmd in open_youtube ):
            playsound_play( f"sound\\ok2.wav" )
            gui.Get_To_History( "Jarvis: Загружаю, сэр!", 1 )
            webbrowser.get().open_new_tab( "https://youtube.com/" )

        if ( cmd in open_music ):
            playsound_play( f"sound\\ok2.wav" )
            gui.Get_To_History( "Jarvis: Загружаю, сэр!", 1 )
            webbrowser.get().open_new_tab( "https://music.yandex.ru/home/" )

        if ( cmd in open_vk ):
            playsound_play( f"sound\\ok2.wav" )
            gui.Get_To_History( "Jarvis: Загружаю, сэр!", 1 )
            webbrowser.get().open_new_tab( "https://vk.com/feed/" )

        if ( cmd == "выход" ):
            QtWidgets.QApplication.closeAllWindows()
            playsound_play( f"sound\\thanks.wav" )

        if ( cmd in clear_history ):
            gui.Clear_History( self_instance )

        if ( cmd in jarvis_stupid ):
            playsound_play( f"sound\\stupid.wav" )
            gui.Get_To_History( "Jarvis: Очень тонкое замечание, сэр!", 1 )

        if ( cmd in super_mode_night ):
            global video_yt
            music = "music" + str( randomazer( 1, 8 ) )
            open_music_yt = globals()[ music ]

            video_yt = "https://www.youtube.com/watch?v="

            video_yt += open_music_yt
            playsound_play( f"sound\\ok3.wav" )
            gui.Get_To_History( "Jarvis: Запрос выполнин, сэр!", 1 )
            webbrowser.get().open_new_tab( video_yt )

        if ( cmd in super_mode_programming ):
            playsound_play( f"Jarvis Sound Pack\\Me working at project ser.wav" )
            gui.Get_To_History( "Jarvis: Мы работаем над проектом сэр?", 1 )

        if ( cmd in sound_stop ):
            playsound_play( f"sound\\ok3.wav" )
            gui.Get_To_History( "Jarvis: Запрос выполнин сэр.", 1 )
            pyautogui.press( "playpause" )

        # ONE OPEN

        # SHUTDOWN

        if ( cmd in shutdown_h ):
            playsound_play( f"Jarvis Sound Pack\\Nezamechen.wav" )
            gui.Get_To_History( "Jarvis: Да, это поможет вам оставаться незамеченным", 1 )
            event_cancel( downing_time, "shutdown_h", cmd )

        if ( cmd in cancel_event ):
            msg = "отмена"
            event_cancel( downing_time, "", msg )

        # SHUTDOWN

        if ( cmd in open_my_playlist ):
                playsound_play( f"sound\\ok2.wav" )
                gui.Get_To_History( "Jarvis: Загружаю, сэр!", 1 )
                webbrowser.get().open_new_tab( f"{ user_playlist }" )

        if cmd != "":
            if ( cmd == "/colors" ):
                gui.Get_To_History( "#ffd700 - Золотой ( gold )\n""#e600e6 - Пурпурный ( purple )\n"
                                    "#00FFD1 - Дефолт ( default )\n""#1476ff - Кабальтовый ( kabal )\n"
                "#4794ff - Светло Кабальтовый ( light kabal )\n""#7DF9FF - Electric Blue ( electric blue )\n"
                "#ff1493 - Deep Pink ( deep pink )\n""#e30b5d - Raspberry ( raspberry )\n""#00ff00 - Lime ( lime )\n"
                "#FF5733 - Shades of Pink ( shades pink )\n""#FF00FF - Fuchsia ( fuchsia )\n"
                "#F2D16B - Golden Sand ( golden sand )\n""#E2F55D - Honeysuckle ( honey, honeysuckle )\n"
                "#F87954 - Coral ( coral )\n""#A164F8 - Medium Purple ( medium purple )\n"
                "#FD8A12 - Dark Orange ( dark orange )\n""#9242E1 - Cool Night ( cl night )\n"
                "#00FFB7 - Light Lime ( lg lime )", 1 )

        if cmd.startswith( change_color ):
            for word in change_color:
                if word in cmd:
                    parts = cmd.split( word, 1 )
                    global user_text
                    user_text = parts[ 1 ]
                    user_text = user_text.strip( " " )
            
            CHANGE_COLOR = False
            # user_text = user_text.replace( "s", "" )
            print( user_text )
            if ( user_text == "gold" ):
                CHANGE_COLOR = True
                config.set( "Params", "default_color_interface", "#ffd700" )
                gui.Init_Theme( self_instance )

            if ( user_text == "purple" ):
                CHANGE_COLOR = True
                config.set( "Params", "default_color_interface", "#e600e6" )
                gui.Init_Theme( self_instance )

            if ( user_text == "default" ):
                CHANGE_COLOR = True
                config.set( "Params", "default_color_interface", "#00FFD1" )
                gui.Init_Theme( self_instance )

            if ( user_text == "kabal" ):
                CHANGE_COLOR = True
                config.set( "Params", "default_color_interface", "#1476ff" )
                gui.Init_Theme( self_instance )

            if ( user_text == "light kabal" ):
                CHANGE_COLOR = True
                config.set( "Params", "default_color_interface", "#4794ff" )
                gui.Init_Theme( self_instance )

            if ( user_text == "electric blue" ):
                CHANGE_COLOR = True
                config.set( "Params", "default_color_interface", "#7DF9FF" )
                gui.Init_Theme( self_instance )

            if ( user_text == "deep pink" ):
                CHANGE_COLOR = True
                config.set( "Params", "default_color_interface", "#ff1493" )
                gui.Init_Theme( self_instance )

            if ( user_text == "raspberry" ):
                CHANGE_COLOR = True
                config.set( "Params", "default_color_interface", "#e30b5d" )
                gui.Init_Theme( self_instance )

            if ( user_text == "lime" ):
                CHANGE_COLOR = True
                config.set( "Params", "default_color_interface", "#00ff00" )
                gui.Init_Theme( self_instance )

            if ( user_text == "shades pink" ):
                CHANGE_COLOR = True
                config.set( "Params", "default_color_interface", "#FF5733" )
                gui.Init_Theme( self_instance )

            if ( user_text == "fuchsia" ):
                CHANGE_COLOR = True
                config.set( "Params", "default_color_interface", "#FF00FF" )
                gui.Init_Theme( self_instance )

            if ( user_text == "golden sand" ):
                CHANGE_COLOR = True
                config.set( "Params", "default_color_interface", "#F2D16B" )
                gui.Init_Theme( self_instance )

            if ( user_text == "honey" or user_text == "honeysuckle" ):
                CHANGE_COLOR = True
                config.set( "Params", "default_color_interface", "#E2F55D" )
                gui.Init_Theme( self_instance )

            if ( user_text == "coral" ):
                CHANGE_COLOR = True
                config.set( "Params", "default_color_interface", "#F87954" )
                gui.Init_Theme( self_instance )

            if ( user_text == "medium purple" ):
                CHANGE_COLOR = True
                config.set( "Params", "default_color_interface", "#A164F8" )
                gui.Init_Theme( self_instance )

            if ( user_text == "dark orange" ):
                CHANGE_COLOR = True
                config.set( "Params", "default_color_interface", "#FD8A12" )
                gui.Init_Theme( self_instance )

            if ( user_text == "cl night" ):
                CHANGE_COLOR = True
                config.set( "Params", "default_color_interface", "#9242E1" )
                gui.Init_Theme( self_instance )

            if ( user_text == "lg lime" ):
                CHANGE_COLOR = True
                config.set( "Params", "default_color_interface", "#00FFB7" )
                gui.Init_Theme( self_instance )

            if ( "#" in user_text ):
                html_hex = user_text.strip( "#" )
                config.set( "Params", "default_color_interface", f"#{ html_hex }" )
                gui.Init_Theme( self_instance )

            if ( "#" not in user_text ): # and user_text != "s"
                if ( CHANGE_COLOR == False ): 
                    gui.Get_To_History( f"Нет такого цвета \"{ user_text }\", попробуйте ввести цвет через #, например #00ff00", 1 )

            with open( "user_config.ini", "w" ) as fl:
                config.write( fl )

        if cmd.isdigit(): # isdigit - текст является числом, а не словом
            try:
                number = cmd
                number_str = num2words( number, lang="ru" )
                print( f"Ваше число { cmd } в прописи: { number_str }" )
            except KeyError:
                print( "Вы ввели слишком большое число" )

        if cmd in switch_language:
            playsound_play( f"sound\\ok1.wav" )
            gui.Get_To_History( "Jarvis: Есть!", 1 )
            pyautogui.keyDown( "altleft" )
            pyautogui.keyDown( "shift" )
            pyautogui.keyUp( "altleft" )
            pyautogui.keyUp( "shift" )

        if cmd in sub_enter:
            playsound_play( f"sound\\ok1.wav" )
            gui.Get_To_History( "Jarvis: Есть!", 1 )
            pyautogui.click()

        # if input_enter in cmd:
        #     entered = cmd.replace( input_enter, "" )
        #     entered = entered.replace( " ", "" )
        #     pyautogui.typewrite( entered )
        #     print( entered )

        if cmd.startswith( internet_search ):
            for word in internet_search:
                if word in cmd:
                    parts = cmd.split( word, 1 )
                    global wh_search
                    wh_search = parts[ 1 ]
                    wh_search = wh_search.strip( " " )

            gui.Get_To_History( f"Ищу: \"{ word } { wh_search }\"", 1 )
            res_search = f"{ word } { wh_search }"
            res_search = res_search.replace( " ", "+" )
            webbrowser.open_new_tab( f"yandex.ru/search/?clid=2456107&text={ res_search }&l10n=ru&lr=10732" )

        # def open_program( program_name ):
        #     try:
        #         reg_key = winreg.OpenKey( winreg.HKEY_LOCAL_MACHINE, f"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths\\{ program_name }.exe" )
        #         program_path = winreg.QueryValue( reg_key, None )
        #         gui.Get_To_History( program_path, 1 )
        #         subprocess.Popen( program_path )
        #     except FileNotFoundError:
        #         print( f"Программы { program_name } нет." )
        #     except OSError as e:
        #         print( f"Ошибка: { e }" )

        # # Пример использования
        # open_program( "chrome" )

        if cmd in open_steam:
            gui.Get_To_History( "Открываю Steam", 1 )
            subprocess.Popen( f"C:\\Program Files (x86)\\Steam\\steam.exe" )

        if cmd in open_chrome:
            def open_program( program_name ):
                try:
                    reg_key = winreg.OpenKey( winreg.HKEY_LOCAL_MACHINE, f"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths\\{ program_name }.exe" )
                    program_path = winreg.QueryValue( reg_key, None )
                    gui.Get_To_History( "Открываю Chrome", 1 )
                    subprocess.Popen( program_path )
                except FileNotFoundError:
                    gui.Get_To_History( f"Программы { program_name } нет.", 1 )
                except OSError as e:
                    print( f"Ошибка: { e }" )

            open_program( "chrome" )

        if cmd in open_explorer:
            pyautogui.keyDown( "win" )
            pyautogui.keyDown( "e" )
            pyautogui.keyUp( "win" )
            pyautogui.keyUp( "e" )
        
        self.ui.console.setText( "" )

    def Update_Weather( self, weath ): # Добавляет текст погоды
        self.ui.weather.setText( weath )

    def Update_Now_Time( self, time ): # Обновление текущего времени
        self.ui.now_time.setText( time )

    def update_text_editor( self, new_text ): 
        self.ui.history.setPlainText( new_text )

    def Clear_History( self ): # Функция очистки истории запросов
        self.clear_thread.start()

    def Get_To_History( msg, who ): # Функция добавления запросов в историю
        if ( who == 1 ):
            default_color_interface = config.get( "Params", "default_color_interface" )
            color = default_color_interface.strip( "\"\"" )
            self_instance.ui.history.setTextColor( QColor( f"{ color }" ) )
            Set_History( self_instance, f"[{ get_now_time() }] { msg }" )
        else:
            self_instance.ui.history.setTextColor(QColor(253, 245, 255))
            Set_History( self_instance, f"[{ get_now_time() }] { msg }" )

    def Close_Jarvis( self ): # Функция закрытия Джарвиса
        self.close()

    def list_pressed( self ):
        global jarvis_mode
        global setting_mode
        global list_mode
        global addon_mode
        global colvo_jarvis
        
        jarvis_mode = False
        setting_mode = False
        list_mode = True
        addon_mode = False

        if widget_size == True:
            self.ui.history.hide()
            self.ui.add_programm.hide()
            self.ui.about.hide()
            self.ui.addon.hide()

            self.ui.console.hide()
            self.ui.weather.hide()
            self.ui.now_time.hide()

            self.ui.tele.hide()

            self.ui.city.hide()
            self.ui.city_name.hide()
            self.ui.color_interface.hide()
            self.ui.interface_color.hide()
            self.ui.width_border.hide()
            self.ui.border_px.hide()
            self.ui.input_check.hide()
            self.ui.save_settings.hide()

            self.ui.paths.hide()

            self.ui.commands.show()

        if widget_size == False:
            self.ui.history.hide()
            self.ui.about.hide()
            self.ui.add_programm.hide()
            self.ui.addon.hide()

            self.ui.console.show()
            self.ui.weather.show()
            self.ui.now_time.show()

            self.ui.tele.hide()

            self.ui.city.hide()
            self.ui.city_name.hide()
            self.ui.color_interface.hide()
            self.ui.interface_color.hide()
            self.ui.width_border.hide()
            self.ui.border_px.hide()
            self.ui.input_check.hide()
            self.ui.save_settings.hide()

            self.ui.paths.hide()

            self.ui.commands.show()

    def addons_pressed( self ):
        global jarvis_mode
        global setting_mode
        global list_mode
        global addon_mode

        jarvis_mode = False
        setting_mode = False
        list_mode = False
        addon_mode = True

        self.ui.history.hide()
        self.ui.about.hide()

        self.ui.console.hide()
        self.ui.weather.hide()
        self.ui.now_time.hide()

        self.ui.city.hide()
        self.ui.city_name.hide()
        self.ui.color_interface.hide()
        self.ui.interface_color.hide()
        self.ui.width_border.hide()
        self.ui.border_px.hide()
        self.ui.save_settings.hide()

        self.ui.commands.hide()

        self.ui.tele.show()
        self.ui.addon.show()

    def setting_pressed( self ):
        global save_
        global jarvis_mode
        global setting_mode
        global list_mode
        global addon_mode

        save_ = 1

        jarvis_mode = False
        setting_mode = True
        list_mode = False
        addon_mode = False

        self.ui.input_check.setText( "" )

        if widget_size == True:
            self.ui.history.hide()
            self.ui.commands.hide()
            self.ui.add_programm.hide()
            self.ui.addon.hide()

            self.ui.console.hide()
            self.ui.weather.hide()
            self.ui.now_time.hide()
            
            self.ui.interface_color.show()
            self.ui.tele.hide()

            self.ui.city.show()
            self.ui.city_name.show()
            self.ui.color_interface.show()
            self.ui.width_border.show()
            self.ui.border_px.show()
            self.ui.input_check.show()
            self.ui.save_settings.show()

            self.ui.about.show()
            self.ui.paths.show()

            self.ui.history.hide()
            self.ui.commands.hide()

        if widget_size == False:
            self.ui.history.hide()
            self.ui.commands.hide()
            self.ui.add_programm.hide()
            self.ui.addon.hide()

            self.ui.console.show()
            self.ui.weather.show()
            self.ui.now_time.show()

            self.ui.about.show()
            self.ui.paths.show()
            
            self.ui.interface_color.show()
            self.ui.tele.hide()

            self.ui.city.show()
            self.ui.city_name.show()
            self.ui.color_interface.show()
            self.ui.width_border.show()
            self.ui.border_px.show()
            self.ui.input_check.show()
            self.ui.save_settings.show()

    def on_return_pressed_city( self ):
        global cmd_city_name

        cmd_city_name = self.ui.city_name.text()
        print( cmd_city_name )

    def on_return_pressed_interface_color( self ):
        global cmd_interface_color

        cmd_interface_color = self.ui.interface_color.text()
        print( cmd_interface_color )

    def on_return_pressed_border_px( self ):
        global cmd_border_px

        cmd_border_px = self.ui.border_px.text()
        print( cmd_border_px )

    def add_path( self ):
        print( "add_PTH" )
        
    def save_settings_pressed( self ):
        global save_
        global cmd_city_name
        global cmd_interface_color
        global cmd_border_px

        if save_ == 1:
            you_city_ = config.get( "Params", "you_city" )
            default_color_interface_ = config.get( "Params", "default_color_interface" )
            default_border_size_ = config.get( "Params", "default_border_size" )

            city_name = self.ui.city_name.text()
            interface_color = self.ui.interface_color.text()
            border_px = self.ui.border_px.text()

            if city_name == "":
                self.ui.input_check.setText( "Вы не написали свой город." )

            if interface_color == "":
                self.ui.input_check.setText( "Вы не написали цвет интерфейса." )

            if border_px == "":
                self.ui.input_check.setText( "Вы не написали ширину барьеров." )

            if ( city_name != "" and interface_color != "" and border_px != "" ):
                self.ui.input_check.setText( "" )
                print( f"\n{ self.ui.city_name.text() }\n"f"{ self.ui.interface_color.text() }\n"
                    f"{ self.ui.border_px.text() }\n" )
                config.set( "Params", "you_city", f"\"{ city_name }\"" )
                config.set( "Params", "default_color_interface", f"\"{ interface_color }\"" )
                config.set( "Params", "default_border_size", f"\"{ border_px }\"" )

                with open( "user_config.ini", "w" ) as fl:
                    config.write( fl )
                    self.ui.input_check.setText( "Перезагрузите Jarvis,\nчтобы применить изменения." )

        if save_ == 2:
            pass

    def program_paths( self ):
        global save_
        save_ = 2

        self.ui.interface_color.hide()
        self.ui.city.hide()
        self.ui.city_name.hide()
        self.ui.color_interface.hide()
        self.ui.width_border.hide()
        self.ui.border_px.hide()
        self.ui.input_check.hide()
        # self.ui.save_settings.hide()

        self.ui.add_programm.show()
 
    def exit_pressed( self ):
        playsound_play( f"sound\\thanks.wav" )
        time.sleep( 0.4 )
        QtWidgets.QApplication.closeAllWindows()
        time.sleep( 0.4 )

def MainREC():
    model = Model( "vosk-model" )
    recognizer = KaldiRecognizer( model, 16000 )

    global user_programs_list
    user_programs_list = []

    global stream
    mic = pyaudio.PyAudio()
    stream = mic.open( format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer = 8192 ) # 8000
    stream.start_stream()

    for program, value in programs:
        # print( program, value )
        user_programs_list.append( [ program, value ] )

    # print( user_programs_list )

    for p, pth in user_programs_list:
        p = p.replace( "_", " " )
        print( p )
        # print( pth )

    global STARTED
    global JARVIS
    if ( STARTED == True ):
        num = randomazer( 0, 1 )
        # print( num )
        if ( num == 1 ):
            playsound_play( f"sound\\run.wav" )
            gui.Get_To_History( "Jarvis: Доброе утро!", 1 )
        else:
            playsound_play( f"Jarvis Sound Pack\\Me connected and ready.wav" )
            gui.Get_To_History( "Jarvis: Мы подключены и готовы.", 1 )
        # print( "Jarvis started" )
        STARTED = False
        JARVIS = False

    if ( JARVIS == False ):
        pass

    def commands( msg ):
        if ( msg != "" ):
            global more_msg
            more_msg = msg.split()

            print( msg )

            gui.Get_To_History( f"Вы: { msg }", 2 )

            # ONE OPEN

            if ( msg in open_brouser ):
                playsound_play( f"sound\\ok2.wav" )
                gui.Get_To_History( "Jarvis: Загружаю, сэр!", 1 )
                webbrowser.get().open_new_tab( "https://www.yandex.ru/" )

            if ( msg in open_youtube ):
                playsound_play( f"sound\\ok2.wav" )
                gui.Get_To_History( "Jarvis: Загружаю, сэр!", 1 )
                webbrowser.get().open_new_tab( "https://youtube.com/" )

            if ( msg in open_music ):
                playsound_play( f"sound\\ok2.wav" )
                gui.Get_To_History( "Jarvis: Загружаю, сэр!", 1 )
                webbrowser.get().open_new_tab( "https://music.yandex.ru/home/" )

            if ( msg in open_vk ):
                playsound_play( f"sound\\ok2.wav" )
                gui.Get_To_History( "Jarvis: Загружаю, сэр!", 1 )
                webbrowser.get().open_new_tab( "https://vk.com/feed/" )

            if ( msg == "выход" ):
                playsound_play( f"sound\\thanks.wav" )
                gui.Close_Jarvis( self_instance )
                time.sleep( 2 )
                my_thread.join()

            if ( msg in clear_history ):
                gui.Clear_History( self_instance )

            if ( msg in jarvis_stupid ):
                playsound_play( f"sound\\stupid.wav" )
                gui.Get_To_History( "Jarvis: Очень тонкое замечание, сэр!", 1 )

            if ( msg in super_mode_night ):
                global video_yt
                music = "music" + str( randomazer( 1, 8 ) )
                open_music_yt = globals()[ music ]

                video_yt = "https://www.youtube.com/watch?v="

                video_yt += open_music_yt
                playsound_play( f"sound\\ok3.wav" )
                gui.Get_To_History( "Jarvis: Запрос выполнин, сэр!", 1 )
                webbrowser.get().open_new_tab( video_yt )

            if ( msg in super_mode_programming ):
                playsound_play( f"Jarvis Sound Pack\\Me working at project ser.wav" )
                gui.Get_To_History( "Jarvis: Мы работаем над проектом сэр?", 1 )

            # ONE OPEN

            # MORE OPEN

            if ( "открой" in more_msg and "браузер" in more_msg and "ютуб" in more_msg or "открой" in more_msg and "ютуб" in more_msg and "браузер" in more_msg ):
                # открой браузер ютуб
                more_msg = ""
                playsound_play( f"sound\\ok2.wav" )
                gui.Get_To_History( "Jarvis: Загружаю, сэр!", 1 )
                webbrowser.get().open_new_tab( "https://www.yandex.ru/" )
                webbrowser.get().open_new_tab( "https://youtube.com/" )

            if ( "открой" in more_msg and "браузер" in more_msg and "ютюб" in more_msg or "открой" in more_msg and "ютюб" in more_msg and "браузер" in more_msg ):
                # открой браузер ютуб
                more_msg = ""
                playsound_play( f"sound\\ok2.wav" )
                gui.Get_To_History( "Jarvis: Загружаю, сэр!", 1 )
                webbrowser.get().open_new_tab( "https://www.yandex.ru/" )
                webbrowser.get().open_new_tab( "https://youtube.com/" )

            if ( "включи" in more_msg and "музыку" in more_msg and "ютуб" in more_msg or "включи" in more_msg and "ютуб" in more_msg and "музыку" in more_msg ):
                more_msg = ""
                playsound_play( f"sound\\ok2.wav" )
                gui.Get_To_History( "Jarvis: Загружаю, сэр!", 1 )
                webbrowser.get().open_new_tab( "https://youtube.com/" )
                webbrowser.get().open_new_tab( "https://music.yandex.ru/home/" )

            if ( "включи" in more_msg and "музыку" in more_msg and "ютюб" in more_msg or "включи" in more_msg and "ютюб" in more_msg and "музыку" in more_msg ):
                more_msg = ""
                playsound_play( f"sound\\ok2.wav" )
                gui.Get_To_History( "Jarvis: Загружаю, сэр!", 1 )
                webbrowser.get().open_new_tab( "https://youtube.com/" )
                webbrowser.get().open_new_tab( "https://music.yandex.ru/home/" )

            # MORE OPEN

            # SHUTDOWN

            if ( msg in shutdown_h ):
                playsound_play( f"Jarvis Sound Pack\\Nezamechen.wav" )
                gui.Get_To_History( "Jarvis: Да, это поможет вам оставаться незамеченным.", 1 )
                event_cancel( downing_time, "shutdown_h", msg )

            if ( msg in cancel_event ):
                event_cancel( downing_time, "", msg )

            # SHUTDOWN

            if ( msg in sound_stop ):
                playsound_play( f"sound\\ok3.wav" )
                gui.Get_To_History( "Jarvis: Запрос выполнин сэр.", 1 )
                pyautogui.press( "playpause" )

            if ( msg in open_full_window ):
                playsound_play( f"sound\\ok1.wav" )
                gui.Get_To_History( "Jarvis: Есть!", 1 )
                pyautogui.hotkey( "win" , "up" )

            if ( msg in swirt_window ):
                playsound_play( f"sound\\ok1.wav" )
                gui.Get_To_History( "Jarvis: Есть!", 1 )
                pyautogui.hotkey( "win" , "down" )

            if ( msg in swirt_windows ):
                playsound_play( f"sound\\ok1.wav" )
                gui.Get_To_History( "Jarvis: Есть!", 1 )
                pyautogui.hotkey( "win" , "d" )

            if ( msg in close_window ):
                playsound_play( f"sound\\ok1.wav" )
                gui.Get_To_History( "Jarvis: Есть!", 1 )
                pyautogui.hotkey( "alt" , "F4" )

            if ( msg in open_my_playlist ):
                playsound_play( f"sound\\ok2.wav" )
                gui.Get_To_History( "Jarvis: Загружаю, сэр!", 1 )
                webbrowser.get().open_new_tab( f"{ user_playlist }" )

            if msg in switch_language:
                playsound_play( f"sound\\ok1.wav" )
                gui.Get_To_History( "Jarvis: Есть!", 1 )
                pyautogui.keyDown( "altleft" )
                pyautogui.keyDown( "shift" )
                pyautogui.keyUp( "altleft" )
                pyautogui.keyUp( "shift" )

            if msg in sub_enter:
                playsound_play( f"sound\\ok1.wav" )
                gui.Get_To_History( "Jarvis: Есть!", 1 )
                pyautogui.click()

            # if input_enter in msg:
            #     # entered = msg.replace( input_enter, "" )
            #     # entered = entered.replace( " ", "" )
            #     # print( f"Пишу:{ entered }" )
            #     # pyautogui.typewrite( msg )
            #     # print( len( msg ) )
            #     pyautogui.typewrite( "привет" )

            if msg.startswith( internet_search ):
                for word in internet_search:
                    if word in msg:
                        parts = msg.split( word, 1 )
                        # global wh_search
                        wh_search = parts[ 1 ]
                        wh_search = wh_search.strip( " " )

                # print( f"Ищу:\"{ word } { wh_search }\"" )
                gui.Get_To_History( f"Ищу: \"{ word } { wh_search }\"", 1 )
                res_search = f"{ wh_search }"
                res_search = res_search.replace( " ", "+" )
                webbrowser.open_new_tab( f"yandex.ru/search/?clid=2456107&text={ res_search }&l10n=ru&lr=10732" )

            # if msg in open_steam:
            #     def open_program( program_name ):
            #         try:
            #             program_path = os.environ.get( program_name )
            #             if program_path:
            #                 # subprocess.Popen( program_path )
            #                 print( program_path )
            #             else:
            #                 print( f"Не удалось найти программу: { program_name }" )
            #         except OSError as e:
            #             print( f"Ошибка: { e }" )

            #     # Пример использования
            #     open_program( "chrome" )

            if msg in open_steam:
                gui.Get_To_History( "Открываю Steam", 1 )
                subprocess.Popen( f"C:\\Program Files (x86)\\Steam\\steam.exe" )

            if msg in open_chrome:
                def open_program( program_name ):
                    try:
                        reg_key = winreg.OpenKey( winreg.HKEY_LOCAL_MACHINE, f"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths\\{ program_name }.exe" )
                        program_path = winreg.QueryValue( reg_key, None )
                        gui.Get_To_History( "Открываю Chrome", 1 )
                        subprocess.Popen( program_path )
                    except FileNotFoundError:
                        gui.Get_To_History( f"Программы { program_name } нет.", 1 )
                    except OSError as e:
                        print( f"Ошибка: { e }" )

                open_program( "chrome" )

            if msg in open_explorer:
                pyautogui.keyDown( "win" )
                pyautogui.keyDown( "e" )
                pyautogui.keyUp( "win" )
                pyautogui.keyUp( "e" )

    def stt( voice ):
        global user_text
        user_text = voice

        commands( voice )
    
    check_voice = True

    while True:
        data = stream.read( 4096, exception_on_overflow=False )

        if check_voice == True:
            if ( recognizer.AcceptWaveform( data ) ):
                text = recognizer.Result()

                if text[14:-3] != "":
                    print( f"\nВы сказали: { text[14:-3] } " )
                    if text[14:-3] in activate_names:
                        gui.Get_To_History( "Вы: Jarvis.", 2 )
                        say_ser = randint( 1, 3 )
                        playsound_play( f"sound\\greet{ say_ser }.wav" )

                        if ( say_ser == 2 ):
                            gui.Get_To_History( "Jarvis: К вашим услугам, сэр!", 1 )
                        else:
                            gui.Get_To_History( "Jarvis: Да, сэр!", 1 )

                        check_voice = False

        if check_voice == False:
            if ( recognizer.AcceptWaveform( data ) ):
                text = recognizer.Result()
                stt( text[14:-3] )
                # check_voice = True

def control( message ):
    def save():
        with open( "user_config.ini", "w" ) as fl:
            config.write( fl )

    global bot
    global self_instance

    cmd = message.text.lower()
    # cmd = message.text
    print( f"Telgram command: { cmd }" )

    if ( cmd == "/clear" or cmd == "cls" or cmd == "clear" ):
            gui.Clear_History( self_instance )
    
    if ( cmd in open_brouser ):
        playsound_play( f"sound\\ok2.wav" )
        gui.Get_To_History( "Jarvis: Загружаю, сэр!", 1 )
        webbrowser.get().open_new_tab( "https://www.yandex.ru/" )

    if ( cmd in open_youtube ):
        playsound_play( f"sound\\ok2.wav" )
        gui.Get_To_History( "Jarvis: Загружаю, сэр!", 1 )
        webbrowser.get().open_new_tab( "https://youtube.com/" )

    if ( cmd in open_music ):
        playsound_play( f"sound\\ok2.wav" )
        gui.Get_To_History( "Jarvis: Загружаю, сэр!", 1 )
        webbrowser.get().open_new_tab( "https://music.yandex.ru/home/" )

    if ( cmd in open_vk ):
        playsound_play( f"sound\\ok2.wav" )
        gui.Get_To_History( "Jarvis: Загружаю, сэр!", 1 )
        webbrowser.get().open_new_tab( "https://vk.com/feed/" )

    if ( cmd in clear_history ):
        # global self_instance
        gui.Clear_History( self_instance )

    if ( cmd in jarvis_stupid ):
        playsound_play( f"sound\\stupid.wav" )
        gui.Get_To_History( "Jarvis: Очень тонкое замечание, сэр!", 1 )

    if ( cmd in super_mode_night ):
        global video_yt
        music = "music" + str( randomazer( 1, 8 ) )
        open_music_yt = globals()[ music ]

        video_yt = "https://www.youtube.com/watch?v="

        video_yt += open_music_yt
        playsound_play( f"sound\\ok3.wav" )
        gui.Get_To_History( "Jarvis: Запрос выполнин, сэр!", 1 )
        webbrowser.get().open_new_tab( video_yt )

    if ( cmd in super_mode_programming ):
        playsound_play( f"Jarvis Sound Pack\\Me working at project ser.wav" )
        gui.Get_To_History( "Jarvis: Мы работаем над проектом сэр?", 1 )

    if ( cmd in sound_stop ):
        playsound_play( f"sound\\ok3.wav" )
        gui.Get_To_History( "Jarvis: Запрос выполнин сэр.", 1 )
        pyautogui.press( "playpause" )

    # ONE OPEN

    # SHUTDOWN

    if ( cmd in shutdown_h ):
        playsound_play( f"Jarvis Sound Pack\\Nezamechen.wav" )
        gui.Get_To_History( "Jarvis: Да, это поможет вам оставаться незамеченным", 1 )
        global telegram_mode
        telegram_mode = True
        event_cancel( downing_time, "shutdown_h", cmd )

    if ( cmd in cancel_event ):
        msg = "отмена"
        event_cancel( downing_time, "", msg )

    # SHUTDOWN

    if ( cmd in open_my_playlist ):
            playsound_play( f"sound\\ok2.wav" )
            gui.Get_To_History( "Jarvis: Загружаю, сэр!", 1 )
            webbrowser.get().open_new_tab( f"{ user_playlist }" )

    if ( cmd == "/colors" ):
        bot.send_message( message.chat.id, "#ffd700 - Золотой ( gold )\n""#e600e6 - Пурпурный ( purple )\n"
            "#00FFD1 - Дефолт ( default )\n""#1476ff - Кабальтовый ( kabal )\n"
            "#4794ff - Светло Кабальтовый ( light kabal )\n""#7DF9FF - Electric Blue ( electric blue )\n"
            "#ff1493 - Deep Pink ( deep pink )\n""#e30b5d - Raspberry ( raspberry )\n""#00ff00 - Lime ( lime )\n"
            "#FF5733 - Shades of Pink ( shades pink )\n""#FF00FF - Fuchsia ( fuchsia )\n"
            "#F2D16B - Golden Sand ( golden sand )\n""#E2F55D - Honeysuckle ( honey, honeysuckle )\n"
            "#F87954 - Coral ( coral )\n""#A164F8 - Medium Purple ( medium purple )\n"
            "#FD8A12 - Dark Orange ( dark orange )\n""#9242E1 - Cool Night ( cl night )\n"
            "#00FFB7 - Light Lime ( lg lime )" )

    if cmd.startswith( change_color ):
        for word in change_color:
            if word in cmd:
                global ch_color_tele
                parts = cmd.split( word, 1 )
                ch_color_tele = parts[ 1 ]
                ch_color_tele = ch_color_tele.strip( " " )

        # ch_color_tele = ch_color_tele.replace( "s", "" )
        print( len( ch_color_tele ) )
        print( ch_color_tele )

        if ( ch_color_tele == "gold" ):
            config.set( "Params", "default_color_interface", "#ffd700" )

        if ( ch_color_tele == "purple" ):
            config.set( "Params", "default_color_interface", "#e600e6" )

        if ( ch_color_tele == "default" ):
            config.set( "Params", "default_color_interface", "#00FFD1" )

        if ( ch_color_tele == "kabal" ):
            config.set( "Params", "default_color_interface", "#1476ff" )

        if ( ch_color_tele == "light kabal" ):
            config.set( "Params", "default_color_interface", "#4794ff" )

        if ( ch_color_tele == "electric blue" ):
            config.set( "Params", "default_color_interface", "#7DF9FF" )

        if ( ch_color_tele == "deep pink" ):
            config.set( "Params", "default_color_interface", "#ff1493" )

        if ( ch_color_tele == "raspberry" ):
            config.set( "Params", "default_color_interface", "#e30b5d" )

        if ( ch_color_tele == "lime" ):
            config.set( "Params", "default_color_interface", "#00ff00" )

        if ( ch_color_tele == "shades pink" ):
            config.set( "Params", "default_color_interface", "#FF5733" )

        if ( ch_color_tele == "fuchsia" ):
            config.set( "Params", "default_color_interface", "#FF00FF" )

        if ( ch_color_tele == "golden sand" ):
            config.set( "Params", "default_color_interface", "#F2D16B" )

        if ( ch_color_tele == "honey" or ch_color_tele == "honeysuckle" ):
            config.set( "Params", "default_color_interface", "#E2F55D" )

        if ( ch_color_tele == "coral" ):
            config.set( "Params", "default_color_interface", "#F87954" )

        if ( ch_color_tele == "medium purple" ):
            config.set( "Params", "default_color_interface", "#A164F8" )

        if ( ch_color_tele == "dark orange" ):
            config.set( "Params", "default_color_interface", "#FD8A12" )

        if ( ch_color_tele == "cl night" ):
            config.set( "Params", "default_color_interface", "#9242E1" )

        if ( ch_color_tele == "lg lime" ):
            config.set( "Params", "default_color_interface", "#00FFB7" )

        if ( "#" in ch_color_tele ):
            html_hex = ch_color_tele.strip( "#" )
            config.set( "Params", "default_color_interface", f"#{ html_hex }" )

        save()
        bot.send_message( message.chat.id, "Перезагрузите Jarvis'a или напишите в консоли программы: \"InitTheme\"" )

    if cmd.isdigit(): # isdigit - текст является числом, а не словом
        try:
            number = cmd
            number_str = num2words( number, lang="ru" )
            print( f"Ваше число { cmd } в прописи: { number_str }" )
        except KeyError:
            print( "Вы ввели слишком большое число" )

    if cmd in switch_language:
        playsound_play( f"sound\\ok1.wav" )
        gui.Get_To_History( "Jarvis: Есть!", 1 )
        pyautogui.keyDown( "altleft" )
        pyautogui.keyDown( "shift" )
        pyautogui.keyUp( "altleft" )
        pyautogui.keyUp( "shift" )

    if cmd in sub_enter:
        playsound_play( f"sound\\ok1.wav" )
        gui.Get_To_History( "Jarvis: Есть!", 1 )
        pyautogui.click()

    # if input_enter in cmd:
    #     entered = cmd.replace( input_enter, "" )
    #     print( entered )
    #     entered = entered.replace( " ", "" )
    #     print( entered )
    #     # print( f"Пишу:{ entered }" )
    #     pyautogui.typewrite( entered )

    if cmd.startswith( internet_search ):
        for word in internet_search:
            if word in cmd:
                parts = cmd.split( word, 1 )
                global wh_search
                wh_search = parts[ 1 ]
                wh_search = wh_search.strip( " " )

        # print( f"Ищу:\"{ word } { wh_search }\"" )
        gui.Get_To_History( f"Ищу: \"{ word } { wh_search }\"", 1 )
        res_search = f"{ word } { wh_search }"
        res_search = res_search.replace( " ", "+" )
        webbrowser.open_new_tab( f"yandex.ru/search/?clid=2456107&text={ res_search }&l10n=ru&lr=10732" )

    if cmd in open_full_window:
        playsound_play( f"sound\\ok1.wav" )
        gui.Get_To_History( "Jarvis: Есть!", 1 )
        pyautogui.hotkey( "win" , "up" )

    if cmd in swirt_window:
        playsound_play( f"sound\\ok1.wav" )
        gui.Get_To_History( "Jarvis: Есть!", 1 )
        pyautogui.hotkey( "win" , "down" )

    if cmd in swirt_windows:
        playsound_play( f"sound\\ok1.wav" )
        gui.Get_To_History( "Jarvis: Есть!", 1 )
        pyautogui.hotkey( "win" , "d" )

    if cmd in close_window:
        playsound_play( f"sound\\ok1.wav" )
        gui.Get_To_History( "Jarvis: Есть!", 1 )
        pyautogui.hotkey( "alt" , "F4" )

def TelegramBot():
    global self_instance

    if telegram_api == "":
        self_instance.ui.tele.setText( "Вы не ввели api своего телеграм бота." )

    if telegram_api != "":
        global _enter

        global CONNECT_SESSION
        global CONNECT
        global TIME_CONNECTED
        global CONNECT_USER
        global CONNECT_INFO

        _enter = False
        CONNECT_SESSION = False
        CONNECT = False
        TIME_CONNECTED = 0
        CONNECT_USER = "Вы не подключены."
        CONNECT_INFO = "Вы не подключены."

        code = result_cod
        self_instance.ui.tele.setText( f"Ваш код для подключения: { code }" )
        # print( code )

        config = configparser.ConfigParser()
        config.read( "user_config.ini" )

        telegra_api = config.get( "Api", "telegram_bot_key" )
        telegra_api = str( telegra_api ).strip( "\"\"" )

        global bot
        bot = telebot.TeleBot( telegra_api )

        markup = types.ReplyKeyboardMarkup( resize_keyboard=True )
        have_ = types.KeyboardButton( "У меня есть Jarvis" )
        haven_ = types.KeyboardButton( "У меня нет Jarvis" )

        con_1 = types.KeyboardButton( "Подключить" )
        con_2 = types.KeyboardButton( "Настроить" )
        con_3 = types.KeyboardButton( "Инфо" )

        up_arrow = types.KeyboardButton( "⬆️" )
        down_arrow = types.KeyboardButton( "⬇️" )
        left_arrow = types.KeyboardButton( "⬅️" )
        right_arrow = types.KeyboardButton( "➡️" )
        left_top_arrow = types.KeyboardButton( "↖️" )
        right_top_arrow = types.KeyboardButton( "↗️" )
        left_bottom_arrow = types.KeyboardButton( "↙️" )
        right_bottom_arrow = types.KeyboardButton( "↘️" )
        click = types.KeyboardButton( "👆" )

        help_1 = types.KeyboardButton( "Связь с создателем" )
        help_2 = types.KeyboardButton( "Подробнее" )
        help_3 = types.KeyboardButton( "Где можно приобрести" )
        help_4 = types.KeyboardButton( "Будущее Jarvis" )

        enter_ = types.KeyboardButton( "Управление" )

        back_ = types.KeyboardButton( "Вернуться" )
        exit_ = types.KeyboardButton( "Выход" )

        markup.add( have_, haven_ )

        # bot.send_message( 5927776020, "Дарова Настя" )
        # bot.send_message( 6280414588, "Дарова" )

        def send_sticker( src ):
            return open( src, "rb" )

        def set_j( message ):
            global can_back
            can_back = 1
            bot.send_message( message.chat.id, f"Добро пожаловать, { message.from_user.first_name }", reply_markup=markup )

        @bot.message_handler( commands=[ "start" ] )
        def welcome( message ):
            # ADMIN
            if message.chat.id == 6280414588:
                print( f"ADMIN: { message.chat.username }" )

            if message.chat.id != 6280414588:
                print( f"NO ADMIN: { message.chat.username }" )
            # ADMIN

            bot.send_sticker( message.chat.id, send_sticker( "stick/welcome.webp" ) )
            print( message )
            set_j( message )

        def con_j( message ):
            global CONNECT_SESSION
            global can_back
            
            can_back = 2

            if CONNECT_SESSION == False:
                markup = types.ReplyKeyboardMarkup( resize_keyboard=True )
                markup.add( con_1, con_2, con_3, back_ )

            if CONNECT_SESSION == True:
                markup = types.ReplyKeyboardMarkup( resize_keyboard=True )
                markup.add( con_2, con_3, enter_, exit_, back_ )

            bot.send_message( message.chat.id, "Начнем, что нужно сделать?", reply_markup=markup )

        def help_j( message ):
            global CONNECT_SESSION
            global can_back

            can_back = 3

            if CONNECT_SESSION == False:
                markup = types.ReplyKeyboardMarkup( resize_keyboard=True )
                markup.add( help_1, help_2, help_3, help_4, back_ )
            if CONNECT_SESSION == True:
                markup = types.ReplyKeyboardMarkup( resize_keyboard=True )
                markup.add( help_1, help_2, help_3, help_4, enter_, exit_, back_ )

            bot.send_message( message.chat.id, "Нужна помощь?", reply_markup=markup )

        # Nastya 5927776020

        def connect_to( message ):
            global TIME_CONNECTED
            global CONNECT_SESSION
            global CONNECT_USER
            global CONNECT
            global pin

            if pin == code.replace( " ", "" ):
                CONNECT_SESSION = True
                TIME_CONNECTED = get_now_time()
                bot.send_message( message.chat.id, "Вы успешно подключены к пк." )
                self_instance.ui.tele.setText( f"Подключение: { message.chat.username }\n({ message.chat.id })" )
                node_name = platform.node()
                CONNECT_USER = f"{ node_name }"

                markup = types.ReplyKeyboardMarkup( resize_keyboard=True )
                markup.add( con_2, con_3, enter_, exit_, back_ )
                bot.send_message( message.chat.id, "Начнем, что нужно сделать?", reply_markup=markup )

            if pin != code.replace( " ", "" ):
                bot.send_message( message.chat.id, "Проверь правильность написания кода" )
                CONNECT = False

        @bot.message_handler( commands=[ "connect" ] )
        def connect( message ):
            global CONNECT
            CONNECT = True
            bot.send_message( message.chat.id, "Введите цифры из голосового помощника." )

        @bot.message_handler( commands=[ "settings" ] )
        def settings( message ):
            pass

        @bot.message_handler( content_types=[ "text" ] )
        def txt( message ):
            global CONNECT
            global CONNECT_USER
            global CONNECT_SESSION
            global can_back
            global _enter

            if CONNECT == True:
                global pin
                pin = message.text.replace( " ", "" )
                if pin.isdigit():
                    print( f"{ message.chat.username }({ message.chat.id }) подключение: { message.text }" )
                    connect_to( message )

            elif CONNECT == False:
                if message.text == "У меня есть Jarvis":
                    bot.send_message( message.chat.id, "Тогда приступим к подключению и настройке." )
                    # markup = types.ReplyKeyboardRemove()
                    con_j( message )

                elif message.text == "У меня нет Jarvis":
                    bot.send_message( message.chat.id, "Я могу рассказать подробнее или где можно приобрести." )
                    help_j( message )

            if message.text == "Управление":
                markup = types.ReplyKeyboardMarkup( resize_keyboard=True )
                markup.add( left_top_arrow, up_arrow, right_top_arrow, left_arrow, click, right_arrow, left_bottom_arrow, down_arrow, right_bottom_arrow, con_3, back_, exit_ )

                can_back = 4
                print( can_back )

                bot.send_message( message.chat.id, "Вы перешли в управление", reply_markup=markup )
                _enter = True

            if CONNECT_SESSION == True and _enter == True:
                if message.text == "⬆️":
                    pyautogui.moveRel( 0, -20 )

                elif message.text == "⬇️":
                    pyautogui.moveRel( 0, 20 )

                elif message.text == "⬅️":
                    pyautogui.moveRel( -20, 0 )

                elif message.text == "➡️":
                    pyautogui.moveRel( 20, 0 )

                elif message.text == "↖️":
                    pyautogui.moveRel( -20, -20 )

                elif message.text == "↗️":
                    pyautogui.moveRel( 20, -20 )

                elif message.text == "↙️":
                    pyautogui.moveRel( -20, 20 )

                elif message.text == "↘️":
                    pyautogui.moveRel( 20, 20 )

                elif message.text == "👆":
                    pyautogui.click()

                elif message.text == "Вернуться" or message.text == "вернуться":
                    print( can_back )

                    CONNECT = False
                    _enter = False

                    if can_back == 2:
                        set_j( message )

                    elif can_back == 3:
                        set_j( message )

                    elif can_back == 4:
                        con_j( message )

                elif message.text == "Выход" or message.text == "выход":
                    CONNECT_SESSION = False
                    self_instance.ui.tele.setText( f"Ваш код для подключения: { code }" )
                    CONNECT_USER = "Вы не подключены."

                    markup = types.ReplyKeyboardMarkup( resize_keyboard=True )
                    markup.add( have_, haven_ )

                    bot.send_message( message.chat.id, "Вы вышли из сессии.", reply_markup=markup )
                    CONNECT = False
                    _enter = False
                    set_j( message )

                elif message.text == "Инфо":
                    # global TIME_CONNECTED
            
                    if CONNECT_SESSION == False:
                        bot.send_message( message.chat.id, "Создатель @ShadowDarkness0\nJarvis был и будет бесплатным!\n""|24.06.2023|" )
                    if CONNECT_SESSION == True:
                        bot.send_message( message.chat.id, f"Время подключения: { TIME_CONNECTED }\n"
                                                        f"Имя компьютера: { CONNECT_USER }\n"
                                                        f"Ваш user id: { message.chat.id }" )

                else:
                    if _enter == True:
                        control( message )

            elif message.text == "Вернуться" or message.text == "вернуться":
                print( can_back )

                CONNECT = False
                _enter = False

                if can_back == 2:
                    set_j( message )

                elif can_back == 3:
                    set_j( message )

                elif can_back == 4:
                    con_j( message )

            elif message.text == "Выход" or message.text == "выход":
                CONNECT_SESSION = False
                self_instance.ui.tele.setText( f"Ваш код для подключения: { code }" )
                CONNECT_USER = "Вы не подключены."

                markup = types.ReplyKeyboardMarkup( resize_keyboard=True )
                markup.add( have_, haven_ )

                bot.send_message( message.chat.id, "Вы вышли из сессии.", reply_markup=markup )
                CONNECT = False
                _enter = False
                set_j( message )

            elif message.text == "Подключить" or message.text == "подключить":
                bot.send_message( message.chat.id, "Подключение находится в beta тестировании, используйте команду /connect " )

            elif message.text == "Настроить":
                bot.send_message( message.chat.id, "Настройки находятся в тестировании, будет доступно позже." )

            elif message.text == "Инфо" or message.text == "инфо":
                if CONNECT_SESSION == False:
                    bot.send_message( message.chat.id, "Создатель @ShadowDarkness0\nJarvis был и будет бесплатным!" )
                if CONNECT_SESSION == True:
                    bot.send_message( message.chat.id, f"Время подключения: { TIME_CONNECTED }\n"
                                                        f"Имя компьютера: { CONNECT_USER }\n"
                                                        f"Ваш user id: { message.chat.id }" )

            elif message.text == "Связь с создателем":
                bot.send_message( message.chat.id, "Можете задать любой вопрос @ShadowDarkness0." )

            elif message.text == "Подробнее":
                bot.send_message( message.chat.id, "Jarvis это голосовой помощник из фильма \"Железный человек.\"\n"
                "Программа полностью бесплатна! Легка в использовании, имеет красивый интерфейс и есть виджет погоды и время.\n"
                "Jarvis предназначен для упрощения работы с пк или ноутбуком\n"
                "Также вам может понравиться история: https://dzen.ru/media/id/639b623f43447d0bb38c913e/moi-jarvis-648e04956526147a9bc7b403" )

            elif message.text == "Где можно приобрести":
                bot.send_message( message.chat.id, "Приобрести полностью бесплатно можно в оффициальном канале https://t.me/JARVIS_Free_Edition." )

            elif message.text == "Будущее Jarvis":
                bot.send_message( message.chat.id, "Как и все люди о чём-то мечтают и я не исключение. В дальнейшем я планирую сделать более красивый и удобный интерфейс, а также сделать больше настроек для конкретных нужд людей. Дальше лучше." )

            # USER INFO
            elif message.text == "user_id":
                bot.send_message( message.chat.id, message.chat.id )
            # USER INFO

        bot.polling( none_stop=True )

app = QtWidgets.QApplication( sys.argv )

search_model = True

if ( not os.path.exists( "vosk-model" ) ):
    search_model = False

    print(f"""
        { Fore.RED }[-]{ Fore.RESET }Скачайте русскую версию на:\n  https://alphacephei.com/vosk/models и распакуйте под именем "vosk-model"
    """)
    input( "Нажмите enter, чтобы выйти " )

if ( search_model == False ):
    pass
else:
    my_thread = threading.Thread( target=MainREC )
    my_thread.daemon = True 
    my_thread.start()

    win = gui()
    win.show()

    if acces_weather == True:
        thread_weather = threading.Thread( target=request_( url_weather ) )
        thread_weather.daemon = True
        thread_weather.start()

    if acces_weather == False:
        global self_instance
        gui.Update_Weather( self_instance, f"Вы отключили погоду" )

    thread_time = threading.Thread( target=updater_time_now )
    thread_time.daemon = True
    thread_time.start()

    telebot_ = threading.Thread( target=TelegramBot )
    telebot_.daemon = True
    telebot_.start()

    sys.exit( app.exec_() )