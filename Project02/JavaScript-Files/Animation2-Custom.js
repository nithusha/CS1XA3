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