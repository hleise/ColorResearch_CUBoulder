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
        

    // Whether debug information should be printed out
    this.debug = true; // TODO turn off
    // The amount of time to fade HTML elements in/out
    this.fade = 200;
    // List of trial information object for each experiment phase
    this.trials = new Object();
     
    // Parse the JSON object that we've requested and load it into the
    // configuration
    this.parse_config = function (data) {
        // original_filename
        // image1_filename
        // image2_filename
        // image3_filename
        // is_l1
        // is_l2
        // is_ms_ssim
        var nTotalTrial = 50;
        this.experimentName = "colorExperiment";
        var all_trials = data["trialHolder"];
        var practice_trials = all_trials.slice(nTotalTrial);
        var exp_trials = all_trials.slice(0,nTotalTrial);
        var exp_trials = _.shuffle(exp_trials);
        
        var randPerm;
        for (i = 0; i < exp_trials.length; i++) { 
            var old_image = [];
            old_image[0] = exp_trials[i].image1_filename;
            old_image[1] = exp_trials[i].image2_filename;
            old_image[2] = exp_trials[i].image3_filename;
            
            // Permute images
            randPerm = _.shuffle([0,1,2]);
            exp_trials[i].image1_filename = old_image[randPerm[0]];
            exp_trials[i].image2_filename = old_image[randPerm[1]];
            exp_trials[i].image3_filename = old_image[randPerm[2]];
            
            exp_trials[i].is_l1 = randPerm[0];
            exp_trials[i].is_l2 = randPerm[1];
            exp_trials[i].is_ms_ssim = randPerm[2];   
        }
        
        this.trials[EXPERIMENT.training] = practice_trials.slice(0, 1);
        this.trials[EXPERIMENT.trial] = exp_trials.slice(0, nTotalTrial);
        
        this.instructions[EXPERIMENT.training].examples = [practice_trials[1], null]; // FIXME
    };

    // Load the experiment configuration from the server
    this.load_config = function () {
        var that = this;
        $.ajax({
            dataType: "json",
            url: "/static/json/trial-set-" + this.condition + ".json",
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