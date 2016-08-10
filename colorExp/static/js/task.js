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
var psiTurk = new PsiTurk(uniqueId, adServerLoc);

// Preload the HTML template pages that we need for the experiment
psiTurk.preloadPages($c.pages);
//psiTurk.preloadImages($c.images);

// Objects to keep track of the current phase and state
var CURRENTVIEW;
var STATE;
var ITEMLIST = ["item1", "item2", "item3"];
var rootpath_orignals = "../static/images/stimuli/";

var timer = null;
var time = 0;
var caseIterator = 0;
var testSetOne = ["Takete", "Bouba", "Tikubo", "Maluma"];
var testSetTwo = ["Tekete", "Boaba", "Takehbi", "Maloma"];

/*************************
 * INSTRUCTIONS         
 *************************/

var Instructions = function() {
    resetPage();

    // The list of pages for this set of instructions
    this.pages = $c.instructions[STATE.experiment_phase].pages;
    // The list of examples on each page of instructions
    this.examples = $c.instructions[STATE.experiment_phase].examples;
    // Time when a page of instructions is presented
    this.timestamp;

    // Display a page of instructions, based on the current
    // STATE.index
    this.show = function() {

        debug("show slide " + this.pages[STATE.index]);

        // Load the next page of instructions
        $(".slide").hide();
        var slide = $("#" + this.pages[STATE.index]);
        slide.fadeIn($c.fade);

        // Update the URL hash
        STATE.set_hash();

        this.example = this.examples[STATE.index];
	if (this.example) {
        $("#option-one-text").html("Hello");
        $("#option-two-text").html("World");
	}
	    
        // Bind a handler to the "next" button. We have to wrap it in
        // an anonymous function to preserve the scope.
        var that = this;
        slide.find('.next').click(function () {
            that.record_response();
        });

        // Record the time that an instructions page is presented
        this.timestamp = new Date().getTime();
    };

    // Handler for when the "next" button is pressed
    this.record_response = function() {

        // Calculate the response time
        var rt = (new Date().getTime()) - this.timestamp;
        debug("'Next' button pressed");

        // Record the data. The format is: 
        // experiment phase, instructions, index, trial_phase, response time
        var data = new DataRecord();
        data.update(STATE.as_data());
        data.update(this.examples[STATE.index]);
        data.update({response: "", response_time: rt, start_time: this.timestamp});
        psiTurk.recordTrialData(data);
        debug(data);

        // Go to the next page of instructions, or complete these
        // instructions if there are no more pages
        if ((STATE.index + 1) >= this.pages.length) {
            this.finish();
        } else {
            STATE.set_index(STATE.index + 1);
            this.show();
        }
    };

    // Clean up the instructions phase and move on to the test phase
    this.finish = function() {
        debug("Done with instructions")

        // Record that the user has finished the instructions and
        // moved on to the experiment. This changes their status
        // code in the database.
	if (STATE.experiment_phase == EXPERIMENT.training) {
            psiTurk.finishInstructions();
	}

        // Reset the state object for the test phase
        STATE.set_instructions(0);
        STATE.set_index();
        STATE.set_trial_phase();
        CURRENTVIEW = new TestPhase();
    };

    // Display the first page of instructions
    this.show();
};



/*****************
 *  TRIALS       *
 *****************/

