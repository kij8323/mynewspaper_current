
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
  $(".search-tag").mouseenter(function(){
      $(this).css("background-color","#449d44");
      $(this).children("a").css("color","#fff");
  });
  $(".search-tag").mouseleave(function(){
      $(this).css("background-color","#CCF4D9");
      $(this).children("a").css("color","#449d44");
  });
 $("#morecomment-btn-block").mouseenter(function(){
      $(this).css("background-color","#f0f0f0");
  });
  $("#morecomment-btn-block").mouseleave(function(){
      $(this).css("background-color","white");
  });
 $(".articlecollection").mouseenter(function(){
      $(this).css("background-color","#3ca5f6");
      $(this).css("color","white");
  });
  $(".articlecollection").mouseleave(function(){
      $(this).css("background-color","#fafafa");
      $(this).css("color","#bbb");
  });
});



$(function(){
  $("body").on("click", '.btn-dp', function(){
    $(this).next(".form-comment-reply").fadeToggle();
  });
})