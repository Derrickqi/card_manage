#记录所有的名片列表
card_list = []

def show_menu():
    """显示功能菜单 """
    print("")
    print("*" * 50)
    print("欢迎使用『名片管理系统』V1.0")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.查询信息")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("*" * 50)
    print("新增名片")
    #1.提示用户输入信息
    name = input("请输入姓名:")
    tel_str = input("请输入电话:")
    QQ = input("请输入QQ：")
    Email= input("请输入邮箱:")

    #2.建立一个字典
    card_dict = {"name":name,
                 "tel":tel_str,
                 "QQ":QQ,
                 "Email":Email}

    #3.将名片添加到字典
    card_list.append(card_dict)
    print(card_list)

    #4.提示用户添加成功
    print("添加%s的名片成功" % name)


def show_all():
    """显示所有名片"""
    print("*" * 50)
    print("显示所有名片")

    #判断名片记录是否存在
    if len(card_list) == 0:
        print("当前没有任何名片记录，请增加功能名片！")

        return
    #打印表头
    for name in ["姓名","电话","QQ","邮箱"]:
        print(name,end="\t\t")

    print(" ")

    print("=" * 50)

    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["tel"],
                                        card_dict["QQ"],
                                        card_dict["Email"]))

    print("")
    print("显示名片成功")


def search_card():
    """搜索名片"""
    print("搜索名片")
    #1.提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的姓名")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["tel"],
                                            card_dict["QQ"],
                                            card_dict["Email"]))
            del_card(card_dict)

            break
    else:
        print("抱歉,搜索的姓名不存在！")


def del_card(find_dict):
    print(find_dict)
    action_str = input("清选择需要执行的操作 "
                       "[1].修改  [2].删除 [0] 返回上级菜单:")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"],"姓名(回车不修改):")
        find_dict["QQ"] = input_card_info(find_dict["QQ"],"QQ（回车不修改）:")
        find_dict["tel"] = input_card_info(find_dict["tel"],"tel（回车不修改）:")
        find_dict["Email"] = input_card_info(find_dict["Email"],"Email（回车不修改）:")

        print("修改名片成功")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除名片成功")

def input_card_info (dict_value,tip_message):
    """输入名片信息
    :param dict_value:  字典中原有的值
    :param tip_message: 名片信息
    :return:
    """
    #1.提示用户输入内容
    result_str = input(tip_message)
    if len(result_str) > 0 :
    # 2.如果输入内容，直接返回结果
        return result_str
    # 3.若不输入内容，则返回原值
    else:
        return dict_value


   
