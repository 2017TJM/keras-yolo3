#图像ID要改变 首先要获得图像id
#author:TJM2017 
#time 2019/5/7
import os
import random
from os import getcwd
import xml.etree.ElementTree as ET
wd = getcwd()   # current working path
#print(wd)
def image_id_list():
    path ='voc\VOCdevkit\VOC2019\Annotations'
    list_item=os.listdir(path)
    image_ids_=[]
    for item in list_item:
        image_ids_.append(item)
    #print(image_ids_)
    return image_ids_

# 需要扫描文件夹
#方法1
import xml.dom.minidom
path = 'voc\VOCdevkit\VOC2019\Annotations\\'
list_dir_xml = os.listdir(path)

def list_imag_ids(path=path,list_dir_xml=list_dir_xml):
    list_image_id = []
    for file_name in list_dir_xml:
       # print(file_name)
        #in_file = open(path + file_name)
        dom = xml.dom.minidom.parse(path+'/'+file_name)
        # 得到文档元素对象
        root = dom.documentElement
        #print(root)
        cc = dom.getElementsByTagName('filename')
        c1 = cc[0]
        c1=c1.firstChild.data
        list_image_id.append(c1)
    return list_image_id

def get_image_id_from_xml():
    ids=list_imag_ids(path=path,list_dir_xml=list_dir_xml)
    #randon_id =random.shuffle(image_ids)
    # print(randon_id)
    # print(image_ids)
    # ids = list(range(1,4981))
    # print(ids)
    print(len(ids))
    random.shuffle(ids)
    train = ids[:4480]
    test = ids[4480:]
    dataset = [train, test]
    sets=[('plate_train'), ('plate_test')]
    k = 0
    for image_set in dataset:
        subset_name = sets[k]
        k += 1
        image_ids = open('%s.txt'%(subset_name), 'w')
        for i in range(len(image_set)):
            image_ids.write('%s\n'%(image_set[i]))
        image_ids.close()

# 打开xml文档

#
# im_id = image_id()
# print(im_id)
# #print(im_id)

#方法1函数调用
#get_image_id_from_xml()

#方法2

def get_image_id_from_image():
    """
    :param path: 文件所在的地址的目录（相对或者绝对文件都可）
    :param list_dir_xml:
    :return: 文件列表组成的图片文件名 id
    # 使用 os.path.splitext(file)[0] 可获得 文件名 。
    # 使用 os.path.splitext(file)[-1] 可获得以 . 开头的 文件后缀名 。
    """
    Image_IDs=[]
    xml_list_filename = image_id_list()
    for filename in xml_list_filename:
        image_id=os.path.splitext(filename)[0]
        Image_IDs.append(image_id)
    #print(Image_IDs)
    return Image_IDs

def get_train_test_txtfile(ids):
    random.shuffle(ids)
    train = ids[:4480]
    test = ids[4480:]
    dataset = [train, test]
    sets = [('plate_train'), ('plate_test')]
    k = 0
    for image_set in dataset:
        subset_name = sets[k]
        k += 1
        image_ids = open('%s.txt' % (subset_name), 'w')
        for i in range(len(image_set)):
            image_ids.write('%s\n' % (image_set[i]))
        image_ids.close()

#方法2 函数调用方法
ids=get_image_id_from_image()
get_train_test_txtfile(ids)
#print(iamge_ids)
