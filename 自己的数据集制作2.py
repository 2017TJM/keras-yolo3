import xml.etree.ElementTree as ET
from os import getcwd

#todo :在keras目录中新建Racoon_dataset数据集
#TODO：Racoon_dataset :
                 #todo:annotations
                       #todo:通过lableme标注好的数据集，注意是PascalVOC格式的XML文件
                 #todo:images 原始图像数据和用lableme标注的文件对应
                 #TODO：raccoon_classes.txt这个文件需要新建好和你的数据类别对应
#todo：通过运行 该代码即可获取四个文件
import random
import os
sets=[('plate_train'), ('plate_test')]

#classes = ["plate"]
classes=["plate","0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","J","K","L","M","N","P","Q","R","S","T","U","V","W","X","Y","Z","澳","川","鄂","甘","赣","港","贵","桂","黑","沪","吉","冀","津","晋","京","警","辽","鲁","蒙","闽","宁","青","琼","陕","苏","皖","湘","新","学","渝","豫","粤","云","浙","藏"]


def convert_annotation(image_id, list_file):
    #需要扫描文件夹
    path ="data/voc/VOCdevkit/VOC2019/Annotations/"
    list_dir_xml=os.listdir(path)
    for file_name in list_dir_xml:
        print(file_name)
        in_file = open(path+file_name)
        tree=ET.parse(in_file)
        root = tree.getroot()

        for obj in root.iter('object'):
            difficult = obj.find('difficult').text
            cls = obj.find('name').text
            if cls not in classes or int(difficult)==1:
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
            list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()   # current working path

# 1 arrange train, val, test dataset:
#图像ID要改变 首先要获得图像id




# ids = list(range(1,4981))
# random.shuffle(ids)
# train = ids[:4480]
# test = ids[4480:]
# dataset = [train, test]
# k = 0
# for image_set in dataset:
#     subset_name = sets[k]
#     k += 1
#     image_ids = open('data/%s.txt'%(subset_name), 'w')
#     for i in range(len(image_set)):
#         image_ids.write('%d\n'%(image_set[i]))
#     image_ids.close()


# 2 produce train, val, test data:
for image_set in sets:
    image_ids = open('data/%s.txt'%(image_set)).read().strip().split()
    list_file = open('data/%s_data.txt'%(image_set), 'w')
    for image_id in image_ids:
        list_file.write('data/voc/VOCdevkit/VOC2019/JPEGImages/%s.jpg'%(image_id))
        convert_annotation(image_id, list_file)
        list_file.write('\n')
    list_file.close()


print("Sucess finished the  task")

