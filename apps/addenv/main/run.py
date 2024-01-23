#!/usr/bin/env python
# encoding:utf-8
# cython: language_level=3
from loguru import logger
import requests
import json


async def cdm_api(access_token, api, params):
    logger.info(f"[CDM调用v2] APP执行参数为: {access_token} {api} {params}",
                access_token=access_token, api=api, params=params)

    if api == "获取虚拟化平台列表":
        url = "/api/v1/cdm/internal/env/vm"
        method = "GET"
    elif api == "添加虚拟化平台":
        url = "/api/v1/cdm/internal/env/vm"
        method = "POST"
    elif api == "获取定时策略列表":
        url = "/api/v1/cdm/internal/env/vm"
        method = "GET"
    elif api == "添加虚拟机备份任务":
        url = "/api/v1/cdm/internal/env/vm"
        method = "POST"
