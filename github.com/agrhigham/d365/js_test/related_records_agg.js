function GetSet(executionContext) {
    // executionContext gives access to form component and comes with methods to work with data
    var formContext = executionContext.getFormContext();
    // Get round record id to filter hole records with
    var id = formContext.data.entity.getId();
    // Initialize a variable to hold the sum of putts
    var totalPutts = 0;
    // Create variable string to filter hole records matching round id. $select is used to return certain fields
    var filterQuery = "?$select=arth_numberofputts&$filter=_arth_round_value eq " + id;
    // Filter the hole table
    Xrm.WebApi.retrieveMultipleRecords("arth_hole", filterQuery).then(
        function success(result) {
            for (var i = 0; i < result.entities.length; i++) {
                // Log the entity for debugging
                console.log(result.entities[i]);
                // Extract the value of arth_numberofputts and add it to totalPutts
                var numberOfPutts = result.entities[i].arth_numberofputts;
                // Check if numberOfPutts is a valid number before adding it
                if (!isNaN(numberOfPutts)) {
                    totalPutts += numberOfPutts;
                }
            }
                // Set value of putts this round to sum of putts from the rounds holes
                formContext.getAttribute("arth_puttsthisround").setValue(totalPutts);

        },
        // Log error message if filter fails
        function error(error) {
            console.log(error.message);
        }
    );
}