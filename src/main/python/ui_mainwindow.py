# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 882)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.formLayout_2 = QtWidgets.QFormLayout(self.tab)
        self.formLayout_2.setObjectName("formLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.accountLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accountLineEdit.sizePolicy().hasHeightForWidth())
        self.accountLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.accountLineEdit.setFont(font)
        self.accountLineEdit.setObjectName("accountLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.accountLineEdit)
        self.refreshPushButton = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.refreshPushButton.setFont(font)
        self.refreshPushButton.setObjectName("refreshPushButton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.refreshPushButton)
        self.autoRefreshCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.autoRefreshCheckBox.setFont(font)
        self.autoRefreshCheckBox.setObjectName("autoRefreshCheckBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.autoRefreshCheckBox)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.groupBox_2)
        self.accountInfoGroupBox = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.accountInfoGroupBox.setFont(font)
        self.accountInfoGroupBox.setObjectName("accountInfoGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.accountInfoGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.votePowerLabel = QtWidgets.QLabel(self.accountInfoGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.votePowerLabel.sizePolicy().hasHeightForWidth())
        self.votePowerLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.votePowerLabel.setFont(font)
        self.votePowerLabel.setObjectName("votePowerLabel")
        self.gridLayout_2.addWidget(self.votePowerLabel, 0, 0, 1, 1)
        self.votePowerProgressBar = QtWidgets.QProgressBar(self.accountInfoGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.votePowerProgressBar.setFont(font)
        self.votePowerProgressBar.setProperty("value", 24)
        self.votePowerProgressBar.setObjectName("votePowerProgressBar")
        self.gridLayout_2.addWidget(self.votePowerProgressBar, 1, 0, 1, 1)
        self.RCLabel = QtWidgets.QLabel(self.accountInfoGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RCLabel.sizePolicy().hasHeightForWidth())
        self.RCLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RCLabel.setFont(font)
        self.RCLabel.setObjectName("RCLabel")
        self.gridLayout_2.addWidget(self.RCLabel, 2, 0, 1, 1)
        self.RCProgressBar = QtWidgets.QProgressBar(self.accountInfoGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RCProgressBar.setFont(font)
        self.RCProgressBar.setProperty("value", 24)
        self.RCProgressBar.setObjectName("RCProgressBar")
        self.gridLayout_2.addWidget(self.RCProgressBar, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.STEEMLabel = QtWidgets.QLabel(self.accountInfoGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.STEEMLabel.setFont(font)
        self.STEEMLabel.setObjectName("STEEMLabel")
        self.horizontalLayout.addWidget(self.STEEMLabel)
        self.SBDLabel = QtWidgets.QLabel(self.accountInfoGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SBDLabel.setFont(font)
        self.SBDLabel.setObjectName("SBDLabel")
        self.horizontalLayout.addWidget(self.SBDLabel)
        self.SPLabel = QtWidgets.QLabel(self.accountInfoGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SPLabel.setFont(font)
        self.SPLabel.setObjectName("SPLabel")
        self.horizontalLayout.addWidget(self.SPLabel)
        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.accountInfoGroupBox)
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.text2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text2.setFont(font)
        self.text2.setText("")
        self.text2.setObjectName("text2")
        self.gridLayout_3.addWidget(self.text2, 0, 2, 1, 1)
        self.text = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.text.setFont(font)
        self.text.setText("")
        self.text.setObjectName("text")
        self.gridLayout_3.addWidget(self.text, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.frame)
        self.lastUpvotesLabel = QtWidgets.QLabel(self.tab)
        self.lastUpvotesLabel.setObjectName("lastUpvotesLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lastUpvotesLabel)
        self.lastUpvotesListWidget = QtWidgets.QListWidget(self.tab)
        self.lastUpvotesListWidget.setObjectName("lastUpvotesListWidget")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.lastUpvotesListWidget)
        self.curationRewardLabel = QtWidgets.QLabel(self.tab)
        self.curationRewardLabel.setObjectName("curationRewardLabel")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.curationRewardLabel)
        self.lastCurationListWidget = QtWidgets.QListWidget(self.tab)
        self.lastCurationListWidget.setObjectName("lastCurationListWidget")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.lastCurationListWidget)
        self.authorRewardLabel = QtWidgets.QLabel(self.tab)
        self.authorRewardLabel.setObjectName("authorRewardLabel")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.authorRewardLabel)
        self.lastAuthorListWidget = QtWidgets.QListWidget(self.tab)
        self.lastAuthorListWidget.setObjectName("lastAuthorListWidget")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.lastAuthorListWidget)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.accountHistListWidget = QtWidgets.QListWidget(self.tab_3)
        self.accountHistListWidget.setObjectName("accountHistListWidget")
        self.gridLayout_5.addWidget(self.accountHistListWidget, 1, 0, 1, 1)
        self.accountHistNotificationCheckBox = QtWidgets.QCheckBox(self.tab_3)
        self.accountHistNotificationCheckBox.setObjectName("accountHistNotificationCheckBox")
        self.gridLayout_5.addWidget(self.accountHistNotificationCheckBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.bookkeepingLabel = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bookkeepingLabel.setFont(font)
        self.bookkeepingLabel.setWordWrap(False)
        self.bookkeepingLabel.setObjectName("bookkeepingLabel")
        self.verticalLayout.addWidget(self.bookkeepingLabel)
        self.drugwarsPushButton = QtWidgets.QPushButton(self.tab_2)
        self.drugwarsPushButton.setObjectName("drugwarsPushButton")
        self.verticalLayout.addWidget(self.drugwarsPushButton)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Settings"))
        self.label_3.setText(_translate("MainWindow", "account"))
        self.refreshPushButton.setText(_translate("MainWindow", "Refresh"))
        self.autoRefreshCheckBox.setText(_translate("MainWindow", "Auto refresh"))
        self.accountInfoGroupBox.setTitle(_translate("MainWindow", "holger80 (70)"))
        self.votePowerLabel.setText(_translate("MainWindow", "Vote Power"))
        self.RCLabel.setText(_translate("MainWindow", "RC"))
        self.RCProgressBar.setFormat(_translate("MainWindow", "%p% full in 87 hours"))
        self.STEEMLabel.setText(_translate("MainWindow", "TextLabel"))
        self.SBDLabel.setText(_translate("MainWindow", "TextLabel"))
        self.SPLabel.setText(_translate("MainWindow", "TextLabel"))
        self.lastUpvotesLabel.setText(_translate("MainWindow", "Lastest Upvotes (last 24h)"))
        self.curationRewardLabel.setText(_translate("MainWindow", "Latest curation rewards (last 24h)"))
        self.authorRewardLabel.setText(_translate("MainWindow", "Latest author rewards (last 24h)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Account info"))
        self.accountHistNotificationCheckBox.setText(_translate("MainWindow", "Notification on all events"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Account history"))
        self.bookkeepingLabel.setText(_translate("MainWindow", "TextLabel"))
        self.drugwarsPushButton.setText(_translate("MainWindow", "Show drugwars stats"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "bookkeeping"))

