let buttonRegister = document.getElementById('button-register')


buttonRegister.addEventListener('mouseover', ()=>{
    buttonRegister.style.backgroundColor = "#A1E3F9"
    buttonRegister.style.color = "black"
    buttonRegister.style.cursor = "pointer"
})

buttonRegister.addEventListener('mouseout', ()=>{W
    buttonRegister.style.backgroundColor = "#6b0080"
    buttonRegister.style.color = "white"
    buttonRegister.style.cursor = "default"
})

class FormData{

    formUrl = "register"

    data = {
        nome: "",
        email: "",
        pass: ""
    }

    constructor(){
        this.formulario = document.getElementById('register');
        this.eventos();
    }

    eventos() {
        this.formulario.addEventListener('submit', e =>{
            this.handleSubmit(e);
        })
    }

    handleSubmit(e){
        e.preventDefault();
        this.getData(e);
    }

    getData(e){
        this.data = {
            nome: e.srcElement[0].value,
            email: e.srcElement[1].value,
            pass: e.srcElement[2].value
        }

        this.sendData();
    }

    sendData(){
        fetch(this.formUrl, {
            method: "POST",
            body: JSON.stringify(this.data),
            headers: {
                "Content-Type": "application/json; charset=UTF-8"
            }
        });
    }
}

new FormData();