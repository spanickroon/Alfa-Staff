document.getElementById("nav_login").addEventListener('click', nav_choice);
document.getElementById("nav_signup").addEventListener('click', nav_choice);

function nav_choice(ev) {
    ev.preventDefault();
    if (ev.target.getAttribute('id') == 'nav_login') {
        document.querySelector('.nav-link-active').classList.remove('nav-link-active');
        document.getElementById("nav_login").classList.add('nav-link-active');
    } else {
        document.querySelector('.nav-link-active').classList.remove('nav-link-active');
        document.getElementById("nav_signup").classList.add('nav-link-active');
    }
}

function show_hide_password(target){
    var input = document.getElementById('password');
	if (input.getAttribute('type') == 'password') {
		target.classList.add('view');
		input.setAttribute('type', 'text');
	} else {
		target.classList.remove('view');
		input.setAttribute('type', 'password');
	}
	return false;
}

function show_hide_password1(target){
    var input = document.getElementById('password1');
	if (input.getAttribute('type') == 'password') {
		target.classList.add('view');
		input.setAttribute('type', 'text');
	} else {
		target.classList.remove('view');
		input.setAttribute('type', 'password');
	}
	return false;
}

function show_hide_password2(target){
    var input = document.getElementById('password2');
	if (input.getAttribute('type') == 'password') {
		target.classList.add('view');
		input.setAttribute('type', 'text');
	} else {
		target.classList.remove('view');
		input.setAttribute('type', 'password');
	}
	return false;
}