# BUPT APIs

A lightweight Python library containing several API endpoints for Beijing University of Posts and Telecommunications (BUPT).

> [!IMPORTANT]
> This library is provided only for BUPT students for on-campus use. The author is not responsible for any consequences, damages, or issues arising from abuse or misuse of this software.

## Installation

```bash
pip install buptapis
```

## Usage

```python
from buptapis import BUPTAPI

# Get CAS Login URL
print(BUPTAPI.CAS.LOGIN)  # "https://auth.bupt.edu.cn/authserver/login"
```

## Available Modules

- [CAS](https://auth.bupt.edu.cn/authserver/login)
- [UC](https://uc.bupt.edu.cn/#/user/pc/index)
- [UCloud](https://ucloud.bupt.edu.cn/)
- [Electric](https://app.bupt.edu.cn/buptdf/wap/default/chong/)
