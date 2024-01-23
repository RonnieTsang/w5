#!/usr/bin/env python
# encoding:utf-8
# cython: language_level=3
from loguru import logger
import requests
import json


async def cdm_api(access_token, url, method, path_params, query_params, json_params):
    logger.info(f"[CDM调用] APP执行参数为: {access_token} {url} {method}",
                access_token=access_token, url=url, method=method)

    endpoint = "http://172.16.1.102:9000"
    if method.lower() == "get":
        try:
            headers = {
                'Authorization': 'Bearer {token}'.format(token=access_token)
            }
            url = "{endpoint}{url}?{query}".format(endpoint=endpoint, url=url, query=query_params)
            r = requests.get(url=url, headers=headers)
        except Exception as e:
            logger.error("[CDM调用] 请求API失败:{e}", e=e)
            return {"status": 2, "result": "CDM调用失败:" + str(e)}

        return {"status": 0, "result": r.json()}
    elif method.lower() == "post":
        try:
            headers = {
                'Content-Type': 'application/json;charset=UTF-8',
                'Authorization': 'access_token {token}'.format(token=access_token)
            }
            r = requests.post(
                url="{endpoint}{url}".format(endpoint=endpoint, url=url),
                data=json_params,
                headers=headers,
            )
        except Exception as e:
            logger.error("[CDM调用] 请求API失败:{e}", e=e)
            return {"status": 2, "result": "CDM调用失败:" + str(e)}

        return {"status": 0, "result": r.json()}
