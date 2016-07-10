/*
 * Hunter Leise
 * Color Research JavaScript
*/

/* Anonymous function for the "module patttern", so no global variables are introduced */
(function() {
    "use strict";

    var timer = null;
    var time = 0;
    var caseIterator = 0;
    var testSetOne = ["Takete", "Bouba", "Tikubo", "Maluma"];
    var testSetTwo = ["Tekete", "Boaba", "Takehbi", "Maloma"];

    /* Setup when the page is loaded */
    window.onload = function() {
        resetPage();

        $("option-one").onclick = optionClicked;
        $("option-two").onclick = optionClicked;
        $("recenter-shape").onmouseenter = startTimer;
        $("recenter-shape").onmouseleave = stopTimer;
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

        $("option-one").style.borderColor = randomColor;
        $("option-two").style.borderColor = randomColor;

        if (randomDarker == 0) {
            $("option-one").style.filter = "brightness(90%)";
        } else {
            $("option-two").style.filter = "brightness(90%)";
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
        $("recenter-shape-filling").style.top = (9 - fillingRadius) + "px";
        $("recenter-shape-filling").style.height = fillingDiameter + "px";
        $("recenter-shape-filling").style.width = fillingDiameter + "px";
        $("recenter-shape-filling").style.borderRadius = fillingRadius + "px";
        $("recenter-shape-filling").style.MozBorderRadius = fillingRadius + "px";
        $("recenter-shape-filling").style.webkitBorderRadius = fillingRadius + "px";
    }

    /* Changes the display settings for either the "recenter" or "testCase" state */
    function setStateDisplay(state) {
        switch (state) {
            case "recenter":
                $("case-instructions").style.display = "none";
                $("recenter-instructions").style.display = "block";
                $("recenter-shape").style.display = "block";

                $("shape-image").style.display = "none";
                $("option-one").style.display = "none";
                $("option-two").style.display = "none";

                $("options-container").style.marginTop = "185px";
                $("option-one").style.filter = "brightness(100%)";
                $("option-two").style.filter = "brightness(100%)";

                break;
            case "testCase":
                $("case-instructions").style.display = "block";
                $("recenter-instructions").style.display = "none";
                $("recenter-shape").style.display = "none";

                $("shape-image").style.display = "inline";
                $("option-one").style.display = "block";
                $("option-two").style.display = "block";

                $("options-container").style.marginTop = "20px";

                break;
            default:
                console.log("State sent to setStateDisplay isn't valid.")
        }
    }

    /* Sets the image and name options given the caseIterator. */
    function setTestCase() {
        $("shape-image").src = "Images/" + caseIterator + ".png";
        $("option-one").innerHTML = testSetOne[caseIterator];
        $("option-two").innerHTML = testSetTwo[caseIterator];
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

    /* Shorthand method for calling document.getElementById */
    function $(id) {
        return document.getElementById(id);
    }

}) ();