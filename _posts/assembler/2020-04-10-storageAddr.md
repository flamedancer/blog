---
layout: post 
title: storageAddr 
categories: [assembler]
---

----
#####  -----1 and、or 指令  #####

1. `and`   :   `and al,11011111B`  转化为大写

   `or`:    `or al,001000000B` 转化为小写

----
#####  -----2 [bx+idata] #####

1. `[bx+idata]` :  ((ds)*16 + (bx)+idata)
2. 有多重写法注意下：`idata[bx]` `[bx].idata`

----
#####  -----3 寄存器 si、di、bp  #####

1. `si` `di` 功能上和`bx` 一样都具有寻址功能, 例如 `mov ax,[si]    mov ax, [di + 16]`
2. 不能拆分成两个字节寄存器
3. `[bx+si]` : ((dx)*16 + (bx) + (si))
4. `[bx+si+idata]` : ((dx)*16 + (bx) + (si) + idata)
5. 但是 `si` `di`不能同时出现在寻址[...]中
	- ❎`[si + di]`
	- ✅`[bx+si]`
	- ✅`[bx+di]`
6. 具体来，只有这四种组合是合法的
   - bx   si   
   - bx  di
   - bp si
   - bp di

7. `bp`和其他三个在寻址上的区别在于：默认`bp`寻址的段地址在`ss`中，而其它三个在`ds`中

​     

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
