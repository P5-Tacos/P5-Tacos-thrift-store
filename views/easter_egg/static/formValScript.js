console.log("it is alive");
function inc(element, increment_numb, item, max) {
    let el = document.querySelector(`[name="${element}"]`); //differentiates between items
    if (el.value >= max){ //when the input is maxed pressed one over max
        console.log(String(el));
        //max number of items that one can purchase
        el.value = max;

        //constructs the error message based on the item that was passed in
        document.getElementById("error_msg" + increment_numb).innerHTML = "cannot purchase more than "+ max + " "+ item +"(s)";

        //allows error messages to fade out after a certain time
        setTimeout(function(){ document.getElementById("error_msg" + increment_numb).innerHTML =""; }, 3000);
    } else {
        console.log(String(el));
        //incrementing by +1
        el.value = parseInt(el.value) + 1;
    }
}

function dec(element, increment_numb) {
    let el = document.querySelector(`[name="${element}"]`); //differentiates between items
    if (parseInt(el.value) > 0) { //if the item count is greater than 0
        console.log(String(el));

        //decrement the count by 1
        el.value = parseInt(el.value) - 1;

        //takes away the error message
        document.getElementById("error_msg" + increment_numb).innerHTML = "";
    }
}

var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

function showTab(n) {
    // This function will display the specified tab of the form...
    var x = document.getElementsByClassName("tab");
    x[n].style.display = "block";
    //... and fix the Previous/Next buttons:
    if (n == 0) {
        document.getElementById("prevBtn").style.display = "none";
    } else {
        document.getElementById("prevBtn").style.display = "inline";
    }
    if (n == (x.length - 1)) {
        document.getElementById("nextBtn").innerHTML = "Submit";
    } else {
        document.getElementById("nextBtn").innerHTML = "Next";
    }
    //... and run a function that will display the correct step indicator:
    fixStepIndicator(n)
}

function nextPrev(n) {
    // This function will figure out which tab to display
    var x = document.getElementsByClassName("tab");
    // Exit the function if any field in the current tab is invalid:
    if (n == 1 && !validateForm()) return false;
    // Hide the current tab:
    x[currentTab].style.display = "none";
    // Increase or decrease the current tab by 1:
    currentTab = currentTab + n;
    // if you have reached the end of the form...
    if (currentTab >= x.length) {
        // ... the form gets submitted:
        document.getElementById("regForm").submit();
        return false;
    }
    // Otherwise, display the correct tab:
    showTab(currentTab);
}

function validateForm() {
    // This function deals with validation of the form fields
    var x, y, i, valid = true;
    x = document.getElementsByClassName("tab");
    y = x[currentTab].getElementsByTagName("input");
    // A loop that checks every input field in the current tab:
    for (i = 0; i < y.length; i++) {
        // If a field is empty...
        if (y[i].value == "") {
            // add an "invalid" class to the field:
            y[i].className += " invalid";
            // and set the current valid status to false
            valid = false;
        }
    }
    // If the valid status is true, mark the step as finished and valid:
    if (valid) {
        document.getElementsByClassName("step")[currentTab].className += " finish";
    }
    return valid; // return the valid status
}

function snackValidate() {

}

function fixStepIndicator(n) {
    // This function removes the "active" class of all steps...
    var i, x = document.getElementsByClassName("step");
    for (i = 0; i < x.length; i++) {
        x[i].className = x[i].className.replace(" active", "");
    }
    //... and adds the "active" class on the current step:
    x[n].className += " active";
}
/*
    function inc(element) {
        let el = document.querySelector(`[name="${element}"]`);
        el.value = parseInt(el.value) + 1;
    }

    function dec(element) {
        let el = document.querySelector(`[name="${element}"]`);
        if (parseInt(el.value) > 0) {
            el.value = parseInt(el.value) - 1;
        }
    }*/