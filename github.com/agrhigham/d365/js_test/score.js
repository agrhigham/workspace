function AddScore(executionContext) {
    var formContext = executionContext.getFormContext();
    var total_score = 0;

    // Fetch and check 'arth_professionalgreeting' attribute
    var professionalAttr = formContext.getAttribute("arth_professionalgreeting");
    var professional = professionalAttr ? professionalAttr.getText() : null;

    // Fetch and check 'arth_datapolicy' attribute
    var dataPolicyAttr = formContext.getAttribute("arth_dataprotectioncompliance");
    var data_policy = dataPolicyAttr ? dataPolicyAttr.getText() : null;

    // Score calculation based on the string values of choice fields
    if (professional === "Yes") {  
        total_score += 1;
    }

    if (data_policy === "Yes") {  
        total_score += 1;
    }

    // Setting the score, converting to string if needed
    formContext.getAttribute("arth_score").setValue(total_score.toString());
}