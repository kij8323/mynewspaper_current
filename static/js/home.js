
$(document).ready(function(){
  $(".weiboshare").mouseenter(function(){
      $(this).css("background-position","0 -76px");
  });
  $(".weiboshare").mouseleave(function(){
      $(this).css("background-position","0 -38px");
  });
  $(".weichatshare").mouseenter(function(){
      $(this).css("background-position","-37px -76px");
  });
  $(".weichatshare").mouseleave(function(){
      $(this).css("background-position","-37px -37px");
  });
  $(".qqzoneshare").mouseenter(function(){
      $(this).css("background-position","-76px -76px");
  });
  $(".qqzoneshare").mouseleave(function(){
      $(this).css("background-position","-76px -37px");
  });
});


