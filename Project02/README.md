# CS1XA3 Project 02
#### Nithusha Sivakumar | sivakumn | 400088188

## Overview

This webage is my, Nithusha's, custom CV.

## Custom Javscript Code #1

**Description:**
My first custom javascript is in a file called `Collapseit-Custom.js`. It can be found in `private/CS1XA3/Project02/js`.

I added this feature just to have some fun and show some of my interests beyond what goes on a CV. For this I included a collapsible collage of some of my photos. To not clutter up space, I thought it would be best to leave to the user if they wanted to explore that or not. 

I've added comments to the javascript file, but the function focuses on the button that users need to click to collapse or uncollapse the collage. Using the `.toggle()` the function toggles between whether the button is "active" or not which is a class describing the state of the button. Based on this, a new height is set for the content below the button.

The code has been inserted below as well:

```javascript
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
```

## Custom Javscript Code #2

**Description:**
My second custom javascript is in a file called `Animation2-Custom.js`. It can be found in `private/CS1XA3/Project02/js` as well.

This was a cool animation that I thought was aesthetically pleasing. Users have to click the button 
and it again toggles between fading in the boxes or fading out the set of boxes. This uses `.fadeToggle()` which is a jQuery selector and is linked at the beginning of the HTML before the javascript.

There are comments on the file, but this function now looks for the containers with a specific id name, that is unique to the animation I created. Specifically it goes through the document and finds the range of boxes I created at the bottom of the page. I set initiliazer speeds for both fading in and fading out. Based on if the container is visible or not it, either descends or ascends in speed through a for loop of all containers with the unique id name of "animation".

The code has been inserted below as well:

```javascript
$(document).ready(function () {
    $("#mine").click(function() {                                   /*What to do when button is clicked ie defining its function*/
        var x = document.getElementsByClassName("animation");       /*find all elements with the TagName div ie all boxes made*/
        var i;                                                      /* initializer/counter for the array of elements*/
        var j = 4500;                                               /* initializer/coutner for speed of fadeToggle if boxes aren't visible*/
        var k = 900;                                                /* initializer/coutner for speed of fadeToggle if boxes are visible*/

        for ( i = 0; i < x.length; i ++) {                          /* loop through every element in x so all boxes, find the idName and then run fadeToggle, reset the speed for each following box to be faster than the one before*/
            var idName = x[i].id;
            var s = "#" + idName;
            if ($(s).is(":visible")) {
                $(s).fadeToggle(k);
                k = k * (1.005)**i;
            }
            else {
                $(s).fadeToggle(j);
                j = j/(1.05)**i;
            }         
        }
    })
})
```

**References:** 
- The Html document used this template from [Themezy](https://www.themezy.com/):
    [Main Template](https://www.themezy.com/free-website-templates/151-ceevee-free-responsive-website-template)
    
    - The CSS and javascript files not mentioned as a custom code also primarily came from this download and were altered to suit my needs.

- The big constellation animation came from a template from [CodePen](https://codepen.io/):
    [Constellation](https://codepen.io/acauamontiel/pen/mJdnw)
    
    - JavaScript file named `Constellation.js` under the folder js is where the template is implemented.

- Some code from this codepen animation was altered to fit the animation above. 
    [ConstellationAnimation](https://codepen.io/andrew_lee87/pen/jAvLav)

- The CSS code for the images is from a template from [w3schools](https://www.w3schools.com/):
    [ResponsiveImageGrid](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_image_grid_responsive)
    
    - It can be found in `private/CS1XA3/Project02/CSS` under a file in named `Animation.css`.
