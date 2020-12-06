/*---------------function init---------------*/
function init(){
    document.querySelectorAll('.open_tasks').forEach((link)=>{
        link.addEventListener('click', open_tasks);
    })

    document.getElementById('send').addEventListener('click', send);
}

/*---------------Buy request---------------*/
function review(ev){
    fetch("review",
    {
        method: "POST",
        body: "review_text=" + document.getElementById("review-text").value,
        headers: {"content-type": "application/x-www-form-urlencoded", "X-CSRFToken": getCookie('csrftoken') },
    })
    .then( response => {
        if (response.status !== 200) {
            return Promise.reject();
        }
        return response.json()
    })
    .then( response => {
        document.querySelector(".modal").classList.toggle("show-modal");

        document.getElementById("send").removeAttribute("disabled");

        if(response['send'] == 'ok'){
            toggleModalAnswer('Ваш отзыв отправлен на рассмотрение.')
        } else if (response['send'] == 'error') {
            toggleModalAnswer('Возникла ошибка, сообщите о ней администратору.')
        } else {
            toggleModalAnswer('Возникла ошибка, сообщите о ней администратору.')
        }
    })
    .catch(() => console.log('error'));
}

/*---------------Open tasks request---------------*/
function open_tasks(ev){
    fetch("taskmanager",
    {
        method: "POST",
        body: "number_day=" + ev.target.id,
        headers: {"content-type": "application/x-www-form-urlencoded", "X-CSRFToken": getCookie('csrftoken') },
    })
    .then( response => {
        if (response.status !== 200) {
            return Promise.reject();
        }
        return response.text()
    })
    .then( render_html => {
        document.getElementById('tasks_list').innerHTML = render_html;
    })
    .catch(() => console.log('error'));
}

/*---------------Modal---------------*/
function toggleModal(text) {
    document.querySelector(".modal").classList.toggle("show-modal");
    document.querySelector(".close-button").addEventListener("click", toggleModal);
    document.getElementById("review").addEventListener("click", review);
    document.getElementById("text").innerText = text
}

function toggleModalAnswer(text) {
    if (typeof text == 'object') {
        text = ""
    }
    document.querySelector(".modal-answer").classList.toggle("show-modal");
    document.querySelector(".close-button-answer").addEventListener("click", toggleModalAnswer);
    document.getElementById("text-answer").innerText = text
}

function send(ev){
    toggleModal("Оставьте ваш отзыв.", ev);
    document.getElementById("send").onclick = function() {
        this.disabled = 'disabled';
    }
}

/*---------------Get Cookie---------------*/
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

/*---------------DOM---------------*/
document.addEventListener('DOMContentLoaded', init);