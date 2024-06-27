function GetSet(executionContext) {

    var formContext = executionContext.getFormContext();

    var active_stage = formContext.data.process.getActiveStage();

    var string = active_stage.getName();

    formContext.getAttribute("description").setValue(string);

    formContext.data.process.addOnStageChange(function (set_stage) {

        var active_stage = formContext.data.process.getActiveStage();

        var string = active_stage.getName();

        formContext.getAttribute("description").setValue(string);
    });
}