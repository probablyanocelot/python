from ctypes import *

print(windll.kernel32)
print(cdll.msvcrt)
libc = cdll.msvcrt


# accessing functions from loaded dlls
print(libc.printf)
print(windll.kernel32.GetModuleHandleA)

'''Note that win32 system dlls like kernel32 and user32 often export ANSI as well as UNICODE versions of a function. The UNICODE version is exported with an W appended to the name, while the ANSI version is exported with an A appended to the name. The win32 GetModuleHandle function, which returns a module handle for a given module name, has the following C prototype, and a macro is used to expose one of them as GetModuleHandle depending on whether UNICODE is defined or not:'''
# ANSI version
#   HMODULE GetModuleHandleA(LPCSTR lpModuleName);
# UNICODE version
#   HMODULE GetModuleHandleW(LPCWSTR lpModuleName);

'''Sometimes, dlls export functions with names which aren’t valid Python identifiers, like "??2@YAPAXI@Z". In this case you have to use getattr() to retrieve the function:'''
getattr(cdll.msvcrt, "??2@YAPAXI@Z")