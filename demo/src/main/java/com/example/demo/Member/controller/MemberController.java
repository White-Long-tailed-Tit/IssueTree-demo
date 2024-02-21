package com.example.demo.Member.controller;

import com.example.demo.Member.domain.Member;
import com.example.demo.Member.service.MemberService;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;
import jakarta.validation.constraints.NotEmpty;

@RestController //@Controller + @ResponseBody
@RequiredArgsConstructor
public class MemberController {
    private final MemberService memberService;

    @PostMapping("/api/member/signin")
    public CreateMemberResponse saveMember(@RequestBody CreateMemberRequest request){
        Member member=new Member();
        member.setName(request.getName());

        Long id=memberService.join(member);
        return new CreateMemberResponse(id);
    }

    @GetMapping("/api/member/{id}")
    public DeleteMemberResponse deleteMemberV1(@PathVariable("id")Long id){
        memberService.delete(id);
        return new DeleteMemberResponse(id,"성공적으로 회원을 삭제했습니다");
    }


    @Data
    static class CreateMemberRequest{
        @NotEmpty
        private String name;
    }

    @Data
    static class CreateMemberResponse{
        private Long id;

        public CreateMemberResponse(Long id) {
            this.id = id;
        }
    }

    @Data
    @AllArgsConstructor
    static class DeleteMemberResponse{
        private Long id;
        private String msg;
    }
}
