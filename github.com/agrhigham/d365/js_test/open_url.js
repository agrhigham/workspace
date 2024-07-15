function OpenURL(primaryControl) {

    var formContext = primaryControl;

    var url = formContext.getAttribute("msdyn_url").getValue();

    Xrm.Navigation.openUrl(url);

}
