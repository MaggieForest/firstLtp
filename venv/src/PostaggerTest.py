# -- coding: utf-8 --**
#测试词性标注 - Postagger
LTP_DATA_DIR = 'F:/zou/LTP/ltp_data/ltp_data' #v3.3.1同样报错模型未加载,采用v3.4.0
import os
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`

from pyltp import Postagger
postagger = Postagger() # 初始化实例
postagger.load(pos_model_path)  # 加载模型

words = ['欧几里得', '是', '西元前', '三', '世纪', '的', '希腊', '数学家', '。']
postags = postagger.postag(words)  # 词性标注

for i in range(len(words)):
    print words[i],'(',
    print postags[i],')',
postagger.release()  # 释放模型