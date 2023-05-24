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
これが難しかった．そのサイトに行ってサイトマップ入手してURL全部行って電話番号取得するのも考えたけど，<br>
だいたいの企業はトップページか /company /about に電話番号が載っていた．<br>
そのページのページソースから電話番号の形式の文字列があればそれを取得<br>
最初は正規表現を使って電話番号を取得していたが，それでは電話番号っぽい並びの電話番号ではないものがしゅとくされてしまうから，<br>
力ずくで電話番号をしゅとくしている．
<br>
<br>
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
