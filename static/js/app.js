//  Navbar

const nav = document.getElementById('nav');
const menu = document.getElementById('menu');
const menuHeigt = menu.getBoundingClientRect().height;
const menuH = menuHeigt - 240;

// document.addEventListener("DOMContentLoaded", () => {
// 	const elemenId = window.location.href.match(/#(\w+)$/)[1];
// 	if(elemenId){
// 		console.log(elemenId, window.location.href);
// 		const elementTop = document.getElementById(elemenId).getBoundingClientRect()
	
// 		window.scrollTo({
// 			behavior: "smooth",
// 			top: elementTop - 400
// 		})
// 	}
	
// })





const setScrollListebner = () => {
	const { scrollY } = window;

	if (scrollY >= menuH) {
		nav.classList.add('sticky');
	} else {
		nav.classList.remove('sticky');
	}
}

window.addEventListener("scroll", setScrollListebner)



// /* Когда пользователь нажимает на кнопку, переключаться раскрывает содержимое */
// function myFunction() {
// 	document.getElementById("books_myDropdown").classList.toggle("show");
// }
// // Закрыть раскрывающийся список, если пользователь щелкнет за его пределами.
// window.onclick = function (event) {
// 	if (!event.target.matches('.books_dropbtn')) {
// 		var dropdowns = document.getElementsByClassName("books_dropdown-content");
// 		var i;
// 		for (i = 0; i < dropdowns.length; i++) {
// 			var openDropdown = dropdowns[i];
// 			if (openDropdown.classList.contains('show')) {
// 				openDropdown.classList.remove('show');
// 			}
// 		}
// 	}
// }