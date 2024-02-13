package com.example.demo.domain;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Entity
@Getter
@Setter
public class Member {
    @Id
    @GeneratedValue
    @Column(name="member_id") //컬럼명 지정 (안하면 그냥 id됨)
    private Long id;
    private String name;

}