#!/usr/bin/env python
# encoding:utf-8
# cython: language_level=3
from loguru import logger
import requests
import json


async def login(account, password):
    logger.info("[BFF登录] APP执行参数为: {account} {password}", account=account, password=password)

    headers = {'Content-Type': 'application/json;charset=UTF-8'}

    try:
        r = requests.post(
            url="http://172.16.1.102:9000/api/v1/cdm/public/login",
            data=json.dumps({
                "account": account,
                "password": password,  # TODO：要加密
                "captchaId": "NOreCAPTCHA",
                "captchaCode": "NOreCAPTCHA",
            }),
            headers=headers,
        )
    except Exception as e:
        logger.error("[BFF登录] 登录失败:{e}", e=e)
        return {"status": 2, "result": "BFF登录失败:"+str(e)}

    return {"status": 0, "result": r.json()["data"]["token"]}
