@echo off

rem This file is UTF-8 encoded, so we need to update the current code page while executing it
for /f "tokens=2 delims=:." %%a in ('"%SystemRoot%\System32\chcp.com"') do (
    set _OLD_CODEPAGE=%%a
)
if defined _OLD_CODEPAGE (
    "%SystemRoot%\System32\chcp.com" 65001 > nul
)

set VIRTUAL_ENV=D:\Programs-miscellaneous\TwitterFeed\venv

if not defined PROMPT set PROMPT=$P$G

if defined _OLD_VIRTUAL_PROMPT set PROMPT=%_OLD_VIRTUAL_PROMPT%
if defined _OLD_VIRTUAL_PYTHONHOME set PYTHONHOME=%_OLD_VIRTUAL_PYTHONHOME%

set _OLD_VIRTUAL_PROMPT=%PROMPT%
set PROMPT=(venv) %PROMPT%

if defined PYTHONHOME set _OLD_VIRTUAL_PYTHONHOME=%PYTHONHOME%
set PYTHONHOME=

if defined _OLD_VIRTUAL_PATH set PATH=%_OLD_VIRTUAL_PATH%
if not defined _OLD_VIRTUAL_PATH set _OLD_VIRTUAL_PATH=%PATH%

set PATH=%VIRTUAL_ENV%\Scripts;%PATH%

set CONSUMER_KEY="fPt4a7istHIo0kh8iS3PhWHK6"
set CONSUMER_SECRET="vu7nAlCm3ByaXTln766Ob8O3FMFtF8wzwanugwdRqFkjSRUMF7"
set BEARER_TOKEN="AAAAAAAAAAAAAAAAAAAAALgXOAEAAAAAmKlAQ3YvSv03QvA5pPI90GgOwoo%3D6SpUWP9bMI3xpS3rmGmeSUr7PX926p9uphObSdi40EHphSvLgG"
set ACCESS_TOKEN="1125419842389954560-wbf9LThY910s44iKbXk0n7aLudJhOJ"
set ACCESS_SECRET="8CK1YrJE4knhS027Tx83zxoHdmyQNuxYnmUOa7WsGXZ6J"

:END
if defined _OLD_CODEPAGE (
    "%SystemRoot%\System32\chcp.com" %_OLD_CODEPAGE% > nul
    set _OLD_CODEPAGE=
)
