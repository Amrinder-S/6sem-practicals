#include <windows.h>

int main() {
    // Execute the system command "dir" without opening a command prompt window
    ShellExecute(NULL, "open", "cmd.exe", "/c start https://www.youtube.com/watch?v=Pg3szYXumaE", NULL, SW_HIDE);

    return 0;
}
