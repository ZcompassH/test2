昨天只在hub上建了仓库，今天才clone过来。
昨天没写，所以从day 2开始

.gitignore的规则：
你想忽略	     规则	                 说明
某个文件	        my_secret.txt  	     不管在哪个子目录，同名都忽略
只忽略根目录那个	/my_secret.txt 	       开头加 / = 只认仓库根目录
所有同类文件	   *.pem	              任何以 .pem 结尾的文件（* = 任意字符）
整个文件夹	        data/	              结尾加 / = 忽略这个目录及其全部内容
某目录下的文件	    notes/draft.md        带路径就按路径匹配
例外	          !keep_this.txt	      前面加 ! = 这条不要忽略

路径不要带空格


day3
了解了input、print（f、int、float、round（number,x）、print（f：.xf）

分隔符sep=和end=

定义函数def ，代码开头写def main():
                                 在这写代码，后面可以自己定义其他函数，最后只调用主函数，可实现颠倒顺序的效果
其实并非颠倒顺序，代码依旧由上到下执行，只不过主要内容变成了定义的main函数，最后所有定义走一遍再调用即可。