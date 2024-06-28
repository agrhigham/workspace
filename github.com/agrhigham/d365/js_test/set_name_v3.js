function GetSet(executionContext) {

    var formContext = executionContext.getFormContext();

    var name = formContext.getAttribute("arth_name").getValue();
    
    var number = formContext.getAttribute("arth_par").getValue();
    
    var string = number.toString();

    var field_value = `${name}-${string}`
    
    formContext.getAttribute("arth_testtext").setValue(field_value);
    
    }