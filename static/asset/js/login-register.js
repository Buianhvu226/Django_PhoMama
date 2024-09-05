var x = document.getElementById("login");
var y = document.getElementById("register");
var z = document.getElementById("switch-btn");

function register() {
    x.style.left = "-400px";
    y.style.left = "50px";
    z.style.left = "50%"
}
function login() {
    x.style.left = "50px";
    y.style.left = "450px";
    z.style.left = "0"
}

window.onload = function () {
	document.querySelector('#error').textContent = '';	
    const urlParams = new URLSearchParams(window.location.search);
    var status = urlParams.get('status').toLowerCase();
    if (status == "register") {
        document.getElementById('register-state').click();
    }
    else {
        document.getElementById('login-state').click();
    }
};