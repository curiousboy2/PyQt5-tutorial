#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
author: LiuJinYong
website: https://github.com/liujinyong
"""

import sys

from PyQt5.QtWidgets import *


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        title = QLabel('Title')

        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        gird = QGridLayout()
        gird.setSpacing(10)

        gird.addWidget(title, 1, 0)
        gird.addWidget(titleEdit, 1, 1)

        gird.addWidget(author, 2, 0)
        gird.addWidget(authorEdit, 2, 1)

        gird.addWidget(review, 3, 0)
        gird.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(gird)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())