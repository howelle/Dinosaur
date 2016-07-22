window.onload=function drops() {
	var dinosaur = document.getElementById('dinosaur');
	var timeperiod = document.getElementById('timeperiod');
	var place = document.getElementById('place');

	var Dropdown1 = document.getElementById('Dinosaurs');
	var Dropdown2 = document.getElementById('Timeperiods');
	var Dropdown3 = document.getElementById('Places');


	dinosaur.addEventListener("mouseenter", firstEnter);
	timeperiod.addEventListener("mouseenter", secondEnter);
	place.addEventListener("mouseenter", thirdEnter);

	function firstEnter(ev) {
		Dropdown1.classList.toggle("show")
		ev.preventDefault()
	}

	function secondEnter(ev) {
		Dropdown2.classList.toggle("show")
		ev.preventDefault()
	}

	function thirdEnter(ev) {
		Dropdown3.classList.toggle("show")
		ev.preventDefault()
	}


	Dropdown1.addEventListener("mouseleave", firstExit);
	Dropdown2.addEventListener("mouseleave", secondExit);
	Dropdown3.addEventListener("mouseleave", thirdExit);

	function firstExit(ev) {
		ev.preventDefault()
		Dropdown1.classList.remove("show")

	}


	function secondExit(ev) {
		ev.preventDefault()
		Dropdown2.classList.remove("show")

	}

	function thirdExit(ev) {
		ev.preventDefault()
		Dropdown3.classList.remove("show")

	}



window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {

    var dropdowns = document.getElementsByClassName("dropdown-content");
    var dropdowns2 = document.getElementsByClassName("dropdown-content2");
    var dropdowns3 = document.getElementsByClassName("dropdown-content3");
    
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }}

    var j;
    for (j = 0; j < dropdowns2.length; j++) {
      var openDropdown2 = dropdowns2[j];
      if (openDropdown2.classList.contains('show')) {
        openDropdown2.classList.remove('show');
      }
  }
    var k;
    for (k = 0; k < dropdowns3.length; k++) {
      var openDropdown3 = dropdowns3[k];
      if (openDropdown3.classList.contains('show')) {
        openDropdown3.classList.remove('show');
      }}

	}

}
};


