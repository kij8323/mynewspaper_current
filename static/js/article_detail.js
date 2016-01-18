
$(document).ready(function(){
  $(".weiboshare").mouseenter(function(){
      $(this).css("background-color","#f63756");
  });
  $(".weiboshare").mouseleave(function(){
      $(this).css("background-color"," #fafafa");
  });
  $(".weichatshare").mouseenter(function(){
      $(this).css("background-color","#46BC45");
  });
  $(".weichatshare").mouseleave(function(){
      $(this).css("background-color","#fafafa");
  });
  $(".qqzoneshare").mouseenter(function(){
      $(this).css("background-color","#EFDC11");
  });
  $(".qqzoneshare").mouseleave(function(){
      $(this).css("background-color","#fafafa");
  });
});


$(function(){
  $('.btn-dp').click(function(){
    $(this).next(".form-comment-reply").fadeToggle();
  })
});


