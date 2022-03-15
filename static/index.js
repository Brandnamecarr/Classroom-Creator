$(document).ready(function(){
    $("button").click(function(){
      $.ajax({url: "server_time", success: function(result){
        $("#server-time").html(result);
        console.log(result);
      }});
    });
  });


console.log("here");