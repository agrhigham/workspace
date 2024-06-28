function GetSet(executionContext) {

    var formContext = executionContext.getFormContext();
    
    var name = formContext.getAttribute("arth_name").getValue();
    
    formContext.getAttribute("arth_testtext").setValue(name);
    
    }