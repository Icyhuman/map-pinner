function byebye(img){
    console.log('removing image')
    let image=img
    image.classList.add("boxgo")
    setTimeout(() => {
        image.classList.remove("boxgo")
        image.style.display="none";
    }, 300);
}

function pinclick(pin, link){
    console.log('Displaying image: '+link)
    let box=document.getElementById("box")
    box.src=link
    box.style.display="block"
    pin.src="imgs/gpin.png"
}

console.log('Oh hey, you\'re checking out the console. Cool. Not that there\'s much here, unless you\'re really into actions being logged.')
let secret = 'Yahaha! You found me!'