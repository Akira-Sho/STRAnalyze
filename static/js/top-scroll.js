document.addEventListener('DOMContentLoaded', e => {
const PageTopBtn = document.getElementById('scroll-top');

window.addEventListener( 'scroll' , scroll_event );
function scroll_event(){
if(window.pageYOffset > 400){
    PageTopBtn.style.opacity = '1';
    PageTopBtn.style.display = 'block';
  }else if(window.pageYOffset < 399){
    PageTopBtn.style.opacity = '0';
    PageTopBtn.style.display = 'none';
  }
};

PageTopBtn.addEventListener('click', () =>{
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
});
});