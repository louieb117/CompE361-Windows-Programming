import openpyxl
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import pandas as pd
import sys

from pandas import ExcelWriter


class SideMenu(QMainWindow):
    def __init__(self):
        # QMainWindow initialization
        super(SideMenu, self).__init__()

    def activate_side_menu(self, window):
        # Button
        window.pb_listusers.clicked.connect(window.gui_listusers)
        window.pb_adduser.clicked.connect(window.gui_adduser)
        window.pb_updateuser.clicked.connect(window.gui_updateuser)
        window.pb_deleteuser.clicked.connect(window.gui_deleteuser)

        window.pb_listbooks.clicked.connect(window.gui_listbooks)
        window.pb_addbook.clicked.connect(window.gui_addbook)
        window.pb_updatebook.clicked.connect(window.gui_updatebook)
        window.pb_deletebook.clicked.connect(window.gui_deletebook)

        window.pb_listorders.clicked.connect(window.gui_listorders)
        window.pb_createorder.clicked.connect(window.gui_createorder)
        window.pb_updateorders.clicked.connect(window.gui_updateorders)
        window.pb_cancelorder.clicked.connect(window.gui_cancelorder)

    def gui_listusers(self):
        # Debug Message
        print('gui_listuser')
        self.close()
        # Load next GUI
        self.show_admin_listusers_gui = AdminLU()

    def gui_adduser(self):
        # Debug Message
        print('gui_adduser')
        self.close()
        # Load next GUI
        self.show_admin_adduser_gui = AdminAU()

    def gui_updateuser(self):
        # Debug Message
        print('gui_updateuser')
        self.close()
        # Load next GUI
        self.show_admin_updateuser_gui = AdminUU()

    def gui_deleteuser(self):
        # Debug Message
        print('gui_deleteuser')
        self.close()
        # Load next GUI
        self.show_admin_deleteuser_gui = AdminDU()

    def gui_listbooks(self):
        # Debug Message
        print('gui_listbooks')
        self.close()
        # Load next GUI
        self.show_admin_listbooks_gui = AdminLB()

    def gui_addbook(self):
        # Debug Message
        print('gui_addbook')
        self.close()
        # Load next GUI
        self.show_admin_addbook_gui = AdminAB()

    def gui_updatebook(self):
        # Debug Message
        print('gui_updatebook')
        self.close()
        # Load next GUI
        self.show_admin_updatebook_gui = AdminUB()

    def gui_deletebook(self):
        # Debug Message
        print('gui_deletebook')
        self.close()
        # Load next GUI
        self.show_admin_deletebook_gui = AdminDB()

    def gui_listorders(self):
        # Debug Message
        print('gui_listorders')
        self.close()
        # Load next GUI
        self.show_admin_listorders_gui = AdminLO()

    def gui_createorder(self):
        # Debug Message
        print('gui_createorder')
        self.close()
        # Load next GUI
        self.show_admin_createorder_gui = AdminAO()

    def gui_updateorders(self):
        # Debug Message
        print('gui_updateorder')
        self.close()
        # Load next GUI
        self.show_admin_updateorder_gui = AdminUO()

    def gui_cancelorder(self):
        # Debug Message
        print('gui_cancelorder')
        self.close()
        # Load next GUI
        self.show_admin_cancelorder_gui = AdminDO()


class AdminMain(SideMenu):
    def __init__(self):
        # QMainWindow initialization
        super(AdminMain, self).__init__()

        # Load UI file
        #self.ui_file = ui_file
        uic.loadUi('UI/AdminMain.ui', self)
        self.show()
        SideMenu().activate_side_menu(self)


class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        super(PandasModel, self).__init__()
        self.df_data = data


    def rowCount(self, parent=None):
        return self.df_data.shape[0]

    def columnCount(self, parent=None):
        return self.df_data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self.df_data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.df_data.columns[col]
        return None


