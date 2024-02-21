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
* 파싱 결과
	```
	File Path: C:\Users\user\Desktop\휴학\IssueTree-demo\demo\src\main\java\com\example\demo\controller\MemberController.java:4
	Error Message: package com.example.demo.service does not exist
	```

```
C:\Users\user\Desktop\휴학\IssueTree-demo\demo\src\main\java\com\example\demo\controller\MemberController.java:14: error: cannot find symbol
    private final MemberService memberService;
                  ^
  symbol:   class MemberService
  location: class MemberController
```
* 오류 발생 위치 파싱 가능 

3. java.lang.IllegalArgumentException 에러 
```
Servlet.service() for servlet [dispatcherServlet] in context with path [] threw exception [Request processing failed; nested exception is java.lang.IllegalArgumentException: Model has no value for key 'pageNumber'] with root cause
java.lang.IllegalArgumentException: Model has no value for key 'pageNumber'
	at org.springframework.web.servlet.view.RedirectView.replaceUriTemplateVariables(RedirectView.java:387)
	at org.springframework.web.servlet.view.RedirectView.createTargetUrl(RedirectView.java:346)
	at org.springframework.web.servlet.view.RedirectView.renderMergedOutputModel(RedirectView.java:307)
	at org.springframework.web.servlet.view.AbstractView.render(AbstractView.java:316)
	at org.springframework.web.servlet.DispatcherServlet.render(DispatcherServlet.java:1400)
	at org.springframework.web.servlet.DispatcherServlet.processDispatchResult(DispatcherServlet.java:1145)
	at org.springframework.web.servlet.DispatcherServlet.doDispatch(DispatcherServlet.java:1084)
	at org.springframework.web.servlet.DispatcherServlet.doService(DispatcherServlet.java:963)
	at org.springframework.web.servlet.FrameworkServlet.processRequest(FrameworkServlet.java:1006)
	at org.springframework.web.servlet.FrameworkServlet.doGet(FrameworkServlet.java:898)
	at javax.servlet.http.HttpServlet.service(HttpServlet.java:655)
	at org.springframework.web.servlet.FrameworkServlet.service(FrameworkServlet.java:883)
	at javax.servlet.http.HttpServlet.service(HttpServlet.java:764)
	at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:227)
	at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
	at org.apache.tomcat.websocket.server.WsFilter.doFilter(WsFilter.java:53)
	at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
	at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
	at com.navercorp.lucy.security.xss.servletfilter.XssEscapeServletFilter.doFilter(XssEscapeServletFilter.java:36)
	at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
	at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
	at lfcp.arch.common.filter.SessionValidationFilter.doFilter(SessionValidationFilter.java:173)
	at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
	at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
	at lfcp.arch.common.filter.InboundFilter.doFilter(InboundFilter.java:148)
	at org.apache.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:189)
	at org.apache.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:327)
	at org.springframework.security.web.access.intercept.FilterSecurityInterceptor.invoke(FilterSecurityInterceptor.java:115)
	at org.springframework.security.web.access.intercept.FilterSecurityInterceptor.doFilter(FilterSecurityInterceptor.java:81)
	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:336)
	at org.springframework.security.web.access.ExceptionTranslationFilter.doFilter(ExceptionTranslationFilter.java:121)
	at org.springframework.security.web.access.ExceptionTranslationFilter.doFilter(ExceptionTranslationFilter.java:115)
	at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:336)
... 중략
```
* 참고글: https://goddaehee.tistory.com/323
* 아래와 같이 출력됨
  ![image](https://github.com/White-Long-tailed-Tit/IssueTree-demo/assets/65723420/b2ba1aee-9bac-4e3d-a104-c9ac90199530)

