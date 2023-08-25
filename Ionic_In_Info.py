import os
import sys

from base_dir import YML_SET
from commom.def_share.Def_Base import extract_substring
from commom.def_share.Is_Use import time_test
from commom.def_share.Yml import load_dict_by_yml


class IonicInInfo:
    def __init__(self):
        # ********1输入：
        # 1.1基本输入：
        # 项目名称

        self.name = '阳春锦绣'
        # 文件设置
        self.work_path = r'G:\0js\0专利\js\M3015'
        # 1.2位移控制设置
        self.direct = 'x'
        self.edge_layer = 5
        self.edge_sita_invert = 1000.0
        # self.dict_disp_setup = None

        # 1.3理想控制
        # 理想模型位移角 1 /
        self.dream_sita_invert = 1000
        # ---------------------
        self.dream_sita = 1000
        # 折减经验系数β
        self.pesi = 1.0
        # 2*********2 设置
        # 2.1复制的文件夹设置
        # 选择不需要复制的文件夹
        self.lst_except_son_path = []

        self.is_include_file0 = 1
        self.is_include_file1 = 1
        self.is_include_file2 = 1
        self.is_include_file3 = 1

        # 2.2输出图形设置 DrawSet
        self.y_divide_num = 2  # y轴楼层等分数量
        # 图形宽度
        self.screen_width = 12
        # 图形高度
        self.screen_high = 8
        # 2.3图形输出
        # 图形输出子文件夹
        self.jpg_path = 'DoricOut'
        # 图形输出父文件夹
        self.jpg_father_path = ''
        self.out_jpg_filename = 'g:\\1'

        # 2.4标准层控制
        # 隐藏顶部楼层数量
        self.hide_layer = 0
        # 需要显示控制的标准层
        self.lst_sign_line_layer = '5,6,7,8'  # [5, 6, 7, 8]
        # 2.5刚度控制StiffnessSet

        # 刚度类型
        self.str_k = '剪切刚度'  # '弯曲刚度''自定义刚度'
        # 自定义刚度
        self.dict_my_stiffness = {}  # {5:300, 6:400, 7:500, 8:600}
        # 3*********3 vip设置
        # 3.1 上级文件夹全部执行
        self.is_run_in_father_path = False  # False
        self.jpg_all_path = 'DoricOut_All'
        # 版权允许测试
        self.is_allowed = False


class IonicInInfoDao:
    def __init__(self, in_info=None):
        if in_info is None:
            self.in_info = IonicInInfo()
        else:
            self.in_info = in_info

    def setvar_by_dict_tab(self, dict_tab):
        for k_tab, v_tab in dict_tab.items():
            for k_frame, v_frame in v_tab.items():
                for k_ctrl, v_ctrl in v_frame.items():
                    if 'attribute' in v_ctrl:
                        value = v_ctrl['value']
                        attribute = v_ctrl['attribute']
                        setattr(self.in_info, attribute, value)
                    else:
                        continue