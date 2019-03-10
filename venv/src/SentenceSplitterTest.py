# -- coding: utf-8 --**

# LTP_DATA_DIR = '/Users/dyh/NLP/ltp_data'
#LTP_DATA_DIR = 'F:/zou/LTP/ltp_data/ltp_data_v3.3.1'
#par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`
#ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型路径，模型名称为`pos.model`
#pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
#cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为‘cws.model’

#测试分句使用-SentenceSplitter
from pyltp import SentenceSplitter
sentence = SentenceSplitter.split('测试分句，这是分句1。这是分句2。这个是，分句3。')
for i in range(len(sentence)):
    print i+1,':',sentence[i]

