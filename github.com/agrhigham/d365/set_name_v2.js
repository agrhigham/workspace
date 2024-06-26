function GetSet(executionContext) {

    var formContext = executionContext.getFormContext();
    
    var date = formContext.getAttribute("arth_par").getValue();
    
    var string = date.toString();
    
    formContext.getAttribute("arth_testtext").setValue(string);
    
    }