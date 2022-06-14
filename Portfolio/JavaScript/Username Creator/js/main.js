function clicked() {
/** This set of code uses the ID I set from my username_CDV.html file and gives them a variable */
  var firstname = document.getElementById('firstname').value;
  var lastname = document.getElementById('lastname').value;
  var schoolname = document.getElementById('school').value;

/** This line creates an alert window with the username based on the input of the user after the "Create Username" button is clicked. */
  alert("Your username is: " + firstname.substr(0, 1) + lastname.substr(0, 1) + schoolname.replace(/^(.{1}[^\s]*).*/, "$1") + "\n");

}
