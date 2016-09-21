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
var $c = new Config(condition, counterbalance);

// Initalize psiturk object
var psiTurk = new PsiTurk(uniqueId, adServerLoc, mode);

console.log(d3.rgb(d3.lab(44.55407937199547, 62.70600838856094, 32.35534334585406)));

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
var isTrial = false;

// Used to loop back around the instruction trials.
var instructionIterator = 0;
var expIterator = 0;

setupExpEvents();

/*************************
 * Trial Code       
 *************************/

/* Handles when a word option is clicked */
function optionClicked(optionID) {
    assert(optionID == "#left-option" || optionID == "#right-option", "optionID is set to " + optionID + "and not #left-option or #right-option as expected");
    assert(isTrial == true || isTrial ==false, "isTrial is set to " + isTrial + "not true or false as expected.");
    
    setStateDisplay("recenter");

    if (isTrial) {
        psiTurk.recordTrialData({ // Record the response for this trial
            'trialNum': expIterator,
            'word': $(optionID + "-text").html(),
            'color': $(optionID).css("background-color")
            // start time,end time for the trial and for the experiment as a whole
            // trialID
            //
        });

        expIterator++;

        if (expIterator >= $c.expTrials.length) {
            currentview = new Debriefing();
        } else {
            updateProgress(expIterator, $c.expTrials.length);
            setTestCase();
        }
    } else {
        instructionIterator++;

        if (instructionIterator >= $c.practiceTrials.length ) {
            instructionIterator = 0;
        }

        setTestCase();
    }
}

/* Resets the page to its defaults when the page is refreshed. */
function resetPage() {
    setStateDisplay("recenter");
    updateProgress(expIterator, $c.expTrials.length);
    setTestCase();
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
    assert(state == "recenter" || state == "testCase", "State is set to " + state + "not recenter or testCase as expected");

    switch (state) {
        case "recenter":
            // Things to hide
            $("#task-instructions").css("display", "none");
            $("#shape-image").css("display", "none");
            $("#left-option-container").css("display", "none");
            $("#right-option-container").css("display", "none");

            // Things to show
            $("#recenter-instructions").css("display", "block");
            $("#recenter-shape").css("display", "block");

            // Fine tune layout
            $("#options-container").css("marginTop", "185px");
            
            break;
        case "testCase":
            // Things to hide
            $("#recenter-instructions").css("display", "none");
            $("#recenter-shape").css("display", "none");

            // Things to show
            $("#task-instructions").css("display", "block");
            $("#shape-image").css("display", "inline");
            $("#left-option-container").css("display", "block");
            $("#right-option-container").css("display", "block");

            // Fine tune layout
            $("#options-container").css("marginTop", "20px");

            break;
        default:
            console.log("State is set to " + state + "not recenter or testCase as expected")
    }
}

/* Sets the image and name options given the instructionIterator. */
function setTestCase() {
    assert(isTrial == true || isTrial == false, "isTrial is set to " + isTrial + "not true or false as expected");
    var i = 0;

    if (!isTrial) { // when it is the instructions example
        i = instructionIterator;
        $("#shape-image").attr("src", "/static/images/shapes/" + $c.practiceTrials[i].shape_filename);
    } else { // when it is a real trial
        i = expIterator;
        $("#shape-image").attr("src", "/static/images/shapes/" + $c.expTrials[i].shape_filename);
    }

    switch(counterbalance) {
        case "0":
            $("#left-option").css("background-color", $c.expTrials[i].rgb1);
            $("#right-option").css("background-color", $c.expTrials[i].rgb2);
            $("#left-option").html($c.expTrials[i].word1);
            $("#right-option").html($c.expTrials[i].word2);
            break;
        case "1":
            $("#left-option").css("background-color", $c.expTrials[i].rgb2);
            $("#right-option").css("background-color", $c.expTrials[i].rgb1);
            $("#left-option").html($c.expTrials[i].word1);
            $("#right-option").html($c.expTrials[i].word2);
            break;
        case "2":
            $("#left-option").css("background-color", $c.expTrials[i].rgb1);
            $("#right-option").css("background-color", $c.expTrials[i].rgb2);
            $("#left-option").html($c.expTrials[i].word2);
            $("#right-option").html($c.expTrials[i].word1);
            break;
        case "3":
            $("#left-option").css("background-color", $c.expTrials[i].rgb2);
            $("#right-option").css("background-color", $c.expTrials[i].rgb1);
            $("#left-option").html($c.expTrials[i].word2);
            $("#right-option").html($c.expTrials[i].word1);
            break;
        default:
            console.log("counterbalance is " + counterbalance + " and not in range (0, 3) as expected.");
    }
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

/*************************
 * Debriefing Code       
 *************************/

var Debriefing = function() {

    var error_message = "<h1>Oops!</h1><p>Something went wrong submitting your HIT. This might happen if you lose your internet connection. Press the button to resubmit.</p><button id='resubmit'>Resubmit</button>";

    prompt_resubmit = function() {
        replaceBody(error_message);
        $("#resubmit").click(resubmit);
    };

    resubmit = function() {
        replaceBody("<h1>Trying to resubmit...</h1>");
        reprompt = setTimeout(prompt_resubmit, 10000);
        
        psiTurk.saveData({
            success: function() {
                clearInterval(reprompt); 
                psiTurk.completeHIT();
            }, 
            error: prompt_resubmit
        });
    };

    psiTurk.showPage('debriefing.html');
    
    $("#finishHit").click(function () {
        psiTurk.saveData({
            success: function(){
                psiTurk.completeHIT();
            }, 
            error: prompt_resubmit
        });
    });
}

// --------------------------------------------------------------------
// --------------------------------------------------------------------

/*******************
 * Run Task
 ******************/

 var colorExperiment = function() {
    isTrial = true;
    psiTurk.showPage("stage.html");
    resetPage();
};

$(window).load(function() {
    psiTurk.recordUnstructuredData("condition", condition);
    psiTurk.recordUnstructuredData("counterbalance", counterbalance);

    psiTurk.doInstructions(
        instructionPages,
        function() { currentview = new colorExperiment(); }
    );
});
