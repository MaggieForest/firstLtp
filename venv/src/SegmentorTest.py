# -- coding: utf-8 --**
#测试分词使用 - Segmentor
import os
LTP_DATA_DIR = 'F:/zou/LTP/ltp_data/ltp_data' #v3.3.1报错Segmentor: Model not loaded!，使用新版本模型v3.4.0运行成功
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为‘cws.‘
from pyltp import Segmentor
segmentor = Segmentor()  # 初始化实例
segmentor.load(cws_model_path)  # 加载模型
words = segmentor.segment('欧几里得是西元前三世纪的希腊数学家。')  # 分词
print ' '.join(words)
segmentor.release()  # 释放模型，但是人名并未识别，以下方法可以识别出人名



path_name = 'F:/zou/LTP/Names-Corpus-master/Names-Corpus/testName.txt'
segmentor = Segmentor()  # 初始化实例
segmentor.load_with_lexicon(cws_model_path, path_name) # 加载模型地址，参数lexicon是自定义词典的文件路径
words = segmentor.segment('欧几里得是西元前三世纪的希腊数学家。')
print ' '.join(words)
segmentor.release()




