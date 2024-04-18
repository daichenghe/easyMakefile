set ROOT_PATH=%~dp0

echo %ROOT_PATH%

DEL /F/S/Q	*.o
DEL /F/S/Q	*.d
timeout /t 15