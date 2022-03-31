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

$(document).ready(function() {
  $('#googleSuccessBar').hide();
  $('#googleConnected').change(function() {
    $('#googleSuccessBar').toggle()
  });
});


//test fucntion for signing in with google.
//Prints users' information.
function onSignIn(googleUser) {
  console.log("Signed in!");
  //Useful data for your client-side scripts:
  var profile = googleUser.getBasicProfile();
  console.log("ID: " + profile.getId()); // Don't send this directly to your server!
  console.log('Full Name: ' + profile.getName());
  console.log('Given Name: ' + profile.getGivenName());
  console.log('Family Name: ' + profile.getFamilyName());
  console.log("Image URL: " + profile.getImageUrl());
  console.log("Email: " + profile.getEmail());
}