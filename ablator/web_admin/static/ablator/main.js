$(document).ready(function () {
    reloadLogWindow();
    window.setInterval(reloadFunctionalityPage, 1000);
});

function reloadFunctionalityPage() {
    reloadLogWindow();
};

function reloadLogWindow() {
    var logWindow = $("#log-window");
    if (logWindow) {
        $.get(logWindow.attr("data-id"), function (data) {
            logWindow.html(data);
        });
    }
};