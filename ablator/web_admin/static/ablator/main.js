$(document).ready(function () {
    reloadFunctionalityPage();
    window.setInterval(reloadFunctionalityPage, 1000);
});

function reloadFunctionalityPage() {
    reloadEnabledUsersCount();
    reloadLogWindow();
}

function reloadEnabledUsersCount() {
    var enabledUsersDiv = $('#functionality-enabled-users');
    if (enabledUsersDiv) {
        $.get(enabledUsersDiv.attr("data-id"), function (data) {
            enabledUsersDiv.html(data);
        });
    }
}

function reloadLogWindow() {
    var logWindow = $("#log-window");
    if (logWindow) {
        $.get(logWindow.attr("data-id"), function (data) {
            logWindow.html(data);
        });
    }
}