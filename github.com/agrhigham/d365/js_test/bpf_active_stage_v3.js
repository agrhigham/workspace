function UpdateDescriptionWithActiveStage(executionContext) {
    var formContext = executionContext.getFormContext();
    
    // Function to set the description field with the name of the active stage
    function setActiveStageName() {
        var activeStage = formContext.data.process.getActiveStage();
        
        if (activeStage) {
            var activeStageName = activeStage.getName();
            formContext.getAttribute("description").setValue(activeStageName);
        }
    }

    // Set the description field on form load
    setActiveStageName();

    // Add an event listener for stage change, and update the description field
    formContext.data.process.addOnStageChange(function() {
        setActiveStageName();
    });
}