class AdminLU(SideMenu):

    def __init__(self):
        # QMainWindow initialization
        super(AdminLU, self).__init__()
        # Data frame
        self.df_users = pd.read_excel('database_copy.xlsx', sheet_name='users').drop(columns='password')

        # Load UI file
        uic.loadUi('UI/Admin_LU.ui', self)
        self.show()

        # Side Menu
        SideMenu().activate_side_menu(self)

        # Displaying to table view widget
        model = PandasModel(self.df_users)
        view = self.tv_listusers
        view.setModel(model)
        view.show()
        print('table View')


class AdminAU(SideMenu):
    def __init__(self):
        # QMainWindow initialization
        super(AdminAU, self).__init__()
        # Load UI file
        uic.loadUi('UI/Admin_AU.ui', self)
        self.show()



        SideMenu().activate_side_menu(self)

        # Button
        self.pb_create.clicked.connect(self.gui_state)

    def creation_gate(self):
        # Load UI file
        uic.loadUi('UI/Admin_AU.ui', self)
        self.show()

        # Button
        self.pb_create.clicked.connect(self.gui_state)

    def gui_state(self):
        # Data frame
        self.df_users = pd.read_excel('database_copy.xlsx', sheet_name='users')
        self.log_user = self.df_users.loc[self.df_users.username == self.le_username.text()].reset_index()
        # Check if empty or not in db
        if len(self.le_username.text()) != 0 & len(self.log_user) != 0:
            if self.le_password.text() == self.le_reenterpassword.text():
                username = self.le_username.text()
                password = self.le_password.text()
                if self.rb_admin.isDown():
                    admin = 'TRUE'
                else:
                    admin = 'FALSE'

                mb = QMessageBox()
                mb.setWindowTitle('Username added')
                mb.setText('Are you sure you want to add user?\n ')
                mb.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                res = mb.exec()
                if res == QMessageBox.Yes:
                    with ExcelWriter('database_copy.xlsx', mode="a", if_sheet_exists="overlay") as writer:
                        self.df_users.loc[len(self.df_users)] = [len(self.df_users), username, password, admin]
                        self.df_users.to_excel(writer, sheet_name='users', index=False)
                    print('user added')
                    self.close()
                    self.creation_gate()
                elif res == QMessageBox.No:
                    self.close()
                    self.creation_gate()

        else:
            mb = QMessageBox()
            if self.log_user.empty:
                mb.setWindowTitle('No Username entered')
                mb.setText('No Username entered\nPlease enter username')
            else:
                mb.setWindowTitle('Username already exist')
                mb.setText('Username already exist\nPlease enter new username')
            mb.setStandardButtons(QMessageBox.Ok)
            res = mb.exec()
            if res == QMessageBox.Ok:
                self.close()
                self.creation_gate()


class AdminUU(SideMenu):

    def __init__(self):
        # QMainWindow initialization
        super(AdminUU, self).__init__()

        # Data frame
        self.df_users = pd.read_excel('database_copy.xlsx', sheet_name='users').drop(columns='password')

        # Load UI file
        uic.loadUi('UI/Admin_UU.ui', self)
        self.show()

        SideMenu().activate_side_menu(self)

        # Displaying to table view widget
        model = PandasModel(self.df_users)
        view = self.tv_updateuser
        view.setModel(model)
        view.show()
        print('table View')

class AdminDU(SideMenu):

    def __init__(self):
        # QMainWindow initialization
        super(AdminDU, self).__init__()

        # Data frame
        self.df_users = pd.read_excel('database_copy.xlsx', sheet_name='users').drop(columns='password')

        # Load UI file
        uic.loadUi('UI/Admin_DU.ui', self)
        self.show()

        SideMenu().activate_side_menu(self)

        # Displaying to table view widget
        model = PandasModel(self.df_users)
        view = self.tv_deleteuser
        view.setModel(model)
        view.show()
        print('table View')



    def confirm(self):
        mb = QMessageBox()
        mb.setWindowTitle('Username already exist')
        mb.setText('Username already exist\nPlease enter new username')
        mb.setStandardButtons(QMessageBox.Ok)
        res = mb.exec()
        if res == QMessageBox.Ok:
            self.close()
            self.creation_gate()



