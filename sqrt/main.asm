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
    mov eax,[dig]
    mov ecx,2   
    div ecx
    xor edx,edx
    mov ebx,eax
    mov eax,[dig]
    div ebx
    xor edx,edx
    add eax,ebx
    div ecx
psqrt:
    xor edx,edx
    mov ebx,eax
    mov eax,[dig]
    div ebx
    xor edx,edx
    add eax,ebx
    div ecx
    xor edx,edx
    mov edx,ebx
    sub edx,eax
    cmp edx,1
    jge psqrt
    dprint
    mov rax, 60
    xor rdi, rdi
    syscall
    
section .data
    dig dd 289
    done db 'Done', 0xA, 0xD
    len equ $ - done
    newline db 0xA, 0xD
    nlen equ $ - newline

section .bss
    result resb 1