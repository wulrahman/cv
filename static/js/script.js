var scrollTop = function() {
    window.scrollTo(0, 0);
};


window.onload = function() {

    scrollTop();
        // Get a reference to the <path>
    var path_star = document.getElementById('star-path');
    var svg_container = document.getElementById('svg_container');
    var down_icon = document.getElementById('down-icon');
    var background_blur = document.getElementById('background-blur');

    // Get length of path... ~577px in this case
    var pathLength = path_star.getTotalLength();

    // Make very long dashes (the length of the path itself)
    path_star.style.strokeDasharray = pathLength + ' ' + pathLength;

    // Offset the dashes so the it appears hidden entirely
    path_star.style.strokeDashoffset = pathLength;

    // Jake Archibald says so
    // https://jakearchibald.com/2013/animated-line-drawing-svg/
    path_star.getBoundingClientRect();

    // When the page scrolls...
    document.onscroll = function(event) {
    
        // What % down is it? 
        // https://stackoverflow.com/questions/2387136/cross-browser-method-to-determine-vertical-scroll-percentage-in-javascript/2387222#2387222
        // Had to try three or four differnet methods here. Kind of a cross-browser nightmare.
        // var page_height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        var scrollPercentage = (document.documentElement.scrollTop + document.body.scrollTop) / (window.innerHeight-100);
            
        // Length to offset the dashes
        var drawLength = pathLength * scrollPercentage;
        
        // Draw in reverse
        path_star.style.strokeDashoffset = pathLength - drawLength;
            
        // When complete, remove the dash array, otherwise shape isn't quite sharp
        // Accounts for fuzzy math
        
        if (scrollPercentage >= 0.99) {
            path_star.style.strokeDasharray = "none";
            
        } else {
            path_star.style.strokeDasharray = pathLength + ' ' + pathLength;
        }

        if(scrollPercentage <= 0.01 || scrollPercentage >=  0.99) {
            path_star.style.display  = "none"
        }
        else {
            path_star.style.display  = "block"
        }
        
        if(scrollPercentage <= 0.01) {
            down_icon.style.display  = "block"
        }
        else {
            down_icon.style.display  = "none"
        }

        if(scrollPercentage <= 0.99) {
            background_blur.style.display  = "block"
        }
        else {
            background_blur.style.display  = "none"
        }
        //https://uxwing.com/hand-finger-down-icon/
    
    }

}
