# -*- coding:utf-8 -*-
#匹配到语料库
import glob
import json
datas = glob.glob("E:/nanoGPT/chinese-poetry-master/全唐诗/poet.tang*json")
#处理数据
for data in datas:
    with open(data, 'r', encoding='utf-8') as fp:  #打开文本
        tangshi = json.load(fp)   #读取文本
        for each_shi in tangshi:
            # print(each_shi["paragraphs"])
            if len(each_shi["paragraphs"]) == 2 and len(each_shi["paragraphs"][0]) == 12 and len(each_shi["paragraphs"][1]) == 12:
                with open("E:/nanoGPT/data/Poetry/portey.txt", "a", encoding= 'utf-8') as f:
                    f.write("".join(each_shi["paragraphs"]))
                    f.write("\n")

