const app = {
    pages: [],
    show: new Event('show'),
    init: function(){
        app.pages = document.querySelectorAll('.page');
        app.pages.forEach((pg)=>{
            pg.addEventListener('show', app.pageShown);
        })
        document.querySelectorAll('.nav-link').forEach((link)=>{
            link.addEventListener('click', app.nav);
        })

        document.getElementById("btn-login").addEventListener('click', login);
        document.getElementById("p_c").addEventListener('click', show_hide_password);

        history.replaceState({}, '', 'login');
        window.addEventListener('popstate', app.poppin);
    },
    nav: function(ev){
        ev.preventDefault();
        let currentPage = ev.target.getAttribute('data-target');

        if(document.querySelector('.active').getAttribute("id") == "login"){
            document.getElementById("email_login").value = "";
            document.getElementById("password").value = "";
            document.getElementById("error_login").innerText = "";
        } else if (document.querySelector('.active').getAttribute("id") == "signup") {
            document.getElementById("email_signup").value = "";
            document.getElementById("password1").value = "";
            document.getElementById("password2").value = "";
            document.getElementById("error_signup").innerText = "";
        } else if (document.querySelector('.active').getAttribute("id") == "reset") {
            document.getElementById("email_reset").value = "";
            document.getElementById("error_reset").innerText = "";
        }

        document.querySelector('.active').classList.remove('active');
        document.getElementById(currentPage).classList.add('active');
        history.pushState({}, currentPage, currentPage);
        document.getElementById(currentPage).dispatchEvent(app.show);
    },
    pageShown: function(ev){
        ev.preventDefault();

        let currentPage = document.querySelector('.active').getAttribute('id');
        if (currentPage != 'login') {
            fetch(currentPage + "_insert", 
                {
                method: "GET",
                headers:{"content-type":"application/x-www-form-urlencoded"}
            })
            .then( response => {
                if (response.status !== 200) {
                    return Promise.reject();
                }
                return response.text()
            })
            .then( render_html => {
                if (currentPage == "signup") {
                    document.querySelector('.active').innerHTML = render_html;
                    document.getElementById("btn-signup").addEventListener('click', signup);
                    console.log(document.getElementById("reset"))
                    document.querySelectorAll('.nav-link').forEach((link)=>{
                        link.addEventListener('click', app.nav);
                    })
                } else if (currentPage == "reset") {
                    document.querySelector('.active').innerHTML = render_html;
                    document.getElementById("btn-reset").addEventListener('click', reset);
                }
            })
            .catch(() => console.log('error'));
        }
    },
    poppin: function(ev){
        let hash = location.pathname.replace('/', '');
        document.querySelector('.active').classList.remove('active');
        document.getElementById(hash).classList.add('active');
        document.getElementById(hash).dispatchEvent(app.show);
    }
}

window.onload=function()
{
    history.replaceState({}, '', 'login');
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function sendNotification(title, options) {
    if (!("Notification" in window)) {
        alert('Ваш браузер не поддерживает HTML Notifications, его необходимо обновить.');
    } else if (Notification.permission === "granted") {
        var notification = new Notification(title, options);
    } else if (Notification.permission !== 'denied') {
        Notification.requestPermission(function (permission) {
            if (permission === "granted") {
                var notification = new Notification(title, options); 
            }
        });
    } else {
        // Пользователь ранее отклонил наш запрос на показ уведомлений
    }
}

function login(ev) {
    ev.preventDefault();

    fetch('login', 
    {
        method: "POST",
        body: "email=" + document.getElementById("email_login").value + "&password=" + document.getElementById("password").value,
        headers: {"content-type": "application/x-www-form-urlencoded", "X-CSRFToken": getCookie('csrftoken') },
    })
    .then( response => {
        if (response.status !== 200) {
            
            return Promise.reject(); 
        }
        return response.json()
    })
    .then( response => {
        if (response['validation'] == "ok") {
            document.location.href = 'profile'
        } else if (response['validation'] == "error") {
            document.getElementById("error_login").innerText = "Проверьте введенные вами данные."
        } else if (response['validation'] == "user_not_found") {
            document.getElementById("error_login").innerText = "Пользователь не найден. Проверьте введенные вами данны."
        } else if (response['validation'] == "password_incorrect") {
            document.getElementById("error_login").innerText = "Проверьте введенный вами пароль."
        }
    })
    .catch(() => console.log('error'));
}

function signup(ev) {
    ev.preventDefault();

    if (document.getElementById("password1").value == document.getElementById("password2").value) {
        fetch('signup', 
        {
            method: "POST",
            body: "email=" + document.getElementById("email_signup").value + "&password1=" + document.getElementById("password1").value + "&password2=" + document.getElementById("password2").value,
            headers: {"content-type": "application/x-www-form-urlencoded", "X-CSRFToken": getCookie('csrftoken') },
        })
        .then( response => {
            if (response.status !== 200) {
                
                return Promise.reject(); 
            }
            return response.json()
        })
        .then( response => {
            if (response['confirmation'] == "ok") {
                sendNotification('Регистрация', {
                    body: 'Пожалуйста, подтвердите ваш email адресс для завершения регистрации.',
                    dir: 'auto'
                });
            } else if (response['confirmation'] == "error") {
                document.getElementById("error_signup").innerText = "Проверьте введенный вами логин или пароль."
            } else if (response['confirmation'] == "user_found") {
                document.getElementById("error_signup").innerText = "Данный пользователь уже зарегистрирован."
            }
        })
        .catch(() => console.log('error'));
    } else {
        document.getElementById("error_signup").innerText = "Пароли не совпадают!"
    }
}

function reset(ev) {
    ev.preventDefault();

    fetch('reset', 
    {
        method: "POST",
        body: "email=" + document.getElementById("email_reset").value,
        headers: {"content-type": "application/x-www-form-urlencoded", "X-CSRFToken": getCookie('csrftoken') },
    })
    .then( response => {
        if (response.status !== 200) {
            
            return Promise.reject(); 
        }
        return response.json()
    })
    .then( response => {
        if (response['reseting'] == "ok") {
            sendNotification('Восстановление пароля', {
                body: 'Пожайлуйста, зайдите на ваш email адресс для полученя нового пароля.',
                dir: 'auto'
            });
        } else if (response['reseting'] == "error") {
            document.getElementById("error_reset").innerText = "Проверьте введенный вами email."
        } else if (response['reseting'] == "user_not_found") {
            document.getElementById("error_reset").innerText = "Пользователь не найден. Проверьте введенный вами email."
        }
    })
    .catch(() => console.log('error'));
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

document.addEventListener('DOMContentLoaded', app.init);