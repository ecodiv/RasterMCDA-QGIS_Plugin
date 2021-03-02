# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RastermcdaDialog
                                 A QGIS plugin
 Plugin implementing MCDA, for raster datasets
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-10-25
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Wallner Andreas Georg
        email                : andreasgeorg.wallner@edu.fh-kaernten.ac.at
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.PyQt.QtWidgets import QMessageBox

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'raster_MCDA_dialog_base.ui'))
    
FORM_CLASS1, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'raster_MCDA_dialog_weight_PC.ui'))


class RastermcdaDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(RastermcdaDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.textBrowser_info.setText("""Plugin by: WALLNER Andreas, Student: CUAS, Geoinformation and Environmental Technologies
        
Raster MCDA is a Plugin to solve MCDA problems based on raster data.
Implemented decision rules are: WLC, Ideal Point (TOPSIS) and OWA method. 
Relevant raster data can be added to a criterion table.
Within the table weights and a factor, relevant for a necessary standardisation, can be set.
Sum of weights should be 1
To run the Plugin, select an output location and click OK.
More details: Click Show Help...
""")

    def createQTables(self):
        #Create Row and collum of Table_WLC
        self.tableWidget_wlc.setRowCount(0)
        self.tableWidget_wlc.setColumnCount(3)
        self.tableWidget_wlc.setColumnWidth(0, 200)
        self.tableWidget_wlc.setColumnWidth(1, 120)
        self.tableWidget_wlc.setColumnWidth(2, 60)
        self.tableWidget_wlc.setHorizontalHeaderLabels(["criterion","benefit=1 / cost=0","weight"])
        
        # Create Row and collum of Table_IP
        self.tableWidget_ip.setRowCount(0)
        self.tableWidget_ip.setColumnCount(5)
        self.tableWidget_ip.setColumnWidth(0, 200)
        self.tableWidget_ip.setColumnWidth(1, 120)
        self.tableWidget_ip.setColumnWidth(2, 60)
        self.tableWidget_ip.setHorizontalHeaderLabels(["criterion","benefit=1 / cost=0","weight","ideal point","neg. ideal point"])
        
        # Create Row and collum of Table_OWA
        self.tableWidget_owa.setRowCount(0)
        self.tableWidget_owa.setColumnCount(3)
        self.tableWidget_owa.setColumnWidth(0, 200)
        self.tableWidget_owa.setColumnWidth(1, 120)
        self.tableWidget_owa.setColumnWidth(2, 60)
        self.tableWidget_owa.setHorizontalHeaderLabels(["criterion","benefit=1 / cost=0","weight"])
        
        
        self.tableWidget_con.setRowCount(0)
        self.tableWidget_con.setColumnCount(1)
        self.tableWidget_con.setColumnWidth(0, 300)
        self.tableWidget_con.setHorizontalHeaderLabels(["constraint layer name"])
        
        self.tabWidget_decision_rule.setCurrentIndex(0)
        
        self.textBrowser_checkWeights.setVisible(False)
        self.label_checkWeights.setVisible(False)
        self.pushButton_help.setVisible(False)
        
        self.label_help.setText('<a href="https://github.com/awallner-WallE/RasterMCDA-QGIS_Plugin/wiki">Show Help...</a>')
        self.label_help.setOpenExternalLinks(True)

#---------------------------------------User information - Message Box------------------------------------

    # Example: https://www.tutorialspoint.com/pyqt/pyqt_qmessagebox.htm
    def showMessageBox(self, boxType, title,  msgText, infoText, detailedText): 
        msg = QMessageBox()
        msg.setIcon(boxType)
        msg.setWindowTitle(title)
        msg.setText(msgText)
        msg.setInformativeText(infoText)
        msg.setDetailedText(detailedText)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
    
    # old method for showing help (before github wiki)
    def showHelp(self): 
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setStyleSheet("QLabel{min-width: 300px;}");
        msg.setWindowTitle("Help")
        msg.setText("Raster MCDA Help")
        msg.setInformativeText("Use the plugin as followed: (Details)")
        msg.setDetailedText("""
        1. Choose between WLC or IP Decision rules method.\n\n
        2. Add the relevant criteria (raster layer) from the combo box to the criterion table.\n
            Use min 2 criterion layers!\n\n
        3. If a raster is not standartized [mmin value > 0, max value < 1, it willget standartized automatically.\n
            IMPORTANT choose benefit (1) or cost (0) criteria in the criterion table, when working with non standarized rasters.\n
            Use only rasters with same cellsize, origin, extend and reference system.\n\n
        4. Choose weights: Weights are calculated automatically when adding a new layer to the table.\n
            When editing the weights keep watch that the sum of weights = 1.\n
            Otherwise the plugin will normalize the existing weights.\n\n
        5. Choose path for the output raster.\n\n
        RUN the Plugin by clicking OK""")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        

class RastermcdaWeightingPCDialog(QtWidgets.QDialog, FORM_CLASS1):
    def __init__(self, parent=None):
        """Constructor."""
        super(RastermcdaWeightingPCDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        
        self.tableWidget_saaty.setRowHeight(0, 50)
        
        self.label_help.setText('<a href="https://github.com/awallner-WallE/RasterMCDA-QGIS_Plugin/wiki">Show Help...</a>')
        self.label_help.setOpenExternalLinks(True)
