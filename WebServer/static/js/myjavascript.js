
var cloudType = "google";
var routerPublicIP = "52.32.16.225";
var routerPrivateIP = "172.31.17.245";

function addRouter() {
    document.getElementById("myDropdown").classList.toggle("show");
}
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {

    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}

function toggleRouter() {
    document.getElementById("myDropDown").classList.toggle("show");
}
function deleterouter() {
    
}