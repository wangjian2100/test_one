import os
import sys


class YmlSet:
    def __init__(self, base_dir):
        # ********0.3文件夹：
        self.sys_path = os.path.join(base_dir, r'config\yml_set')
        self.work_path = os.path.join(base_dir, r'config\yml_work')
        self.main_path = os.path.join(base_dir, r'config\yml_main')
        # ********0.1主页面配置：
        self.tab_yml = os.path.join(self.sys_path, 'in_tab.yml')
        self.bak_tab_yml = os.path.join(self.sys_path, 'in_tab.bak')
        self.sys_tab_yml = os.path.join(self.sys_path, 'in_tab.sys')
        self.lst_com_set_yml_filename = os.path.join(self.sys_path, 'com_set.sys')
        # ********0.2测试页面配置：
        # self.gui_question_title_yml = os.path.join(self.sys_path, 'dict_question_title.yml')
        # self.gui_question_body_yml = os.path.join(self.sys_path, 'dict_question_body.yml')
        # self.gui_ck_question_body_yml = os.path.join(self.sys_path, 'dict_ck_question_body.yml')
        # ********0.4工作文件：
        self.in_wzq = os.path.join(self.work_path, 'in_wzq.yml')

        # ********0.5out文件：
        self.struc_in_var_path = r'G:\PyPro\ionic1_pro\config\var_temp'
        self.struc_in_yml_path = r'G:\PyPro\ionic1_pro\config\yml_struc_in'
        self.general_mid_yml_path = r'G:\PyPro\ionic1_pro\config\yml_general_mid'
        # debug
        self.work_in_path = r'G:\0js\00\G7电算\G7219'
# 要返回类所在的.py 文件的绝对路径
BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
YML_SET = YmlSet(BASE_DIR)
