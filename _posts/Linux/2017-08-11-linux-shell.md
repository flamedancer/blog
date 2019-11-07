---
layout: post 
title: shell 
categories: [linux]
---

----
#####  -----1  #####

1. `file cmd` 查看文件类型  
1. `*` 和 `.` 的区别：`*`是正则表达式匹配所有当前目录下所有文件，`.`只是代表当前文件夹。 
1.   所以 `ls *`  和 `ls .` 可以显示当前目录文件 但只能  `for f in *` 而不能 `for f in .`   
1. `read val` 可以读取输入赋值给 val  

----
#####  -----2 特殊变量  #####

$IFS | $0 | $# | $$ | $* | $@
-----|----|----|----|----|---
参数间隔符 | 执行文件名 | argc | pid | argv (join by $IFS) | argv (join by " ")


----
#####  -----3 Boolean check  #####

1. test EXP   [ EXP ]  返回的估计是一个 exit_status 之类的示例，所有的命令和sh都是返回这样一种类型。
   所以  if test echo 'ok'  不会报错。
2. 要正确记住 -nzfdrwxgue 这几个判断options 的含义
3. 比较符 eq 和 == ， ne 和 != 貌似是等价的
4. 比较符 不用 < , > 而用 lt  gt 是 因为 <  > 已近被用为 重定向符


----
#####  -----4 流程控制语句  #####
* if  EXP; then  EXP; elif EXP; then EXP; else  EXP; fi
* for  EXP in  EXP; do  EXP; done
* while  EXP; do  EXP; done
* until  EXP; do  EXP; done
* case  EXP in    EXP)   EXP;; esac 


#####  -----5 function  #####
>
We can make functions return numeric values using the return command.
The usual way to make func- tions return strings is for the function
to store the string in a variable, which can then be used after the
function finishes. Alternatively, you can echo a string and catch the
result

1. return 语句参数只能为数字  0 代表 true  非0 为false 
2. funciotn 应该也是最后返回一个 exit_status之类的类型  , 默认为最后一天语句的return值 
3. linux 下的命令结果都是输出到标准输出的, 一般获得的写法都像这样 result=$(grep 'xxx' yy.txt), 
   所以用函数用最后一行echo来提供输出结果

```
# output:  ok
#       :
f() {
    return 0
}
if f
then
    echo ok
fi
fr="$(f)"
echo $fr

# output:  ok
#       :  0 
f() {
    echo 0
}
if f
then
    echo ok
fi
fr="$(f)"
echo $fr

# error: return: sdf: numeric argument required
f() {
    return "sdf"
}
f
```


#####  -----6 commands  #####
1.  `.` 点号操作符。类似 C #include 语句。执行外部文件，不会新启进程, 而是在当前进程执行，所以会改变当前作用域变量。
2. `exec` the typical use is to replace the current shell with a diffrent program. 直接变成另外一个程序！
3. `:` 类似python里的pass 空语句。例如 `: ${name:=gc}` (是不是用 `name=${name:=gc} 更明了呢).
4. `eval` 和 python一样，执行字符串代表的语句. 
5. `exit`  exit 0  成功   exit 非0 失败
6. `export 变量名`  使所有子进程共享此变量名. 但不会影响父程序变量.
7. `expr` 同 $((...)) 数学计算. 字符串为shell的基准类型，执行 s=$s+1 不能进行数学计算.
8. `set` 设置$*的值。 
9. `shift` 左出栈 $*. 
10. `trap` 信号触发器 trap command signal
11. `unset` 删除一个变量或函数 很 set 没半毛线关系？
12. `find`  find [paths] [options] [tests] [action]
    * path 可写多个
    * tests 可用 '或且非'. 默认用 '且' 连接多个tests, 可用括号但需要 转义 因括号为特殊符号, 例如: 
      find . \(- newer xx.c -o -name "*.c" \) -type f -print
    * action除简单的 -print -ls 外重点记忆 -exec 用法。 （-ok 和 exec 类似只是需要用户确认）：
        1.  \; 结尾
        2. {} 代表当前要执行的文件
        3. 例如： -exec ls -l {} \;
13. `grep`   grep [options] PATTERN [FILES]
    1. 记住 -c -l -v 的含义
    2. grep 是以行为单位处理的
    3. 默认打印整行。-c 打印 文件名:行数 -l 打印 文件名 -v 打印 未命中的行
    4. 奇怪的正则表达 如：grep a[[:blank:]] word.txt 。 为什么不直接写成 grep a[:blank:] word.txt.
       因为 [ ] 有特殊的含义---选择性配置。所以要用双中括号。
   

##### 7. for 循环 列表 
循环数组时候一个关键点是要在数组后面增加 [@] 符号，表示获取数组全部内容，如果不加，则只能获取到第一个元素。
也可以通过下标的方式获取数组元素  array[index]
```shell
ips=('192.168.149.160' '192.168.149.161' '192.168.149.162')
for ip in ${ips[@]}
do
echo ${ip}
done

```
    

