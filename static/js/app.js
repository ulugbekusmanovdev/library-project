//  Navbar

const nav = document.getElementById("nav");
const menu = document.getElementById("menu");
const menuHeigt = menu.getBoundingClientRect().height;

window.onscroll = function(){
const {scrollTop} = document.documentElement;

    if(scrollTop >= menuHeigt){
        nav.classList.add("sticky");
    } else {
        nav.classList.remove("sticky");
    }
}

// Hamburger menu
// const creat = document.querySelector('label');
// const naw = document.querySelector(".nav");
// const on = document.querySelector('.button');
// const off = document.querySelector('.button2');

// on.onclick = () => {
//     creat.classList.remove('button');
//     creat.classList.add('button2');
//     naw.classList.add('over', 'nav');
// }

// off.onclick = () => {
//     creat.classList.remove('button2');
//     creat.classList.add('button');
//     naw.classList.add('nav');
//     naw.classList.remove('over');

// }





// drop-down menu

// document.getElementById('menu').onmouseover = function(event) {
//     const target = event.target;
   
//     if(target.className == "navbar_title") {
//         const sub = target.getElementsByClassName('navbar_sub');
//         closeMenu();
//         sub[0].style.display = "block"; 
//     }
// }

// document.onmouseover = function(event){
//     const target = event.target;
//     console.log(event.target);
//     if(target.className != "navbar_title" && target.className != "navbar_sub" ){
//         closeMenu();
//     }
// }


// function closeMenu() {
//     // const menuu = document.getElementById("nav");
//     const subm = document.getElementsByClassName('navbar_sub');
//     for (let i = 0; i < subm.length; i++){
//         subm[i].style.display = "none";
//     }
// }

// // Slider
// var slideIndex = 1;
// showSlides(slideIndex);

// // Next/previous controls
// function plusSlides(n) {
//   showSlides(slideIndex += n);
// }

// // Thumbnail image controls
// function currentSlide(n) {
//   showSlides(slideIndex = n);
// }

// function showSlides(n) {
//   var i;
//   var slides = document.getElementsByClassName("mySlides");
//   var dots = document.getElementsByClassName("dot");
//   if (n > slides.length) {slideIndex = 1}
//   if (n < 1) {slideIndex = slides.length}
//   for (i = 0; i < slides.length; i++) {
//       slides[i].style.display = "none";
//   }
//   for (i = 0; i < dots.length; i++) {
//       dots[i].className = dots[i].className.replace(" active", "");
//   }
//   slides[slideIndex-1].style.display = "block";
//   dots[slideIndex-1].className += " active";
// }

// var slideIndex = 0;
// showSlides();

// function showSlides() {
//     var i;
//     var slides = document.getElementsByClassName("mySlides");
//     for (i = 0; i < slides.length; i++) {
//         slides[i].style.display = "none";
//     }
//     slideIndex++;
//     if (slideIndex > slides.length) {slideIndex = 1}
//     slides[slideIndex-1].style.display = "block";
//     setTimeout(showSlides, 10000); // Change image every 5 seconds
// }

