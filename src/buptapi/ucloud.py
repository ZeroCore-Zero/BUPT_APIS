from enum import StrEnum


class UCLOUD(StrEnum):
    LOGIN = "https://auth.bupt.edu.cn/authserver/login?service=https://ucloud.bupt.edu.cn"
    TOKEN = "https://apiucloud.bupt.edu.cn/ykt-basics/oauth/token"
    INFO = "https://apiucloud.bupt.edu.cn/ykt-basics/info"
    CURRENT = "https://apiucloud.bupt.edu.cn/ykt-site/base-term/current"
    USER = "https://apiucloud.bupt.edu.cn/ykt-basics/userroledomaindept/listByUserId"
