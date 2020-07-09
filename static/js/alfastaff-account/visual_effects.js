/*---------------Navigation effect---------------*/
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