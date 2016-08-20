/* utils.js
 * 
 * This file contains helper utility functions/objects for use by the
 * main experiment code.
 */

function AssertException(message) { this.message = message; }
AssertException.prototype.toString = function () {
    return 'AssertException: ' + this.message;
};

function assert(exp, message) {
    if (!exp) {
        throw new AssertException(message);
    }
}

// Mean of booleans (true==1; false==0)
function boolpercent(arr) {
    var count = 0;
    for (var i=0; i<arr.length; i++) {
        if (arr[i]) { count++; } 
    }
    return 100* count / arr.length;
}

function setupExpEvents() {
    $(document).on("click", "#left-option", function() {
            optionClicked();
    });
    $(document).on("click", "#right-option", function() {
        optionClicked();
    });
    $(document).on("mouseenter", "#recenter-shape", function() {
        startTimer();
    });
    $(document).on("mouseleave", "#recenter-shape", function() {
        stopTimer();
    });
}

// Update the progress bar based on the current trial and total number
// of trials.
function updateProgress(num, num_trials) {
    var width = 2 + 98 * (num / (num_trials - 1.0));
    $("#indicator-stage").css({"width": width + "%"});
    $("#progress-text").html("Progress " + (num + 1) + "/" + num_trials);
}