const swiperHeader = new Swiper('.header-slider',{
	slidesPerView: 1,
	loop:true,
  autoplay: {
    delay: 3000,
  },
  pagination: {
    el: '.swiper-pagination',
    type: 'bullets',
    clickable: true,
  },
});



const searchBtn = document.querySelector('.nav_search-btn');
const searchForm = document.querySelector('.searchForm');
const body = document.querySelector('body');
const printArticle = document.querySelector('.print-article');
const textArticle = document.querySelector('.article-inside__main');
const closeBtn =  document.querySelector('.close-form');

searchBtn.onclick = () =>{
  console.log('работает');
  searchForm.classList.toggle('searchModal');
  body.classList.add('noScroll');
}
closeBtn.onclick = () =>{
  searchForm.classList.remove('searchModal');
  body.classList.remove('noScroll');
}

printBtnOnClick = () =>{
  var pageHtml = document.body.innerHTML
  var htmlToPrint = document.getElementsByClassName('container')[1].innerHTML
  document.body.innerHTML = htmlToPrint;
  window.print();
  document.body.innerHTML = pageHtml;
  return 0
  //window.print();
}



const swiperMenu = new Swiper('.second-menu-slider',{
	loop:true,
  slidesPerView:1,
  spaceBetween:10,
  navigation:{
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  breakpoints:{
    320:{
      slidesPerView:1,
    },
    800:{
      slidesPerView:2,
    },
    1190:{
      slidesPerView:3,
    },
    1292:{
      slidesPerView:4,
    },
  }
});
window.onscroll = function showHeader() {
	let header = document.querySelector('.navbar');
	if(window.pageYOffset > 30){
		header.classList.add('navbar_white');

    try {
      topBtn.style.visibility = 'visible';
    } catch (error) {
      console.log(error)
    }

	}else{
		header.classList.remove('navbar_white');
		topBtn.style.visibility = 'hidden';
	}
}



