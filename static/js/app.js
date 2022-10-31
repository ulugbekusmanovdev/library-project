//  Navbar

const nav = document.getElementById('nav');
const menu = document.getElementById('menu');
const menuHeigt = menu.getBoundingClientRect().height;
const menuH = menuHeigt - 240;

const setScrollListebner = () => {
    const { scrollY } = window;

    if (scrollY >= menuH) {
        nav.classList.add('sticky');
    } else {
        nav.classList.remove('sticky');
    }
}

window.addEventListener("scroll", setScrollListebner)


