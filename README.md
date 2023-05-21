<B>電話番号取得業務</B><br>
<br>
indeed（https://jp.indeed.com/ ）で求人を掲載している企業の電話番号のリスト取得案件
<br>
<br>
<B>メインのコードはscraping.py</B>
<br>
流れとして，<br>
https://jp.indeed.com/ にアクセス
任意の検索でヒットした企業をリスト化<br>
その企業名をhttps://biz-maps.com/ で検索
ヒットしてその企業のURLが掲載されていれば，
そのURLに飛んで電話番号取得<br>
無ければ，https://www.jpnumber.com/ で検索して電話番号取得<br>
<br>
このコードはまずindeedから企業名のスクレイピングをおこなっているが，
indeedでのスクレイピングが禁止だから
indeedでのスクレイピングは控えたほうがいいやろなあ．．．<br>
スクレイピング禁止されて，スクリプトの実行ができなくなることを避けるために，
https://www.proxynova.com/proxy-server-list/ で取得した無料のプロキシを経由してindeedにアクセスするスクリプトも書いた．(proxy_get.py)<br>
（まあ，あんまりよろしくないやろうなあ．．．）<br>
<br>
今のところ，プロキシのIPコードに直打ちせなあかんけど無料プロキシサイトをスクレイピングして，使えるプロキシと使えないプロキシ判断する，自動判断スクリプト追加してもいいなあ．．
<br>
<br>
duplication_delete.pyは取得できた電話番号に重複があれば，それを消すスクリプト