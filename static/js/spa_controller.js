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
                document.querySelector('.active').innerHTML = render_html;
            })
            .catch(() => console.log('ошибка'));
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

document.addEventListener('DOMContentLoaded', app.init);