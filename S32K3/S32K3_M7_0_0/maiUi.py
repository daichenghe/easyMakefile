import sys  
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QLabel, QComboBox, QCheckBox  

class MakefileGenerator(QWidget):  
    def __init__(self):  
        super().__init__()  
        # self.initUI()  

    def initUI(self, MainWindow):  
        # 初始化界面布局  
        layout = QVBoxLayout()  
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 添加选择框  
        self.project_dir_label = QLabel('选择工程目录:')  
        self.project_dir_button = QPushButton('浏览')  
        self.project_dir_button.clicked.connect(self.select_project_dir)  
        self.project_dir_path = None  

        h_layout_dir = QHBoxLayout()  
        h_layout_dir.addWidget(self.project_dir_label)  
        h_layout_dir.addWidget(self.project_dir_button)  
        layout.addLayout(h_layout_dir)  

        self.makefile_template_label = QLabel('选择Makefile模板:')  
        self.makefile_template_button = QPushButton('浏览')  
        self.makefile_template_button.clicked.connect(self.select_makefile_template)  
        self.makefile_template_path = None  

        h_layout_template = QHBoxLayout()  
        h_layout_template.addWidget(self.makefile_template_label)  
        h_layout_template.addWidget(self.makefile_template_button)  
        layout.addLayout(h_layout_template)  

        self.output_dir_label = QLabel('选择输出目录:')  
        self.output_dir_button = QPushButton('浏览')  
        self.output_dir_button.clicked.connect(self.select_output_dir)  
        self.output_dir_path = None  

        h_layout_output = QHBoxLayout()  
        h_layout_output.addWidget(self.output_dir_label)  
        h_layout_output.addWidget(self.output_dir_button)  
        layout.addLayout(h_layout_output)  

        # 添加下拉框（备用）  
        self.dropdown_label = QLabel('下拉框:')  
        self.dropdown = QComboBox()  
        self.dropdown.addItem('选项1')  
        self.dropdown.addItem('选项2')  
        h_layout_dropdown = QHBoxLayout()  
        h_layout_dropdown.addWidget(self.dropdown_label)  
        h_layout_dropdown.addWidget(self.dropdown)  
        layout.addLayout(h_layout_dropdown)  

        # 添加复选框（备用）  
        self.checkbox1 = QCheckBox('复选框1')  
        self.checkbox2 = QCheckBox('复选框2')  
        h_layout_checkboxes = QHBoxLayout()  
        h_layout_checkboxes.addWidget(self.checkbox1)  
        h_layout_checkboxes.addWidget(self.checkbox2)  
        layout.addLayout(h_layout_checkboxes)  

        # 添加按钮来生成Makefile  
        self.generate_button = QPushButton('生成Makefile')  
        self.generate_button.clicked.connect(self.generate_makefile)  
        layout.addWidget(self.generate_button)  

        # 添加标签来显示结果  
        # self.result_label = QLabel('等待生成...')  
        self.result_label = QLabel(self.centralwidget)
        self.result_label.setText("test")
        self.result_label.setText("xxx")        
        layout.addWidget(self.result_label)  

        # 设置窗口属性  
        self.setLayout(layout)  
        self.setWindowTitle('Makefile生成器')  
        self.setGeometry(300, 300, 400, 300)  
  
    def select_project_dir(self):  
        directory = QFileDialog.getExistingDirectory(self, '选择工程目录')  
        self.project_dir_path = directory  
  
    def select_makefile_template(self):  
        file_name, _ = QFileDialog.getOpenFileName(self, '选择Makefile模板', '', 'Makefile Files (*.makefile)')  
        self.makefile_template_path = file_name  
  
    def select_output_dir(self):  
        directory = QFileDialog.getExistingDirectory(self, '选择输出目录')  
        self.output_dir_path = directory  
  
    def generate_makefile(self): 
        # self.result_label.setText("test")
        print('222')
        # self.result_label.update()
        self.result_label.setText("222")
        
if __name__ == '__main__':
    app = QApplication([])
    MainWindow = QMainWindow()
    ui = MakefileGenerator()
    ui.initUI(MainWindow)
    ui.show()
    # MainWindow.show()
    app.exec_()
    # sys.exit(app.exec_())