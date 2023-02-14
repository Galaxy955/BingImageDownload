import sys
import time
import os
import PySide6
from PySide6.QtWidgets import QWidget, QApplication
from MainWindow import Ui_Form
from CatchPic import CatchPic

dirname = os.path.dirname(PySide6.__file__)
plugin_path = os.path.join(dirname, "plugins", "platforms")
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = plugin_path

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # Get the local time.
        local_time = time.strftime("%Y-%m-%d", time.localtime())
        self.ui.today.setText("<font color=red>"+local_time+"</font>")
        self.ui.catch_button.clicked.connect(self.Catch)

    def Catch(self):
        # Get the save directory.
        save_dir = self.ui.save_addr.text()
        # Debug.
        # print(save_dir)
        catch = CatchPic()
        try:
            catch.catch(save_dir)
            self.ui.status.setText("<font color=green>Success!</font>")
        except:
            self.ui.status.setText("<font color=red>Failed!</font>")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.setWindowTitle("每日 Bing 美图下载")
    mainWindow.show()
    sys.exit(app.exec())