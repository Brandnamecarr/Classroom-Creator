// will display the File-Upload Option if the CSV checkbox is clicked.
$(document).ready(function(){
  $('#uploads').hide();
  $('#enable_uploads').change(function(){
      $('#uploads').toggle();
      $('.canvas-login').toggle();
  });
});

$(document).ready(function() {
  $('#googleSuccessBar').hide();
  $('#googleConnected').change(function() {
    $('#googleSuccessBar').toggle()
  });
});


// google signin funciton will send token to flask server
// for server side usage
function getGoogleClassroomData() {
  checkGoogleStatus;
  $.ajax({
    url: "get_current_google_classrooms",
    success: function(data){
      var items = [];
      for (let i = 0; i < data.length; i++) {
        items.push("<li class=\"list-group-item\">" + data[i].descriptionHeading + "</li>");
      }

      $('#google-courses').append(items);
    }
    });
}

// check if user is logged in. If not redirect to google login
var checkGoogleStatus = function() {
  $.ajax({
    url: "google_login_check",
    success: function(data){
      if (data === "false"){
        window.location.replace("http://localhost:5000/google_login");
      }
    }
  });
}();

$(document).ready(function(){
  getGoogleClassroomData();
});
