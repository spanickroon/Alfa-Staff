const animation = '<div class="background"><div class="loader loader-left"></div><div class="loader loader-right"></div><svg xmlns="http://www.w3.org/2000/svg" version="1.1"><defs><filter id="goo"><fegaussianblur in="SourceGraphic" stddeviation="15" result="blur"></fegaussianblur><fecolormatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 26 -7" result="goo"></fecolormatrix><feblend in="SourceGraphic" in2="goo"></feblend></filter></defs></svg></div>'

function init(ev){
    document.querySelectorAll('.num').forEach((link)=>{
        link.addEventListener('click', change_page);
    })

    document.getElementById('sorting_button').addEventListener('click', sort);

    show_first_page();
}

function show_first_page(){    
    document.getElementById('bonuses_container').innerHTML = animation;

    fetch("bonuses/1", 
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
        document.getElementById('bonuses_container').innerHTML = render_html;
        document.querySelectorAll('.button-product-buy').forEach((link)=>{
            link.addEventListener('click', buy);
        })

    })
    .catch(() => console.log('error'));
}

function change_page(ev){
    ev.preventDefault();

    document.getElementById('bonuses_container').innerHTML = animation;

    fetch("bonuses/" + ev.target.id, 
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
        document.getElementById('bonuses_container').innerHTML = render_html;
        document.querySelectorAll('.button-product-buy').forEach((link)=>{
            link.addEventListener('click', buy);
        })
    })
    .catch(() => console.log('error'));
}

function buy(){
    sendNotification('Покупка', {
        body: 'Ваша покупка отправлена на обработку.',
        dir: 'auto'
    });
}

function sort(){
    sendNotification('Сортировка', {
        body: 'Сортировка',
        dir: 'auto'
    });
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

document.addEventListener('DOMContentLoaded', init);