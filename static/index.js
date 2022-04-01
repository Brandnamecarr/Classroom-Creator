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
function onSignIn(googleUser) {
  console.log("Signed in!");
  //Useful data for your client-side scripts:
  var id_token = googleUser.getAuthResponse().id_token;
  $.ajax({
          type : 'POST',
          url: "token", 
          data : {'id_token' : id_token}
          });
}