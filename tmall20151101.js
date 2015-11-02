// ==UserScript==
// @name         tmall
// @namespace    http://your.homepage/
// @version      0.1
// @description  就自动狂点，然而并没有拿到过红包
// @author       You
// @match        https://www.tmall.com/wow/act/14700/*
// @grant        none
// ==/UserScript==

console.info("hehe");
function jq_work(){
    document.getElementById("voucherBtn").click();
    var s = document.getElementById("voucherBtn").innerHTML;
    if (s.includes("本时段已抢完")) {
        location.reload(true);
    }
    console.info("ddd");
    var timeout = parseInt(Math.random()*200+200);
    setTimeout(function(){
        jq_work();
    },timeout);
}

//$(document).ready(function(){
    console.info("begin");
    jq_work();
//});
