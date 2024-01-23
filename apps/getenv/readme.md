## APP 说明

## 动作列表

### 接口调用

**参数：**

| 参数               | 类型  |  必填   | 备注                         |
|------------------| ----  |  ----  |----------------------------|
| **access_token** | text | `是` | access_token               |
| **url**          | text | `是` | 接口URL(用:name标识PATH参数)      |
| **method**       | text | `是` | 接口类型，GET/PUT/POST/DELETE   |
| **path_params**  | text | `是` | PATH参数赋值，JSON dict string  |
| **query_params** | text | `是` | QUERY参数赋值，JSON dict string |
| **json_params**  | text | `是` | BODY参数赋值，JSON string       |

**返回值：**

```
# 正常
{'errcode': 0, 'errmsg': 'ok'}
```
