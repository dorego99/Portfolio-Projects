function GradeScale() {
	<!-- recives input and gives a result -->
  var grade = document.getElementById('input').value;
  var result = document.getElementById('output');
	<!-- Recives the input number and outputs the grade based on the number -->
	if (grade >= 89.5)
  {
		result.innerHTML = "Your grade for this class is an A";
  }
	else if (grade >= 79.6 && grade <= 89.5)
  {
		result.innerHTML = "Your grade for this class is a B";
  }
	else if (grade >= 69.6 && grade <= 79.5)
  {
		result.innerHTML = "Your grade for this class is a C";
  }
	else if (grade >= 60 && grade <= 69.5)
  {
		result.innerHTML = "Your grade for this class is a D";
  }
	else if (grade < 60)
  {
		result.innerHTML = "Your grade for this class is an F"
  }
	else
  {
	<!-- Pop up alert if the user gives an invalid grade -->
	window.alert("Invalid grade. Please enter a numerical grade without a percent sign.");
  }
}