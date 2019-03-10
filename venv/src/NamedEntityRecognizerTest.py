# -- coding: utf-8 --**
#命名实体识别测试 - NamedEntityRecognizer
LTP_DATA_DIR = 'F:/zou/LTP/ltp_data/ltp_data' #v3.3.1同样报错模型未加载,采用v3.4.0
import os
ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型路径，模型名称为`ner.model`

from pyltp import NamedEntityRecognizer
recognizer = NamedEntityRecognizer() # 初始化实例
recognizer.load(ner_model_path)  # 加载模型

words = ['欧几里得', '是', '西元前', '三', '世纪', '的', '希腊', '数学家', '。']
postags = ['nh', 'v', 'nt', 'm', 'n', 'u', 'ns', 'n', 'wp']
nertags = recognizer.recognize(words, postags)  # 命名实体识别

print ' '.join(nertags)
recognizer.release()  # 释放模型




#ltp命名实体类型为：人名（Nh），地名（Ns），机构名（Ni）；
#ltp采用BIESO标注体系。
#   B表示实体开始词，I表示实体中间词，
#   E表示实体结束词，S表示单独成实体，
#   O表示不构成实体。