var TestPhase = function() {
    resetPage();

    /* Instance variables */

    // When the time response period begins
    this.timestamp; 
    // Whether the object is listening for responses
    this.listening = false;

    // List of trials in this block of the experiment
    this.trials = $c.trials[STATE.experiment_phase];
    // Information about the current trial
    this.trialinfo;    
    // The response they gave
    this.response;

    // Handlers to setup each phase of a trial
    this.phases = new Object();

    // Initialize a new trial. This is called either at the beginning
    // of a new trial, or if the page is reloaded between trials.
    this.init_trial = function () {
        debug("Initializing trial " + STATE.index);
        $(".phase").hide();

        // If there are no more trials left, then we are at the end of
        // this phase
        if (STATE.index >= this.trials.length) {
            this.finish();
            return false;
        }
        
        // Load the new trialinfo
        this.trialinfo = this.trials[STATE.index];

        // Update progress bar
        update_progress(STATE.index, this.trials.length);
        
        // Register the response handler to record responses
        var that = this;
        $("#submit-trial-button").click(function(event) {
            var idsInOrder = $("#sortable-images").sortable("toArray");
            that.record_response(idsInOrder);
        });
        return true;
    };

    var loaders = [];
    // Phase 1: show the prompt
    this.phases[TRIAL.prestim] = function(that) {
        $("#phase-container").hide();
        
        // Initialize the trial
        if (that.init_trial()) {
            // Actually show the prestim element
            debug("Show PRESTIM");
            $("#fixation").hide()
            $("#prestim").find("div.question").show()
            $("#prestim").show();
            $("#phase-container").show();
            
            loaders.push(Draw_Image('original-image', rootpath_orignals + that.trialinfo.original_filename));
            loaders.push(Draw_Image('item1-image', rootpath_orignals + that.trialinfo.image1_filename));
            loaders.push(Draw_Image('item2-image', rootpath_orignals + that.trialinfo.image2_filename));
            loaders.push(Draw_Image('item3-image', rootpath_orignals + that.trialinfo.image3_filename));
            
            // Show the stimulus
            STATE.set_trial_phase(STATE.trial_phase + 1);
            that.show();
        }
    };

    // Phase 2: show the stimulus
    this.phases[TRIAL.stim] = function (that) {
        debug("Show STIMULUS");
        // Hide prestim and show stim
        $.when.apply(null, loaders).done(function() {
            // callback when everything was loaded
            show_phase("stim");
            
            var stimuliWidth = $("#item1-image").width();
            $(".original-stimuli").width(stimuliWidth);
            $(".original-stimuli").height(stimuliWidth);
            $(".filler-div").width(stimuliWidth);
            $(".filler-div").height(stimuliWidth);
            $(".filler-div").css('line-height', "" + stimuliWidth + "px")
            
            // Listen for a response
            that.listening = true;
        });
    };

    // Phase 3: show feedback
    this.phases[TRIAL.feedback] = function (that) {
        debug("Show FEEDBACK");
        // Hide stim and show feedback
        show_phase("feedback");
        
        STATE.set_trial_phase();
        STATE.set_index(STATE.index + 1);
        that.show();
    };

    // Show the current trial at the currect phase
    this.show = function () {
        // Update the URL hash
        STATE.set_hash();
        // Call the phase setup handler
        this.phases[STATE.trial_phase](this);
        // Record when this phase started
        this.timestamp = new Date().getTime();
    };

    // Record a response (this could be either just clicking "start",
    // or actually a choice to the prompt(s))
    this.record_response = function(idsInOrder) {
        // If we're not listening for a response, do nothing
        if (!this.listening) return;

        // Record response time
        var rt = (new Date().getTime()) - this.timestamp;

        // Parse the actual value of the data to record
        var ordering = [];
        for (var iItem=0; iItem<ITEMLIST.length; iItem++) {
            ordering[iItem] = ITEMLIST.indexOf(idsInOrder[iItem])
        }
        
        var response = ordering;

        if (response == undefined) return;
        this.listening = false;

        debug("Record response: " + response);

        var data = new DataRecord();
        data.update(this.trialinfo);
        data.update(STATE.as_data());
        data.update({
            start_time: this.timestamp,
            response_time: rt, 
            response: response,
        });

        // Create the record we want to save
        psiTurk.recordTrialData(data);
        debug(data);

        if (STATE.trial_phase == TRIAL.stim) {
            this.response = response;
        }

        // Tell the state to go to the next trial phase or trial
        if (STATE.trial_phase == (TRIAL.length - 1)) {
            STATE.set_trial_phase();
            STATE.set_index(STATE.index + 1);
        } else {
            STATE.set_trial_phase(STATE.trial_phase + 1);
        }            

        // Update the page with the current phase/trial
        this.show();
    };

    // Complete the set of trials in the test phase
    this.finish = function() {
        debug("Finish test phase");

        // Reset the state object for the next experiment phase
	    STATE.set_experiment_phase(STATE.experiment_phase + 1);
        STATE.set_instructions();
        STATE.set_index();
        STATE.set_trial_phase();

        // If we're at the end of the experiment, submit the data to
        // mechanical turk, otherwise go on to the next experiment
        // phase and show the relevant instructions
        if (STATE.experiment_phase >= EXPERIMENT.length) {

            // Show a page saying that the HIT is resubmitting, and
            // show the error page again if it times out or error
            var resubmit = function() {
                $(".slide").hide();
                $("#resubmit_slide").fadeIn($c.fade);

                var reprompt = setTimeout(prompt_resubmit, 10000);
                psiTurk.saveData({
                    success: function() {
                        clearInterval(reprompt); 
                        finish();
                    }, 
                    error: prompt_resubmit
                });
            };

            // Prompt them to resubmit the HIT, because it failed the first time
            var prompt_resubmit = function() {
                $("#resubmit_slide").click(resubmit);
                $(".slide").hide();
                $("#submit_error_slide").fadeIn($c.fade);
            };

            //bdr
            // Render debriefing form
            $(".slide").hide();
            var slide = $("#instructions-debriefing");
            slide.fadeIn($c.fade);
            slide.find('.next').click(function () {
                psiTurk.showPage("submit.html")
                psiTurk.saveData({
                    success: psiTurk.completeHIT, 
                    error: prompt_resubmit
                });
            });

        } else {
            CURRENTVIEW = new Instructions();
        }
    };

    // Load the trial html page
    $(".slide").hide();
    // Show the slide
    $("#trial").fadeIn($c.fade);

    // Initialize the current trial -- we need to do this here in
    // addition to in prestim in case someone refreshes the page in
    // the middle of a trial
    if (this.init_trial()) {
        // Start the test
        this.show();
    };
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
        $("#shape-image").src = "Images/" + caseIterator + ".svg";
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

$(document).ready(function() { 
    // Load the HTML for the trials
    psiTurk.showPage("trial.html");

    // Record various unstructured data
    psiTurk.recordUnstructuredData("condition", condition);
    psiTurk.recordUnstructuredData("counterbalance", counterbalance);
    psiTurk.recordUnstructuredData("choices", $("#choices").html());
    psiTurk.recordUnstructuredData("experimentName", $c.experimentName);

    // Start the experiment
    STATE = new State();

    // Begin the experiment phase
    if (STATE.instructions) {
        CURRENTVIEW = new Instructions();
    } else {
        CURRENTVIEW = new TestPhase();
    }
});
