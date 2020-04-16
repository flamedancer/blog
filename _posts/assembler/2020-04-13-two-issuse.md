---
layout: post 
title: twoIssuse 
categories: [assembler]
---

----
#####  -----1 两个基本问题  #####

1. 两个基本问题 ：
  * 处理的数据在什么地方
  * 要处理的数据有多长
2. 描述性符好
	* reg (register)普通寄存器，eg.    ax,  bx,  al, bl, sp, si, di....
	* seg(segment register) 段寄存器，eg.  ds,ss,cs,es

----
#####  -----2 处理的数据在什么地方#####

1. 数据的位置
	* 立即数   idata
	* 寄存器 reg  sreg
	* 段地址SA组合偏移地址EA  :          (ereg) * 16 + (reg) + (reg) + idata
2. 寻址方式
	* 直接寻址  [idata]
	* 寄存器间接寻址 [bx]
	* 寄存器相对寻址 [bx + idata]
	* 基指变址寻址 [bx + si]
	* 相对基指变址寻址 [bx + si + idata]

----
#####  -----3 要处理的数据有多长  #####

1. 通过寄存器名字指明 数据长度
	* mov ax, 1   字操作
	* mov al, bl   字节操作
2. 在没有寄存器名字的情况下，用操作符   word   ptr  或  byte ptr   （ptr : put to register ?）
	 指明是字操作还是字节操作
   - mov word ptr ds:[0], 1  
   - inc byte ptr [bx]
   
----
#####  -----4  用内存临时存储寄存器内容  #####

1. 将 每行data前四个字符变大写
```assembly
   assume cs:codesg,ss:stacksg,ds:datasg
   
   stacksg segment
       dw 0,0,0,0,0,0,0,0
   stacksg ends
   
   datasg segment
       db '1. display      '
       db '2. brows        '
       db '3. replace      '
       db '4. modify       '
       db '5. shift        '
   datasg ends
   
   codesg segment
     start:
       mov ax,datasg
       mov ds,ax
       mov ax,stacksg
       mov ss,ax
       mov sp,16
   
       mov cx,5
       mov bx,3
   s0:
       push cx
       mov cx,4
   s1:
       mov al,[bx]
       and al,11011111B
       mov [bx],al
       inc bx
       loop s1
   
       pop cx
       add bx,12
       loop s0
   
       mov ax,4c00h
       int 21h
   
   codesg ends
   
   
   end start
```
----
#####  -----5 指令div  #####

1. div  除法指令
2. 分两种情况
   1. 除数为 8 位:
      * 被除数  - 16位，用 ax 存放
        * 除数 -  8位，在reg 或 内存中
      * 商 - 8位，al 存放
      * 余数 - 8位，ah 存放   
   2. 除数为32位：
      * 被除数 - 32位， 用 dx 存高16位，ax存低16位
      * 除数 - 16位，在reg 或 内存中
      * 商 - 16位，ax存放
      * 余数 - 8位，dx 存放

3. 高位存余，低位存商

