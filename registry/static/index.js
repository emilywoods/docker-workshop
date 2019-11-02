class Dashboard {
    constructor() {
        this.refresh_latest();
        this.create_dashboard();
    }

    create_dashboard(dat) {
       var html = ""
       for (var username in dat) {

        var num_of_containers = Object.keys(dat[username]["containers"]).length
        var success = 0
        var error = 0

        for (var container in dat[username]["containers"]) {
            success += dat[username]["containers"][container]["success"]
            error += dat[username]["containers"][container]["error"]
        }

        var has_errors = error > 0;
        console.log(success)
        console.log(error)
        var domString = `
        <div class="entry">
            <div class="user">${username}</div>
            <div class="containers">Registered Containers: ${num_of_containers}</div>
            <div class="success">Messages Sent: ${success}</div>
            <div class="error has-errors-${has_errors}">Errors: ${error}</div>
        </div>`
        html += domString;
       }
       document.getElementById('dashboard').innerHTML = html;
    }

    refresh_latest() {
        var latest_request = new XMLHttpRequest();
        latest_request.open('GET', '/containers', true);
        var self = this
        latest_request.onload = function() {
            if (latest_request.status >= 200 && latest_request.status < 400) {
                var dat = JSON.parse(latest_request.responseText);
               self.create_dashboard(dat)
            }
        };
        latest_request.send();
    }
}

var dashboard = new Dashboard();

setInterval(function(){
    dashboard.refresh_latest();
}, 1000);
