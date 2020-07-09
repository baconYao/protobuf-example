#!/usr/bin/env bash

# 產生 simple protocol buffer 的 python code
# -I: proto 文件的目錄位置
# --python_out: 產生的 python code 的位置
# simple/simple.proto: 要被產生的 protobuf 的所在地
# 最後會產生 simple/simple_pb2.py
protoc -I=simple/ --python_out=simple/ simple/simple.proto

# 產生 enum protocol buffer 的 python code
protoc -I=enum/ --python_out=enum/ enum/enum_example.proto
