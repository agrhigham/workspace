function GetSet(primaryControl) {

    var formContext = primaryControl;

    var id = formContext.data.entity.getId();

    var total_gir = 0;
    var total_agir = 0;
    var total_putts = 0;

    var filterQuery = "?$select=arth_greeninregulation,arth_adjustedgreeninregulation,arth_numberofputts&$filter=_arth_round_value eq " + id;

    Xrm.WebApi.retrieveMultipleRecords("arth_hole", filterQuery).then(
        function success(result) {
            for (var i = 0; i < result.entities.length; i++) {
                // Log the entity for debugging
                console.log(result.entities[i]);

                var gir = result.entities[i].arth_greeninregulation;

                if (gir == "Yes") {
                    total_gir += 1;
                }

                var agir = result.entities[i].arth_adjustedgreeninregulation;

                if (agir == "Yes") {
                    total_agir += 1;
                }

                var numberOfPutts = result.entities[i].arth_numberofputts;

                if (!isNaN(numberOfPutts)) {
                    total_putts += numberOfPutts;
                }
            }

                formContext.getAttribute("arth_greeninregulation").setValue(total_gir);
                formContext.getAttribute("arth_adjustedgreeninregulation").setValue(total_agir);
                formContext.getAttribute("arth_puttsthisround").setValue(total_putts);
        },
        // Log error message if filter fails
        function error(error) {
            console.log(error.message);
        }
    );
}