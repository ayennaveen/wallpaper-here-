const btn = document.getElementById('checkbox');
const targetElement = document.getElementById('your-element-id');
const body = document.querySelector('body');
btn.addEventListener('click', function onClick(event) {
   if( this.classList.toggle('checkbox')){
    body.style.background='rgb(0, 0, 139)';
    body.style.color='white';
    body.style.transition='2s';
 
   }
   else{
    body.style.background='white';
    body.style.color='rgb(0, 0, 139)';
    body.style.transition='2s';
   }
});