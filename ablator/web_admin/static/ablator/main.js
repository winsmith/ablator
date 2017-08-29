$(document).ready(function () {
    reloadFunctionalityPage();
    window.setInterval(reloadFunctionalityPage, 1000);
});

function reloadFunctionalityPage() {
    reloadFunctionalityEnabledUsersCount();
    reloadFunctionalityProgress();
    reloadFunctionalityLogWindow();
}

function reloadFunctionalityEnabledUsersCount() {
    var enabledUsersDiv = $('#functionality-enabled-users');
    if (enabledUsersDiv) {
        $.get(enabledUsersDiv.attr("data-id"), function (data) {
            enabledUsersDiv.html(data);
        });
    }
}

function reloadFunctionalityProgress() {
    var progressSection = $('#functionality-progress');
    if (progressSection) {
        $.get(progressSection.attr("data-id"), function (data) {
            progressSection.html(data);
        });
    }
}

function reloadFunctionalityLogWindow() {
    var logWindow = $("#log-window");
    if (logWindow) {
        $.get(logWindow.attr("data-id"), function (data) {
            logWindow.html(data);
        });
    }
}