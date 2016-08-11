/* task.js
 * 
 * This file holds the main experiment code.
 * 
 * Requires:
 *   config.js
 *   psiturk.js
 *   utils.js
 */

// Create and initialize the experiment configuration object
//var $c = new Config(condition, counterbalance);

// Initalize psiturk object
var psiTurk = new PsiTurk(uniqueId, adServerLoc, mode);

// All pages to be loaded
var pages = [
    "instructions/instruct-1.html",
    "instructions/instruct-2.html",
    "stage.html",
    "debriefing.html"
];

psiTurk.preloadPages(pages);

var instructionPages = [ // add as a list as many pages as you like
    "instructions/instruct-1.html",
    "instructions/instruct-2.html"
];

var timer = null;
var time = 0;
var caseIterator = 0;
var testSetOne = ["Takete", "Bouba", "Tikubo", "Maluma"];
var testSetTwo = ["Tekete", "Boaba", "Takehbi", "Maloma"];

/*************************
 * INSTRUCTIONS         
 *************************/

var colorExperiment = function() {
    psiTurk.showPage("stage.html");
    resetPage();
    next();
};

/* Returns a random color name */
    function getRandomColor() {
        var colors = ["Aqua","Aquamarine","Black", "BlanchedAlmond","Blue","BlueViolet","Brown","BurlyWood","CadetBlue","Chartreuse","Chocolate","Coral","CornflowerBlue","Crimson","Cyan","DarkBlue","DarkCyan","DarkGoldenRod","DarkGray","DarkGrey","DarkGreen","DarkKhaki","DarkMagenta","DarkOliveGreen","Darkorange","DarkOrchid","DarkRed","DarkSalmon","DarkSeaGreen","DarkSlateBlue","DarkSlateGray","DarkSlateGrey","DarkTurquoise","DarkViolet","DeepPink","DeepSkyBlue","DimGray","DimGrey","DodgerBlue","FireBrick","ForestGreen","Fuchsia","Gold","GoldenRod","Gray","Grey","Green","GreenYellow","HotPink","IndianRed","Indigo","Khaki","LawnGreen","Lime","LimeGreen","Magenta","Maroon","MediumAquaMarine","MediumBlue","MediumOrchid","MediumPurple","MediumSeaGreen","MediumSlateBlue","MediumSpringGreen","MediumTurquoise","MediumVioletRed","MidnightBlue","Moccasin","NavajoWhite","Navy","Olive","OliveDrab","Orange","OrangeRed","Orchid","PaleGoldenRod","PaleGreen","PaleTurquoise","PaleVioletRed","PeachPuff","Peru","Pink","Plum","PowderBlue","Purple","Red","RosyBrown","RoyalBlue","SaddleBrown","Salmon","SandyBrown","SeaGreen","Sienna","Silver","SkyBlue","SlateBlue","SlateGray","SlateGrey","SpringGreen","SteelBlue","Tan","Teal","Thistle","Tomato","Turquoise","Violet","Wheat","YellowGreen"];
        return colors[Math.floor(Math.random() * colors.length)];
    }

    /* Handles when a word option is clicked */
    function optionClicked() {
        setStateDisplay("recenter");
        randomizeOptionColors();

        if (caseIterator >= 3 ) {
            caseIterator = 0;
        } else {
            caseIterator++;
        }

        setTestCase();
    }

    /* Sets random colors for the text and border of both name options */
    function randomizeOptionColors() {
        var randomColor = getRandomColor();
        var randomDarker = Math.floor(Math.random() * 2);

        $("#option-one").css("borderColor", randomColor);
        $("#option-two").css("borderColor", randomColor);

        if (randomDarker == 0) {
            $("#option-one").css("filter", "brightness(90%)");
            $("#option-one").css("WebkitFilter", "brightness(90%)");
        } else {
            $("#option-two").css("filter", "brightness(90%)");
            $("#option-two").css("WebkitFilter", "brightness(90%)");
        }
    }

    /* Resets the page to its defaults when the page is refreshed. */
    function resetPage() {
        setStateDisplay("recenter");
        setTestCase();
        randomizeOptionColors();
    }

    /* Changes the size of the recenter shape filling */
    function setCenterFilling(fillingRadius) {
        var fillingDiameter = fillingRadius * 2;
        $("#recenter-shape-filling").css("top", (9 - fillingRadius) + "px");
        $("#recenter-shape-filling").css("height", fillingDiameter + "px");
        $("#recenter-shape-filling").css("width", fillingDiameter + "px");
        $("#recenter-shape-filling").css("borderRadius", fillingRadius + "px");
    }

    /* Changes the display settings for either the "recenter" or "testCase" state */
    function setStateDisplay(state) {
        switch (state) {
            case "recenter":
                $("#case-instructions").css("display", "none");
                $("#recenter-instructions").css("display", "block");
                $("#recenter-shape").css("display", "block");

                $("#shape-image").css("display", "none");
                $("#option-one-container").css("display", "none");
                $("#option-two-container").css("display", "none");

                $("#options-container").css("marginTop", "185px");
                $("#option-one").css("filter", "brightness(100%)");
                $("#option-one").css("WebkitFilter", "brightness(100%)");
                $("#option-two").css("filter", "brightness(100%)");
                $("#option-two").css("WebkitFilter", "brightness(100%)");
                
                break;
            case "testCase":
                $("#case-instructions").css("display", "block");
                $("#recenter-instructions").css("display", "none");
                $("#recenter-shape").css("display", "none");

                $("#shape-image").css("display", "inline");
                $("#option-one-container").css("display", "block");
                $("#option-two-container").css("display", "block");

                $("#options-container").css("marginTop", "20px");

                break;
            default:
                console.log("State sent to setStateDisplay isn't valid.")
        }
    }

    /* Sets the image and name options given the caseIterator. */
    function setTestCase() {
        $("#shape-image").attr("src", "/static/images/instruct-" + caseIterator + ".svg");
        $("#option-one-text").html(testSetOne[caseIterator]);
        $("#option-two-text").html(testSetTwo[caseIterator]);
    }

    /* Starts the timer */
    function startTimer() {
        if (!timer) {
            time = 0;
            setCenterFilling(0);
            timer = setInterval(tick, 50);
        }
    }

    /* Stops the timer */
    function stopTimer() {
        clearInterval(timer);
        timer = null;
        setCenterFilling(0);
    }

    /* Changes the recenter shape filling size during each tick. */
    function tick() {
        if (time < 10) {
            time++;
            setCenterFilling(time);
        } else {
            stopTimer();
            setStateDisplay("testCase");
        }
    }



// --------------------------------------------------------------------
// --------------------------------------------------------------------

/*******************
 * Run Task
 ******************/

$(window).load(function() {
    psiTurk.doInstructions(
        instructionPages,
        function() { currentview = new colorExperiment(); }
    );
});
