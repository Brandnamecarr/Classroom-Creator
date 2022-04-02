// will display the File-Upload Option if the CSV checkbox is clicked.
$(document).ready(function(){
  $('#uploads').hide();
  $('#enable_uploads').change(function(){
      $('#uploads').toggle()
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
  $.ajax({
          url: "get_current_google_classrooms",
          success: function(data){
            console.log(data);
            for (let i = 0; i < data.length; i++) {
              console.log(data[0].descriptionHeading);
            }
          }
          });
}

getGoogleClassroomData();