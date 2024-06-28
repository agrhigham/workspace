function GetSet(executionContext) {
    
    var formContext = executionContext.getFormContext();
    // Get round record id to filter hole records with
    var id = formContext.data.entity.getId();
    // Initialize a variable to hold the sum of putts
    var total_agir = 0;
   
    var filterQuery = "?$select=arth_greeninregulation&$filter=_arth_round_value eq " + id;
    
    Xrm.WebApi.retrieveMultipleRecords("arth_hole", filterQuery).then(
        function success(result) {
            for (var i = 0; i < result.entities.length; i++) {
                // Log the entity for debugging
                console.log(result.entities[i]);
                // Extract the value of arth_numberofputts and add it to totalPutts
                var agir = result.entities[i].arth_greeninregulation;
                // Check if numberOfPutts is a valid number before adding it
                if (agir == "Yes") {
                    total_agir += 1;
                }
            }
                
                formContext.getAttribute("arth_greeninregulation").setValue(total_agir);

        },
        // Log error message if filter fails
        function error(error) {
            console.log(error.message);
        }
    );
}