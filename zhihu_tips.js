// 泼油猴 greaseonkey 
// ==UserScript==
// @auther      jq
// @name        zhihu 页面书签
// @namespace   http://www.zhihu.com/question/
// @description 显示出书签链接，点击加书签
// @include     http://www.zhihu.com/question/*
// @version     1
// @grant       none
// ==/UserScript==

$(".zg-anchor-hidden.ac").css('display','none');
$(".zg-anchor-hidden").css('width','500px');
$(".zg-anchor-hidden").css('top','-5px');
$(".zg-anchor-hidden").css('font-size','15px');
$(".zg-anchor-hidden").html('连我连我连我');
$(".zg-anchor-hidden").click(function(){
  var href_val = $(this).attr('name');
  $(this).attr('href',"#"+href_val);
});
