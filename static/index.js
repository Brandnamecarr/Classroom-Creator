// will display the File-Upload Option if the CSV checkbox is clicked.
$(document).ready(function(){
  $('#uploads').hide();
  $('#canvas-form').hide();
  $('#enable_uploads').change(function(){
      $('#uploads').toggle();
      $('.canvas-login').toggle();
  });

  $( "#switch-user" ).click(function() {
    window.location.replace("http://localhost:5000/google_logout");
  });

  $( "#cancel-csv" ).click(function() {
    var $filename = $('#filename');
    window.location.replace("http://localhost:5000/cancel_csv?file=" + filename);
  });

  $( "#cancel-canvas" ).click(function() {
    window.location.replace("http://localhost:5000/canvas_disconnect");
  });

  $( "#canvas-connect" ).click(function() {
    $('.csv-checkbox').toggle();
    $('.canvas-login').toggle();
    $('#canvas-form').toggle();
  });
  
  $( "#cancel-connect" ).click(function() {
    $('.csv-checkbox').toggle();
    $('.canvas-login').toggle();
    $('#canvas-form').toggle();
  });

  getGoogleClassroomData();
  getCanvasClassroomData();

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

function getCanvasClassroomData() {
  if ( $('#canvas-courses').length ){
    $.ajax({
      url: "get_canvas_courses_names",
      success: function(data){
        var items = [];
        for (let i = 0; i < data.length; i++) {
          items.push("<li class=\"list-group-item\">" + data[i].course_name + " " + data[i].course_section + "</li>");
        }
        $('#canvas-courses').append(items);
      }
      });
  }
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
