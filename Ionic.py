from Ionic_In_Info import IonicInInfo
from commom.gui.Gui_Run import GuiRunDao
from doric.setting.Com_set import ComSetDao

if __name__ == '__main__':
    def do_main():
        in_info = IonicInInfo()

        # 构造设置信息 com_set
        com_set_dao = ComSetDao()
        com_set_dao.set_var()
        com_set_dao.reset_var(in_info)
        com_set = com_set_dao.com_set
        # 执行
        gui_run_dao = GuiRunDao()
        gui_run_dao.set_value(in_info, com_set)
        gui_run_dao.run_gui()


    do_main()
