%macro pushd 0
    push rax
    push rbx
    push rcx
    push rdx
%endmacro

%macro popd 0
    pop rdx
    pop rcx
    pop rbx
    pop rax
%endmacro

%macro print 2
    pushd
    mov rax, 1
    mov rdi, 1
    mov rsi, %1
    mov rdx, %2
    syscall
    popd
%endmacro
%macro fdev 2
    pushd
    mov rax,%1
    mov rbx,%2
    mov ebp,10
    mov rcx,0
    xor rdx,rdx
    div rbx
    add rax,'0'
    mov [result], rax
    print result, 1
    mov rax,rdx
    mul ebp
    mov rcx,','
    mov [result], rcx
    print result, 1
    mov rcx,1
    jmp %%dev
%%dev:
    xor rdx,rdx
    div rbx
    add rax,'0'
    mov [result], rax
    print result, 1
    mov rax,rdx
    mul ebp
    cmp rcx,3
    jge %%end
    inc rcx
    cmp rax,0
    jg %%dev
%%end:
    popd
%endmacro
%macro dprint 0
    pushd
    mov rcx, 10
    mov rbx, 0
%%devide:
    xor rdx,rdx
    div rcx
    push rdx
    inc rbx
    cmp rax,0
    jne %%devide
%%digit:
    pop rax
    add rax, '0'
    mov [result], rax
    print result, 1
    dec rbx
    cmp rbx,0
    jg %%digit
    popd
%endmacro

section .text
global _start

_start:
    mov rbx,0
    mov al,0
    mov rdx,0
    jmp plusarr
minus:
    mov rdx,0
    mov cl,0
    sub cl,al
    mov al,cl
    mov rcx,'-'
    mov [result],rcx
    print result,1
    jmp end
changes:
    mov rdx,1
    sub al, y[rbx]
    inc rbx
    cmp rbx,lenx
    jge end
    jmp minusarr
plusarr:
    add al, x[rbx]
    inc rbx
    cmp rbx,lenx
    jl plusarr
    xor rbx,rbx
minusarr:
    cmp al,y[rbx]
    jb changes
    sub al, y[rbx]
    inc rbx
    cmp rbx,lenx
    jl minusarr
end:
    cmp rdx,0
    jg minus
    mov rdx,4
    mul rdx
    mov rdx,lenx
    mov [ans],al
    mov rax,[ans]
    fdev rax,rdx
    mov rax, 60
    xor rdi, rdi
    syscall
    
section .data
    x dd 5, 3, 2, 6, 1, 7, 4
    lenx equ $ - x
    y dd 0, 10, 1, 9, 2, 8, 5
    leny equ $ - y
    value1 dd 32223
    value2 dd 84628
    done db 'Done', 0xA, 0xD
    len equ $ - done
    newline db 0xA, 0xD
    nlen equ $ - newline

section .bss
    result resb 1
    ans resb 1 