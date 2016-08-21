/* config.js
 * 
 * This file contains the code necessary to load the configuration
 * for the experiment.
 */

// Object to hold the experiment configuration. It takes as parameters
// the numeric codes representing the experimental condition and
// whether the trials are counterbalanced.
var Config = function (condition, counterbalance) {
    // These are the condition and counterbalancing ids
    this.condition = condition;
    this.counterbalance = counterbalance;
    
    // List of trial information object for each experiment phase
    this.practiceTrials = new Object();
    this.expTrials = new Object();
     
    // Parse the JSON object that we've requested and load it into the
    // configuration
    this.parse_config = function (data) {
        this.experimentName = "colorExperiment";
        this.practiceTrials = _.shuffle(data["practiceTrials"]);
        this.expTrials = _.shuffle(data["expTrials"]);
    };

    // Load the experiment configuration from the server
    this.load_config = function () {
        var that = this;
        $.ajax({
            dataType: "json",
            url: "/static/json/trial-set-" + condition + ".json",
            async: false,
            success: function (data) { 
                if (that.debug) {
                    console.log("Got configuration data");
                }
                that.parse_config(data);
            }
        });
    };

    // Request from the server configuration information for this run
    // of the experiment
    this.load_config();
};