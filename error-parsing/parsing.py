import re


str1=r'''C:\Users\user\Desktop\휴학\IssueTree-demo\demo\src\main\java\com\example\demo\controller\MemberController.java:4: error: package com.example.demo.service does not exist
import com.example.demo.service.MemberService;'''

str2=r'''
C:\Users\user\Desktop\휴학\IssueTree-demo\demo\src\main\java\com\example\demo\controller\MemberController.java:14: error: cannot find symbol
    private final MemberService memberService;
                  ^
  symbol:   class MemberService
  location: class MemberController'''

def parsing_1(s):
    s=s.replace('^','')
    # 파일 경로 추출
    match = re.search(r'(.+\.java):(\d+)', s)
    if match:
        file_path = match.group(1) + ':' + match.group(2)
    else:
        file_path = None

    # 에러 메시지 추출
    error_message = re.search(r'error: (.+)', s)
    if error_message:
        error_message = error_message.group(1)
    else:
        error_message = None

    print("File Path:", file_path)
    print("Error Message:", error_message)


parsing_1(str1)
parsing_1(str2)