// Server-Time test function.
$(document).ready(function(){
    $("button").click(function(){
      $.ajax({url: "server_time", success: function(result){
        $("#server-time").html(result);
        console.log(result);
      }});
    });
  });

// will display the File-Upload Option if the CSV checkbox is clicked.
$(document).ready(function(){
  $('#uploads').hide();
  $('#enable_uploads').change(function(){
      $('#uploads').toggle()
  });
});