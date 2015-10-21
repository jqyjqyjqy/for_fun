// ==UserScript==
// @name         pandaTV
// @namespace    http://your.homepage/
// @version      0.1
// @description  自动弹幕
// @author       JQ
// @match       http://www.panda.tv/room/*
// @grant        none
// ==/UserScript==
console.info("hehe");
function jq_work(){
    $("#chat_dispatch").val("爆爆爆" + parseInt(Math.random()*100+1));
    $("#live_wrapper > div.live-right-content > div.right-content-container > div.chat-tool-container > div > div > div.dispatch-btn").click();
    //var timeout = parseInt(Math.random()*10000+1000);
    setTimeout(function(){
        jq_work();
    },2000);
    //},timeout);
}

$(document).ready(function(){
    console.info("begin");
    jq_work();
});
