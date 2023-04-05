# dir()
# help()
import torch

print(dir(torch))
print(dir(torch.cuda.is_available))  # __ 开头和结尾是私有变量
print(help(torch.cuda.is_available))  # help 官方文档解释函数的作用
