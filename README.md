# IssueTree-demo
IssueTree 오류 메시지 파싱 테스트용 레포지토리

## 에러 메시지 파싱 
1. DTO에 @Data 를 안붙이고 POST 요청을 보낼 시 
```
2024-02-13T12:53:20.036+09:00  WARN 10800 --- [nio-8080-exec-1] .w.s.m.s.DefaultHandlerExceptionResolver : Resolved [org.springframework.web.HttpMediaTypeNotAcceptableException: No acceptable representation]
```
* 오류 발생 위치 파싱 불가능 (사유: 에러 메시지에 존재하지 않음)

2. package 경로명 잘못 입력시 
```
C:\Users\user\Desktop\휴학\IssueTree-demo\demo\src\main\java\com\example\demo\controller\MemberController.java:4: error: package com.example.demo.service does not exist
import com.example.demo.service.MemberService;
                               ^
``` 
```
C:\Users\user\Desktop\휴학\IssueTree-demo\demo\src\main\java\com\example\demo\controller\MemberController.java:14: error: cannot find symbol
    private final MemberService memberService;
                  ^
  symbol:   class MemberService
  location: class MemberController
```
* 오류 발생 위치 파싱 가능 