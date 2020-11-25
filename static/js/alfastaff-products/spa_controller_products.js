/*---------------Animation html---------------*/
const animation = '<div class="background"><div class="loader loader-left"></div><div class="loader loader-right"></div><svg xmlns="http://www.w3.org/2000/svg" version="1.1"><defs><filter id="goo"><fegaussianblur in="SourceGraphic" stddeviation="15" result="blur"></fegaussianblur><fecolormatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 26 -7" result="goo"></fecolormatrix><feblend in="SourceGraphic" in2="goo"></feblend></filter></defs></svg></div>'

/*---------------SPA function---------------*/
function init(ev){
    document.querySelectorAll('.num').forEach((link)=>{
        link.addEventListener('click', change_page);
    })

    document.getElementById('sorting_button').addEventListener('click', sort);

    show_first_page();
}

/*---------------Show page request---------------*/
function show_first_page(){    
    document.getElementById('1').classList.add("this-page")

    document.getElementById('products_container').innerHTML = animation;

    var request = "products/1/sort_alphabet"

    if(document.getElementById('sorting_button').classList.contains("activated")){
        request = "products/1/sort_cost"
    }

    fetch(request, 
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
        document.getElementById('products_container').innerHTML = render_html;
        document.querySelectorAll('.button-product-buy').forEach((link)=>{
            link.addEventListener('click', confirm);
        })

    })
    .catch(() => console.log('error'));
}

/*---------------Change page request---------------*/
function change_page(ev){
    ev.preventDefault();

    document.querySelectorAll('.this-page')[0].classList.remove("this-page")
    document.getElementById(ev.target.id).classList.add("this-page")

    document.getElementById('products_container').innerHTML = animation;

    var request = "products/" + ev.target.id + "/sort_alphabet"

    if(document.getElementById('sorting_button').classList.contains("activated")){
        request = "products/" + ev.target.id + "/sort_cost"
    }

    fetch(request, 
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
        document.getElementById('products_container').innerHTML = render_html;
        document.querySelectorAll('.button-product-buy').forEach((link)=>{
            link.addEventListener('click', confirm);
        })
    })
    .catch(() => console.log('error'));
}

/*---------------Buy request---------------*/
function buy(ev){
    fetch("buy/" + ev.target.dataset["target"],
    {
        method: "GET",
        headers:{"content-type":"application/x-www-form-urlencoded"}
    })
    .then( response => {
        if (response.status !== 200) {
            return Promise.reject();
        }
        return response.json()
    })
    .then( response => {   
        document.querySelector(".modal").classList.toggle("show-modal");

        document.getElementById("confirm").removeAttribute("disabled");

        if(response['buy'] == 'ok'){
            toggleModalAnswer('Ваша покупка отправлена на обработку.')
        } else if (response['buy'] == 'error') {
            toggleModalAnswer('Возникла ошибка, сообщите о ней администратору.')
        } else if (response['buy'] == 'not_money') {
            toggleModalAnswer('Недостаточно бонусов для покупки.')
        }
    })
    .catch(() => console.log('error'));
}

/*---------------Modal---------------*/
function toggleModal(text, ev) {
    document.querySelector(".modal").classList.toggle("show-modal");
    document.querySelector(".close-button").addEventListener("click", toggleModal);
    document.getElementById("confirm").setAttribute("data-target", ev.target.id);
    document.getElementById("confirm").addEventListener("click", buy);
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

function confirm(ev){
    toggleModal("Вы уверены, что хотите купить этот товар?", ev);
    document.getElementById("confirm").onclick = function() {
        this.disabled = 'disabled';
    }
}

/*---------------Sort---------------*/
function sort(){
    var element = document.getElementById("sorting_button")
    if (element.classList.contains("activated")){
        element.classList.remove("activated")
        element.innerText = "Сортировать по цене"
        show_first_page()
    } else {
        element.classList.add("activated")
        element.innerText = "Сортировать по алфавиту"
        show_first_page()
    }
}

/*---------------DOM---------------*/
document.addEventListener('DOMContentLoaded', init);