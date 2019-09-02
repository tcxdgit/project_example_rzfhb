# coding:utf-8
"""
提取每年的关键词
算法：TF-IDF
"""
import sys
import os
sys.path.append('../')
import jieba.analyse

topK = 20

home = '.'

# 加载停用词
jieba.analyse.set_stop_words("./stop_words.txt")

# 输出分析结果
f_out = open(os.path.join(home, 'yearly_keywords.txt'), 'w', encoding='utf-8')

for dirpath, dirnames, filenames in os.walk(home):

    print(dirpath)
    content = ''

    for filename in filenames:
        if filename.endswith(".md") and 'README.md' not in filename and 'SUMMARY.md' not in filename and 'R&D.md' not in filename:
            # print(filename)

            dir_file = os.path.join(dirpath, filename)

            tmp_content = open(dir_file, 'rb').read()
            content += str(tmp_content, encoding='utf-8')

    if content:
        tags = jieba.analyse.extract_tags(content, topK=topK)

        print(",".join(tags))
        print('\n')
        f_out.write(dirpath + '\n')
        f_out.write(",".join(tags) + '\n\n')

f_out.close()

