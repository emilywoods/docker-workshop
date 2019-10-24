class Dashboard {
    constructor() {
        this.refresh_latest();
        this.create_dashboard();
    }

    create_dashboard(dat) {
       var html = ""
       for (var ip in dat) {
        var domString = `
        <div class="entry">
            <div class="user">${dat[ip].user}</div>
            <div class="address">${ip}:${dat[ip].port}</div>
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
