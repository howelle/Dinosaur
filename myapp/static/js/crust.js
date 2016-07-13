/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
	function dinoFunction(){
		document.getElementById("Dinosaurs").classList.toggle("show");
	}
	function timeFunction(){
		document.getElementById("Timeperiod").classList.toggle("show");
	}
	function placeFunction(){
		document.getElementById("Place").classList.toggle("show");
	}
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {

    var dropdowns = document.getElementsByClassName("toggleable");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}
$('#menucontainer').click(function(event){
    event.stopPropagation();
});

