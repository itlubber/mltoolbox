# 机器学习模型工具箱

机器学习模型工具箱，提供自动化模型报告输出、超参数调优、代价敏感学习、不平衡数据集处理等功能，快速上手，解放生产力


# 项目结构

```shell
```shell
> tree -I __init__.py

.
├── README.md                       # 说明文档
├── requirements.txt                # 依赖文件
├── mltoolbox                       # 包文件
│   ├── cv                          # 多折交叉验证相关方法
│   ├── eda                         # 数据分析相关方法
│   │   └── auto                    # 自动 EDA 相关方法
│   ├── explainer                   # 模型解释性
│   ├── models                      # 机器学习模型
│   │   ├── auto                    # 自动机器学习相关方法
│   │   ├── ensemble                # 集成学习
│   │   │   ├── bagging
│   │   │   ├── blending
│   │   │   ├── boosting
│   │   │   └── stacking
│   │   ├── classification          # 分类器
│   │   ├── regression              # 回归器
│   │   ├── ranking                 # 排序模型
│   │   └── tricks                  # 模型训练 tricks 合集
│   ├── optimizer                   # 超参数搜索器
│   ├── sampler                     # 采样器
│   ├── selector                    # 选择器
│   ├── transformer                 # 转换器
│   └── utils                       # 公共方法
│       ├── logger.py               # 日志方法
│       ├── setter.py               # 配置器
│       ├── reader.py               # 读取器
│       └── writer.py               # 写入器
├── LICENSE                         # 开源许可
├── MANIFEST.in                     # 打包文件设置
└── setup.py                        # 打包脚本

22 directories, 9 files
```


# 环境配置

