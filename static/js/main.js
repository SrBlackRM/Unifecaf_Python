let buttonRegister = document.getElementById('button-register')


buttonRegister.addEventListener('click', ()=>{
    console.log('funcionando!!')
})

buttonRegister.addEventListener('mouseover', ()=>{
    console.log('cor')
    buttonRegister.style.backgroundColor = "#A1E3F9"
    buttonRegister.style.color = "black"
    buttonRegister.style.cursor = "pointer"
})

buttonRegister.addEventListener('mouseout', ()=>{
    console.log('cor')
    buttonRegister.style.backgroundColor = "#6b0080"
    buttonRegister.style.color = "white"
    buttonRegister.style.cursor = "default"
})

class FormData{
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
        let data = {
            nome: e.srcElement[0].value,
            email: e.srcElement[1].value,
            pass: e.srcElement[2].value
        }

        console.log(data)
    }
}
 

let valida = new FormData()