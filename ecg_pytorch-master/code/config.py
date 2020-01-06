# -*- coding: utf-8 -*-

import os
class Config:
    # for data_process.py
    root = './data'
    data_root='./user_data'
    pre_root='./predition_result'
    train_dir = os.path.join(root, 'hf_round2_train')
    trainA_dir=os.path.join(root, 'testA')
    test_dir = os.path.join(root, 'testB_noDup_rename')
    train_label = os.path.join(root, 'hf_round2_train.txt')
    trainA_label=os.path.join(root, 'hefei_round1_ansA_20191008.txt')
    test_label = os.path.join(root, 'hf_round1_subB.txt')
    arrythmia = os.path.join(root, 'hf_round2_arrythmia.txt')
    train_data = os.path.join(data_root, 'train.pth')

    # for train
    #训练的模型名称
    model_name = 'ResNeXt29_4x64d'
    #在第几个epoch进行到下一个state,调整lr
    stage_epoch = [32,48,64,96]
    #训练时的batch大小
    batch_size =16
    #label的类别数
    num_classes = 34
    #最大训练多少个epoch
    max_epoch = 128
    #目标的采样长度
    target_point_num = 4096
    #保存模型的文件夹
    ckpt = 'ckpt'
    #保存提交文件的文件夹
    sub_dir = pre_root
    #初始的学习率
    lr = 1e-3
    #保存模型当前epoch的权重
    current_w = 'current_w.pth'
    #保存最佳的权重
    best_w = 'best_w.pth'
    # 学习率衰减 lr/=lr_decay
    lr_decay = 5

    #for test
    temp_dir=os.path.join(root,'temp')


config = Config()
