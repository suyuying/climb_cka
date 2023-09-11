# climb_cka

主要是因為cka會特價,所以會每天去看他是否特價！
以下工具會用bs4去爬資料,請把自己的tg資料放到.env檔內
內容大致如下:
```commandline
tg_token=647xxxxx:xxxxx
chat_id=-409425xxxx
```

## 開始使用

這些說明將幫助您在本地機器上設置和運行項目。

### 先決條件

在開始之前，請確保您已經安裝了以下工具：

- [Python](https://www.python.org/downloads/)
- [pipenv](https://pipenv.pypa.io/en/latest/)

### 安裝

1. 複製庫並初始化submodule `tg`

   ```bash
   git clone https://github.com/suyuying/climb_cka.git
   cd climb_cka
   pipenv install
   pipenv shell
   cd tg/
   git submodule init
   git submodule update
   ```

2. 加入.env在最外層
3. 執行指令
    ```commandline
    pipenv shell
    python3 main.py
    ```
    
