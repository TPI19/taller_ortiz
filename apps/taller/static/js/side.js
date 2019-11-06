/* Set the width of the side navigation to 250px and the left margin of the page content to 250px */
function openNav() {
  document.getElementById("mySidenav").style.width = "450px";
  document.getElementById("header").style.marginRight = "450px";
  document.getElementById("main").style.marginRight = "450px";
  document.getElementById("nav-p").style.position = "relative";
  document.getElementById("login-btn").onclick = closeNav;
  
}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0 */
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("header").style.marginRight = "0";
  document.getElementById("main").style.marginRight = "0";
  document.getElementById("nav-p").style.position = "fixed";
  document.getElementById("login-btn").onclick = openNav;
} 