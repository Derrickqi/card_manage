#!/usr/bin/python3
import card_tools
while True:
    # TODO 显示功能菜单
    card_tools.show_menu()

    action_str = input("请输入您希望执行的操作:")
    print("您选择的操作是【{0}】" .format(action_str))

    #1,2,3 针对名片的操作
    if action_str in ["1","2","3"]:
    #新增
         if action_str == "1":
            card_tools.new_card()
    # 显示
         elif action_str == "2":
            card_tools.show_all()
    #查询
         elif action_str == "3":
            card_tools.search_card()
    #0 退出系统
    elif action_str == "0":
        print("欢迎再次使用『名片管理系统』")
        #pass 站位符，保证系统正常，且无任何操作
        break

    else:
        print("您输入的不正确清重新输入")