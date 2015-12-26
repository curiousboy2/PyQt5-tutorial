#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
author: LiuJinYong
website: https://github.com/liujinyong
"""
import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())