function performActionOnFocusedTabRecord() {    
    
    var focusedSession = Microsoft.Apm.getFocusedSession();
    if (!focusedSession) {
        throw new Error("No focused session is available.");
    }

    var focusedTab = focusedSession.getFocusedTab();
        if (!focusedTab) {
            throw new Error("No focused tab is available within the focused session.");
        }

        var recordId = focusedTab.entityId;

        console.log("Focused Record ID: ", recordId);

}