function byebye(img){
    console.log(img)
    let image=img
    image.classList.add("boxgo")
    setTimeout(() => {
        image.classList.remove("boxgo")
        image.style.display="none";
    }, 300);
}

function pinclick(pin, link){
    let box=document.getElementById("box")
    box.src=link
    box.style.display="block"
    pin.src="imgs/gpin.png"
}