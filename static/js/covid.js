function confirm() {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            img_name = this.responseText
            document.getElementById("view").innerHTML = '<img src="./static/img/'+img_name+ '" width=500 height=400>'
        }
    };
    xhttp.open("POST", "confirm");
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send();
}

function death() {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            img_name = this.responseText
            document.getElementById("view").innerHTML = '<img src="./static/img/'+img_name+ '" width=500 height=400>'
        }
    };
    xhttp.open("POST", "death");
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send();
}

function vaccine() {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            img_name = this.responseText
            document.getElementById("view").innerHTML = '<img src="./static/img/'+img_name+ '" width=500 height=400>'
        }
    };
    xhttp.open("POST", "vaccine");
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send();
}

function gdp() {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            img_name = this.responseText
            document.getElementById("view").innerHTML = '<img src="./static/img/'+img_name+ '" width=500 height=400>'
        }
    };
    xhttp.open("POST", "gdp");
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send();
}

function population() {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            img_name = this.responseText
            document.getElementById("view").innerHTML = '<img src="./static/img/'+img_name+ '" width=500 height=400>'
        }
    };
    xhttp.open("POST", "population");
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send();
}

function chart_view() {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            img_name = this.responseText
            document.getElementById("view1").innerHTML = '<img src="./static/img/covid_gdp_plot1.png" width=95%>'
            document.getElementById("view2").innerHTML = '<img src="./static/img/covid_gdp_plot2.png" width=95%>'
            document.getElementById("view3").innerHTML = '<img src="./static/img/covid_gdp_plot3.png" width=95%>'
        }
    };
    xhttp.open("post", "covidgdp");
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send();
}
