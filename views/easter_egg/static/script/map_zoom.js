function init() {
    console.log('init')
    //to get the value to set the slider to
    var map = document.getElementById("map_of_school");
    currentWidth = map.offsetWidth;

    var slider = document.getElementById("map_slider")
    slider.value = currentWidth;
    console.log('slidervalue'+ String(slider.value))

}

//function to resize the size of the svg
function resizeMap(x){
    console.log(x)
    var map = document.getElementById("map_of_school");

    //gets the width of the div that the map is conatined n
    currentWidth = map.offsetWidth;
    //console.log('currentWidth'+ String(currentWidth));

    //adds the current width to the value that was provided by the argument
    finalWidth = Number(currentWidth) + Number(x);
    //console.log(finalWidth);

    //makes the div reflect the user input
    map.style.width = String(finalWidth)+'px';

    var slider = document.getElementById("map_slider")
    slider.value = finalWidth;
}

let elslider = document.getElementById("map_slider");

// use 'change' instead to see the difference in response
//refrence: https://www.impressivewebs.com/onchange-vs-oninput-for-range-sliders/
elslider.addEventListener('input', function () {
    //console.log(elslider.value)
    document.getElementById("map_of_school").style.width = String(elslider.value)+'px';
}, false);

//running on init
init();