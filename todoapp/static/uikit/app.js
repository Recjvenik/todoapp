// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  hljs.highlightAll();
});


let alertWrapper = document.querySelector('.alert')
let alertclose = document.querySelector('.alert__close')

if(alertWrapper){
  alertclose.addEventListener( 'click', ()=>
    alertWrapper.style.display = 'none'
  )  
}