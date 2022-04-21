// will display the File-Upload Option if the CSV checkbox is clicked.
$(document).ready(function(){
  $('#uploads').hide();
  $('#canvas-form').hide();
  
  $('#enable_uploads').change(function(){
      var checked = $(this).prop('checked');
      
      if (checked) {
        $('.canvas-login').hide();
        $('#canvas-form').hide();
        $('#uploads').show();
      } else {
        $('#uploads').hide();
        $('.canvas-login').show();
      }
  });

  $( "#switch-user" ).click(function() {
    window.location.replace("/google_logout");
  });

  $( "#cancel-csv" ).click(function() {
    var $filename = $('#filename');
    window.location.replace("/cancel_csv?file=" + filename);
  });

  $( "#cancel-canvas" ).click(function() {
    window.location.replace("/canvas_disconnect");
  });

  $( "#canvas-connect" ).click(function() {
    $('.csv-checkbox').toggle();
    $('.canvas-login').toggle();
    $('#canvas-form').toggle();
  });

  $( '#migrate-csv' ).click(function() {
    migratecsv();
  });
  
  $( "#cancel-connect" ).click(function() {
    $('.csv-checkbox').toggle();
    $('.canvas-login').toggle();
    $('#canvas-form').toggle();
  });

  $( '#migrate-canvas' ).click(function() {
    migrateCanvas();
  });
  
  getGoogleClassroomData();
  getCanvasClassroomData();
});

function showModal(modalHeader, modalBody) {
  $("#myModal .modal-title").text(modalHeader);
  $("#myModal .modal-body").text(modalBody);
  $("#myModal").modal('show');
}

function loadingHeader(msg) {
  header = "Loading";
  showModal(header, msg);
}

//starts the migration process from canvas to google in backend
function migrateCanvas() {
  loadingHeader("Copying your courses to Google Classroom...")
  $.ajax({
    url: "migrate_canvas",
    success: function(data){
      if (data == "success") {
        header = "Success";
        body = `Congrats! Your courses were successfully uploaded to Google Classroom. 
                We reccomend you verify all Course and Student data is correct.`;
        showModal(header, body);
        getGoogleClassroomData()
      } else {
        console.log(data);
        header = "Error";
        body = data;
        showModal(header, body);
      }
    }
    });
}

function migratecsv() {
  loadingHeader("Copying your courses to Google Classroom...")
  $.ajax({
    url: "migrate_csv",
    success: function(data){
      if (data == "success") {
        header = "Success";
        body = `Congrats! Your courses were successfully uploaded to Google Classroom. 
                We reccomend you verify all Course and Student data is correct.`;
        showModal(header, body);
        getGoogleClassroomData()
      } else {
        header = "Error";
        body = data;
        showModal(header, body);
      }
    }
    });
}

// google signin funciton will send token to flask server
// for server side usage
function getGoogleClassroomData() {
  checkGoogleStatus;
  $.ajax({
    url: "get_current_google_classrooms",
    success: function(data){
      var items = [];
      for (let i = 0; i < data.length; i++) {
        if (!(data[i].courseState === "ARCHIVED" || data[i].courseState === "DECLINED")) {
          items.push("<li class=\"list-group-item\">" + data[i].name + " " + data[i].section + "</li>");
        }
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
        window.location.replace("/google_login");
      }
    }
  });
}();


