import re


str1=r'''C:\Users\user\Desktop\휴학\IssueTree-demo\demo\src\main\java\com\example\demo\controller\MemberController.java:4: error: package com.example.demo.service does not exist
import com.example.demo.service.MemberService;'''

str2=r'''
C:\Users\user\Desktop\휴학\IssueTree-demo\demo\src\main\java\com\example\demo\controller\MemberController.java:14: error: cannot find symbol
    private final MemberService memberService;
                  ^
  symbol:   class MemberService
  location: class MemberController'''

str3 = r"""Servlet.service() for servlet [dispatcherServlet] in context with path [] threw exception [Request processing failed; nested exception is java.lang.IllegalArgumentException: Model has no value for key 'pageNumber'] with root cause
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
    at org.springframework.security.web.FilterChainProxy$VirtualFilterChain.doFilter(FilterChainProxy.java:336)"""

# 예외 메시지 추출
error_message = re.search(r'(?<=threw exception \[).*?(?=\])', str1)

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

def parsing_2(s):
    # 예외 메시지 추출
    error_message = re.search(r'(?<=threw exception \[).*?(?=\])', s)
    if error_message:
        error_message = error_message.group()
    else:
        error_message = None

    print("Error Message:", error_message)
    
parsing_1(str1)
parsing_1(str2)
parsing_2(str3)