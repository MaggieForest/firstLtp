# -- coding: utf-8 --**
#依存句法分析测试 - Parser
LTP_DATA_DIR = 'F:/zou/LTP/ltp_data/ltp_data' #v3.3.1同样报错模型未加载,采用v3.4.0
import os
par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`

from pyltp import Parser
parser = Parser() # 初始化实例
parser.load(par_model_path)  # 加载模型

words = ['欧几里得', '是', '西元前', '三', '世纪', '的', '希腊', '数学家', '。']
postags = ['nh', 'v', 'nt', 'm', 'n', 'u', 'ns', 'n', 'wp']
arcs = parser.parse(words, postags)  # 句法分析

rely_id = [arc.head for arc in arcs]    # 提取依存父节点id
relation = [arc.relation for arc in arcs]   # 提取依存关系
heads = ['Root' if id == 0 else words[id-1] for id in rely_id]  # 匹配依存父节点词语

for i in range(len(words)):
    print relation[i] + '(' + words[i] + ', ' + heads[i] + ')'

parser.release()  # 释放模型


#主谓关系	SBV	subject-verb	我送她一束花 (我 <– 送)
#动宾关系	VOB	直接宾语，verb-object	我送她一束花 (送 –> 花)
#间宾关系	IOB	间接宾语，indirect-object	我送她一束花 (送 –> 她)
#前置宾语	FOB	前置宾语，fronting-object	他什么书都读 (书 <– 读)
#兼语	DBL	double	他请我吃饭 (请 –> 我)
#定中关系	ATT	attribute	红苹果 (红 <– 苹果)
#状中结构	ADV	adverbial	非常美丽 (非常 <– 美丽)
#动补结构	CMP	complement	做完了作业 (做 –> 完)
#并列关系	COO	coordinate	大山和大海 (大山 –> 大海)
#介宾关系	POB	preposition-object	在贸易区内 (在 –> 内)
#左附加关系	LAD	left adjunct	大山和大海 (和 <– 大海)
#右附加关系	RAD	right adjunct	孩子们 (孩子 –> 们)
#独立结构	IS	independent structure	两个单句在结构上彼此独立
#核心关系	HED	head	指整个句子的核心