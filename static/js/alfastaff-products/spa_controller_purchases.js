/*---------------Animation html---------------*/
const animation = '<div class="background-purchases"><div class="loader loader-left"></div><div class="loader loader-right"></div><svg xmlns="http://www.w3.org/2000/svg" version="1.1"><defs><filter id="goo"><fegaussianblur in="SourceGraphic" stddeviation="15" result="blur"></fegaussianblur><fecolormatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 26 -7" result="goo"></fecolormatrix><feblend in="SourceGraphic" in2="goo"></feblend></filter></defs></svg></div>'

/*---------------SPA function---------------*/
function init(){
    document.querySelectorAll('.num').forEach((link)=>{
        link.addEventListener('click', change_page);
    })

    document.getElementById('sorting_button').addEventListener('click', sort);

    try {
        show_first_page();
    } catch (error) {
    }
}

/*---------------Show page request---------------*/
function show_first_page(){
    document.getElementById('1').classList.add("this-page")

    document.getElementById('list_purchases_container').innerHTML = animation

    var request = "purchases/1/sort_date"

    if(document.getElementById('sorting_button').classList.contains("activated")){
        request = "purchases/1/sort_cost"
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
        document.getElementById('list_purchases_container').innerHTML = render_html;
    })
    .catch(() => console.log('error'));
}

/*---------------Change page request---------------*/
function change_page(ev){
    ev.preventDefault();

    document.querySelectorAll('.this-page')[0].classList.remove("this-page")
    document.getElementById(ev.target.id).classList.add("this-page")

    document.getElementById('list_purchases_container').innerHTML = animation;

    var request = "purchases/" + ev.target.id + "/sort_alphabet"

    if(document.getElementById('sorting_button').classList.contains("activated")){
        request = "purchases/" + ev.target.id + "/sort_cost"
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
        document.getElementById('list_purchases_container').innerHTML = render_html;
    })
    .catch(() => console.log('error'));
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
        element.innerText = "Сортировать по дате"
        show_first_page()
    }
}

/*---------------DOM---------------*/
document.addEventListener('DOMContentLoaded', init);