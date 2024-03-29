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

var fillingTimer = null;
var trialTimer = null;
var fillingTime = 0;
var trialTime = 0.0;
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

    stopTrialTimer();
    setStateDisplay("recenter");

    if (isTrial) {
        psiTurk.recordTrialData({ // Record the response for this trial
            'trialNum': expIterator,
            'shapeFilename': $c.expTrials[expIterator].shapeFilename,
            'leftWord': $("#left-option").html(),
            'rightWord': $("#right-option").html(),
            'leftColor': $("#left-option").css("background-color"),
            'rightColor': $("#right-option").css("background-color"),
            'hVar': $c.expTrials[expIterator].hVar,
            'cVar': $c.expTrials[expIterator].cVar,
            'lVar': $c.expTrials[expIterator].lVar,
            'perturbedSide': $("#left-option").css("background-color") === "rgb(218, 55, 67)" ? 'right' : 'left',
            'selectedWord': $(optionID).html(),
            'selectedColor': $(optionID).css("background-color"),
            'selectedSide': optionID === "#left-option" ? 'left' : 'right',
            'wordType': $c.expTrials[expIterator].wordType,
            'shapeType': $c.expTrials[expIterator].shapeType,
            'trialTime': trialTime.toFixed(2)
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
            setStateDisplay("practiceFinished");
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
    $("#recenter-shape-filling")
        .css("top", (9 - fillingRadius) + "px")
        .css("height", fillingDiameter + "px")
        .css("width", fillingDiameter + "px")
        .css("borderRadius", fillingRadius + "px");
}

/* Changes the display settings for either the "recenter" or "testCase" state */
function setStateDisplay(state) {
    assert(state == "recenter" || state == "testCase" || state == "practiceFinished", "State is set to " + state + "not recenter, testCase, practiceFinished as expected");

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

            startTrialTimer();

            break;
        case "practiceFinished":
            // Things to hide
            $("#task-instructions").css("display", "none");
            $("#shape-image").css("display", "none");
            $("#left-option-container").css("display", "none");
            $("#right-option-container").css("display", "none");
            $("#recenter-instructions").css("display", "none");
            $("#recenter-shape").css("display", "none");

            // Things to show
            $("#practice-finished").css("display", "block");

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
        $("#shape-image").attr("src", "/static/images/shapes/" + $c.practiceTrials[i].shapeFilename);

        switch(counterbalance) {
            case "0":
                $("#left-option")
                    .css("background-color", $c.practiceTrials[i].rgb1)
                    .html($c.practiceTrials[i].word1);
                $("#right-option")
                    .css("background-color", $c.practiceTrials[i].rgb2)
                    .html($c.practiceTrials[i].word2);
                break;
            case "1":
                $("#left-option")
                    .css("background-color", $c.practiceTrials[i].rgb2)
                    .html($c.practiceTrials[i].word1);
                $("#right-option")
                    .css("background-color", $c.practiceTrials[i].rgb1)
                    .html($c.practiceTrials[i].word2);
                break;
            case "2":
                $("#left-option")
                    .css("background-color", $c.practiceTrials[i].rgb1)
                    .html($c.practiceTrials[i].word2);
                $("#right-option")
                    .css("background-color", $c.practiceTrials[i].rgb2)
                    .html($c.practiceTrials[i].word1);
                break;
            case "3":
                $("#left-option")
                    .css("background-color", $c.practiceTrials[i].rgb2)
                    .html($c.practiceTrials[i].word2);
                $("#right-option")
                    .css("background-color", $c.practiceTrials[i].rgb1)
                    .html($c.practiceTrials[i].word1);
                break;
            default:
                console.log("counterbalance is " + counterbalance + " and not in range (0, 3) as expected.");
        }
    } else { // when it is a real trial
        i = expIterator;
        $("#shape-image").attr("src", "/static/images/shapes/" + $c.expTrials[i].shapeFilename);

        switch(counterbalance) {
            case "0":
                $("#left-option")
                    .css("background-color", $c.expTrials[i].rgb1)
                    .html($c.expTrials[i].word1);
                $("#right-option")
                    .css("background-color", $c.expTrials[i].rgb2)
                    .html($c.expTrials[i].word2);
                break;
            case "1":
                $("#left-option")
                    .css("background-color", $c.expTrials[i].rgb2)
                    .html($c.expTrials[i].word1);
                $("#right-option")
                    .css("background-color", $c.expTrials[i].rgb1)
                    .html($c.expTrials[i].word2);
                break;
            case "2":
                $("#left-option")
                    .css("background-color", $c.expTrials[i].rgb1)
                    .html($c.expTrials[i].word2);
                $("#right-option")
                    .css("background-color", $c.expTrials[i].rgb2)
                    .html($c.expTrials[i].word1);
                break;
            case "3":
                $("#left-option")
                    .css("background-color", $c.expTrials[i].rgb2)
            .html($c.expTrials[i].word2);
                $("#right-option")
                    .css("background-color", $c.expTrials[i].rgb1)
                    .html($c.expTrials[i].word1);
                break;
            default:
                console.log("counterbalance is " + counterbalance + " and not in range (0, 3) as expected.");
        }
    }
}

/* Starts the filling timer */
function startFillingTimer() {
    if (!fillingTimer) {
        fillingTime = 0;
        setCenterFilling(0);
        fillingTimer = setInterval(fillingTick, 25);
    }
}

/* Stops the filling timer */
function stopFillingTimer() {
    clearInterval(fillingTimer);
    fillingTimer = null;
    setCenterFilling(0);
}

/* Changes the recenter shape filling size during each tick. */
function fillingTick() {
    if (fillingTime < 10) {
        fillingTime++;
        setCenterFilling(fillingTime);
    } else {
        stopFillingTimer();
        setStateDisplay("testCase");
    }
}

/* Starts the trial timer */
function startTrialTimer() {
    if (!trialTimer) {
        trialTime = 0;
        trialTimer = setInterval(function() { trialTime += 0.1 }, 100); // Increments the trial time every tenth of a second
    }
}

/* Stops the trial timer */
function stopTrialTimer() {
    clearInterval(trialTimer);
    trialTimer = null;
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
        psiTurk.recordUnstructuredData('endTime', Math.floor(Date.now() / 1000));
        psiTurk.saveData({
            success: function(){
                psiTurk.completeHIT();
            }, 
            error: prompt_resubmit
        });
    });
};

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
    psiTurk.recordUnstructuredData('condition', condition);
    psiTurk.recordUnstructuredData('counterbalance', counterbalance);
    psiTurk.recordUnstructuredData('startTime', Math.floor(Date.now() / 1000));

    psiTurk.doInstructions(
        instructionPages,
        function() { currentview = new colorExperiment(); }
    );
});
