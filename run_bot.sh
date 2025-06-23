#!/bin/bash

# 进入虚拟环境
source venv/bin/activate

# 从 .env 加载环境变量
export $(grep -v '^#' .env | xargs)

# 运行主程序
python main.py