class AdminLB(SideMenu):

    def __init__(self):
        # QMainWindow initialization
        super(AdminLB, self).__init__()

        # Data frame
        self.df_books = pd.read_excel('database_copy.xlsx', sheet_name='books')

        # Load UI file
        uic.loadUi('UI/Admin_LB.ui', self)
        self.show()

        SideMenu().activate_side_menu(self)

        # Displaying to table view widget
        model = PandasModel(self.df_books)
        view = self.tv_listbooks
        view.setModel(model)
        view.show()
        print('table View')


class AdminAB(SideMenu):
    def __init__(self):
        # QMainWindow initialization
        super(AdminAB, self).__init__()
        # Load UI file
        uic.loadUi('UI/Admin_AB.ui', self)
        self.show()

        SideMenu().activate_side_menu(self)


class AdminUB(SideMenu):

    def __init__(self):
        # QMainWindow initialization
        super(AdminUB, self).__init__()

        # Data frame
        self.df_books = pd.read_excel('database_copy.xlsx', sheet_name='books')


        # Load UI file
        uic.loadUi('UI/Admin_UB.ui', self)
        self.show()

        SideMenu().activate_side_menu(self)

        # Displaying to table view widget
        model = PandasModel(self.df_books)
        view = self.tv_updatebook
        view.setModel(model)
        view.show()
        print('table View')


class AdminDB(SideMenu):

    def __init__(self):
        # QMainWindow initialization
        super(AdminDB, self).__init__()

        # Data frame
        self.df_books = pd.read_excel('database_copy.xlsx', sheet_name='books')

        # Load UI file
        uic.loadUi('UI/Admin_DB.ui', self)
        self.show()

        SideMenu().activate_side_menu(self)

        # Displaying to table view widget
        model = PandasModel(self.df_books)
        view = self.tv_deletebook
        view.setModel(model)
        view.show()
        print('table View')


class AdminLO(SideMenu):

    def __init__(self):
        # QMainWindow initialization
        super(AdminLO, self).__init__()

        # Data frame
        self.df_orders = pd.read_excel('database_copy.xlsx', sheet_name='orders')

        # Load UI file
        uic.loadUi('UI/Admin_LO.ui', self)
        self.show()

        SideMenu().activate_side_menu(self)

        # Displaying to table view widget
        model = PandasModel(self.df_orders)
        view = self.tv_listorders
        view.setModel(model)
        view.show()
        print('table View')


class AdminAO(SideMenu):

    def __init__(self):
        # QMainWindow initialization
        super(AdminAO, self).__init__()

        # Load UI file
        uic.loadUi('UI/Admin_AO.ui', self)
        self.show()

        SideMenu().activate_side_menu(self)


class AdminUO(SideMenu):

    def __init__(self):
        # QMainWindow initialization
        super(AdminUO, self).__init__()

        # Data frame
        self.df_orders = pd.read_excel('database_copy.xlsx', sheet_name='orders')

        # Load UI file
        uic.loadUi('UI/Admin_UO.ui', self)
        self.show()

        SideMenu().activate_side_menu(self)

        # Displaying to table view widget
        model = PandasModel(self.df_orders)
        view = self.tv_updateorder
        view.setModel(model)
        view.show()
        print('table View')


class AdminDO(SideMenu):

    def __init__(self):
        # QMainWindow initialization
        super(AdminDO, self).__init__()

        # Data frame
        self.df_orders = pd.read_excel('database_copy.xlsx', sheet_name='orders')

        # Load UI file
        uic.loadUi('UI/Admin_DO.ui', self)
        self.show()

        SideMenu().activate_side_menu(self)


        # Displaying to table view widget
        model = PandasModel(self.df_orders)
        view = self.tv_deleteorder
        view.setModel(model)
        view.show()
        print('table View')