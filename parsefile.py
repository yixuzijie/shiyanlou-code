#!D:\Python37-32\python.exe

import os
import sys


def parse_file(path):
    """
    ���������ı��ļ���������ո��Ʊ�����е������Ϣ

    :arg path: Ҫ�������ı��ļ���·��

    :return: �����ո������Ʊ������������Ԫ��
    """
    fd = open(path)
    i = 0
    spaces = 0
    tabs = 0
    for i,line in enumerate(fd):
        spaces += line.count(' ')
        tabs += line.count('\t')
    # ���ڹرմ򿪵��ļ�
    fd.close()

    # ��Ԫ����ʽ���ؽ��
    return spaces, tabs, i + 1

def main(path):
    """
    �������ڴ�ӡ�ļ��������

    :arg path: Ҫ�������ı��ļ���·��
    :return: ���ļ�������Ϊ True������ False
    """
    if os.path.exists(path):
        spaces, tabs, lines = parse_file(path)
        print("Spaces {}. tabs {}. lines {}".format(spaces, tabs, lines))
        return True
    else:
        return False


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        sys.exit(-1)
    sys.exit(0)
