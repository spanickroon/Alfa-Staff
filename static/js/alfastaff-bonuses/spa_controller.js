function init(ev){
    document.querySelectorAll('.num').forEach((link)=>{
        link.addEventListener('click', change_page);
    })
    
    show_first_page();
}

function show_first_page(){
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
    })
    .catch(() => console.log('error'));
}

function change_page(ev){
    ev.preventDefault();

    console.log(ev.target.id)

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
        if(render_html == "error"){
            sendNotification('Сайт', {
                body: 'Бонусов больше нет(',
                dir: 'auto'
            });
        } else {
            document.getElementById('bonuses_container').innerHTML = render_html;
        }
    })
    .catch(() => console.log('error'));
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