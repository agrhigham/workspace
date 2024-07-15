function filter(executionContext) {
    var formContext = executionContext.getFormContext();

    var selected_colour = formContext.getAttribute("arth_colour").getValue();

    console.log("Selected colour:", selected_colour);

    var shadeField = formContext.getControl("arth_shade");
    
    var optionsToAdd = {
        478930000: [
            { value: 478930000, text: "Scarlet" },
            { value: 478930001, text: "Burgundy" }
        ],
        478930001: [
            { value: 478930002, text: "Navy Blue" },
            { value: 478930003, text: "Sky Blue" }
        ],
        478930002: [
            { value: 478930004, text: "Emerald" },
            { value: 478930005, text: "Bogey" }
        ]
    };

    if (optionsToAdd[selected_colour]) {
        
        shadeField.clearOptions();

        optionsToAdd[selected_colour].forEach(function(option) {
            shadeField.addOption(option);
        });
    } else {
        console.log("Selected colour does not match predefined values.");
    }
}