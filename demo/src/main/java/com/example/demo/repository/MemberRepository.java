package com.example.demo.repository;


import com.example.demo.domain.Member;
import jakarta.persistence.EntityManager;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
@RequiredArgsConstructor
public class MemberRepository {

    private final EntityManager em;

    public Long save(Member member){
        em.persist(member); //persist하는 순간 영속성 컨텍스트 객체를 올림
        return member.getId();
    }

    public Member findOne(Long id){
        return em.find(Member.class, id); //member를 찾아서 반환해줌
    }

    public List<Member> findAll(){
        return em.createQuery("select m from Member m", Member.class)
                .getResultList();
    }

    public List<Member> findByName(String name){
        //이름으로 찾는 것
        return em.createQuery("select m from Member m where m.name=:name",Member.class)
                .setParameter("name",name)
                .getResultList();
    }

    public void deleteById(Long id){
        Member member=findOne(id);
        em.remove(member);
    }
}
