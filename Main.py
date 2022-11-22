#!/usr/bin/env python3
# coding=utf-8

import re
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

list_of_numbers = []


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)

        self.setWindowTitle('Работа с массивами и файлами в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_upload_data.clicked.connect(self.upload_data_from_file)
        self.btn_process_data.clicked.connect(self.process_data)
        self.btn_save_data.clicked.connect(self.save_data_in_file)
        self.btn_clear.clicked.connect(self.clear)

    def upload_data_from_file(self):
        """
        загружаем данные из файла
        :return: pass
        """
        global path_to_file
        path_to_file = QFileDialog.getOpenFileName(self, 'Открыть файл', '', "Text Files (*.txt)")[0]

        if path_to_file:
            file = open(path_to_file, 'r')

            data = file.read()
            # выводим считанные данные на экран
            self.plainTextEdit.appendPlainText("Полученные данные: \n" + data + "\n")

            global list_of_numbers
            list_of_numbers = []

            # \b -- ищет границы слов
            # [0-9] -- описывает что ищем
            # + -- говорит, что искать нужно минимум от 1 символа
            #for num in re.findall(r'\b[0-9]+\b', "\-?\d*\.?\d+" data):
            for num in re.findall("\-?\d*\.?\d+", data):
                list_of_numbers.append(num)

    def process_data(self):
        if validation_of_data():
            min_num = find_min()

            # -*- выполнение задания -*-
            if str(min_num) == list_of_numbers[1]:
                print(min_num)
                nulling_second_coulumn(min_num)

                self.plainTextEdit.appendPlainText("Данные обработаны! " + '\n')

                # выводим список на экран
                for k, i in enumerate (list_of_numbers):
                    self.plainTextEdit.insertPlainText(str(i) + " ")
                    # чтобы текст был в виде таблицы, делаем отступ после
                    # 6 элемента
                    if ((k + 1) % 5) == 0:
                        self.plainTextEdit.appendPlainText("")
            else:
                self.plainTextEdit.appendPlainText(
                    " Минимальный элемент не стоит во втором столбце")
        else:
            self.plainTextEdit.appendPlainText("Неправильно введены данные! "
                                               "Таблица должна быть размером "
                                               "5х6 и состоять из чисел! \n")

    def save_data_in_file(self):
        """
        сохраняем данные в выбранный нами файл
        :return:
        """
        if path_to_file:
            file = open(path_to_file.split(".")[0] + '-Output.txt', 'w')

            for k, i in enumerate(list_of_numbers):
                file.write(i + " ")
                if ((k+1) % 5) == 0:
                    file.write("\n")

            file.close()

            self.plainTextEdit.appendPlainText("Файл был успешно загружен! \n")
        else:
            self.plainTextEdit.appendPlainText("Для начала загрузите файл!")

    def clear(self):
        self.plainTextEdit.clear()


def find_min():
    """
    находим минимальное число в списке
    :return: минимальное число
    """
    min_num = None
    for i in list_of_numbers:
        if min_num is None or int(i) < min_num :
            min_num = int(i)
    return min_num




def validation_of_data():
    """
    проверяем данные на валидность: всего должно быть ровно 30 ЧИСЕЛ
    :return: True - данные корректны, False - нет
    """
    if len(list_of_numbers) == 30:
        for i in list_of_numbers:
            try:
                float(i)
            except Exception:
                return False
        return True
    else:
        return False


def nulling_second_coulumn(min_num):

    for n, i in enumerate(list_of_numbers):
        if int(i) == min_num:
            list_of_numbers[1] = str(min_num * 0)
            list_of_numbers[6] = str(min_num * 0)
            list_of_numbers[11] = str(min_num * 0)
            list_of_numbers[16] = str(min_num * 0)
            list_of_numbers[21] = str(min_num * 0)
            list_of_numbers[26] = str(min_num * 0)
            break
    pass

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
