function ageScale() {
/* This creates the variable age for the javascript document and links the Id "age" from the HTML document*/
  var age = Number(document.getElementById("age").value);
  document.getElementById("age").value = "";

/* This begins the if else statments. This uses the submitted age between 4 and 15 to be added to the line with the message "total"*/
  if (age >= 4 && age <= 15) {
    var total = document.getElementById("total");
    var senior = document.getElementById("senior");
    var intermediate = document.getElementById("intermediate");
    var junior = document.getElementById("junior");
    total.innerHTML = Number(total.innerHTML) + 1;

/* This adds 1 to each age submitted between 12 and 15 and adds it to the Senior line*/
    if (age <= 15 && age >= 12)
      senior.innerHTML = Number(senior.innerHTML) + 1;

/* This adds 1 to each age submitted between 8 and 11 and adds it to the Intermidiate line*/
    else if (age <= 11 && age >= 8)
      intermediate.innerHTML = Number(intermediate.innerHTML) + 1;

/* This adds 1 to each age submitted between 4 and 7 and adds it to the Junior line*/
    else if (age <= 7 && age >= 4)
      junior.innerHTML = Number(junior.innerHTML) + 1;
  } else {
/* this creates a window alert if someone submits a number that is not between 4 and 15 or if someone submits a letter*/
    window.alert("Invalid age. Please enter an age between 4 and 15");
  }
}