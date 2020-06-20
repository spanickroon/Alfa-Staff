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

        history.replaceState({}, '', 'login');
        window.addEventListener('popstate', app.poppin);
    },
    nav: function(ev){
        ev.preventDefault();
        let currentPage = ev.target.getAttribute('data-target');
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
        }
    })
    .catch(() => console.log('error'));

}

function signup(ev) {
    ev.preventDefault();

    fetch('signup', 
    {
        method: "POST",
        body: "email=" + document.getElementById("email_signup").value + "&password1=" + document.getElementById("password1").value+ "&password2=" + document.getElementById("password2").value,
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
            alert("Please confirm your email address to complete the registration.")
        }
    })
    .catch(() => console.log('error'));

}

document.addEventListener('DOMContentLoaded', app.init);