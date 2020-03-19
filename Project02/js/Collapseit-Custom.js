/* find elements under class name collapseIt ie. scroll down icon */
var c = document.getElementsByClassName("collapseIt"); 
    
c[0].addEventListener("click", function() {
    c[0].classList.toggle("active");                                /*switch between if active or not based on appearance on button*/
    var photos = c[0].nextElementSibling;                           /*pick the next element in the same level of tree, by my HTML code, all images would count as the next element*/
    if (c[0].classList.contains('active')) {                        
        photos.style.maxHeight = photos.scrollHeight + "px";        /*if button shows that the images are not expanded then set their new height to original size*/
    }
    else {
        photos.style.maxHeight = 0;                                 /*if button shows images are present, then set their height to 0, so not visible*/
    }
})
