
async function getJournalEntry() {
    const baseUrlPost = "http://127.0.0.1:5000/getJournalEntry";
    const inputJson = {
        date: document.getElementById("dateInput").value
    }
    const response = await fetch(baseUrlPost, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        }, 
        body: JSON.stringify(inputJson)
    }).then(function(response) {
        response.json().then(function(data) {
            document.getElementById("journal-main").value = data["journal"];
            document.getElementById("title").value = data["title"];
        });
    });
}

async function saveJournalEntry() {
    const baseUrlPost = "http://127.0.0.1:5000/saveJournalEntry";

    const inputJson = {
        input: document.getElementById("journal-main").value,
        title: document.getElementById("title").value,
        date: document.getElementById("dateInput").value
    }
    const response = await fetch(baseUrlPost, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(inputJson)
    }).then(function(response) {
        response.json().then(function(data) {
            console.log("saved");
        });
    });
}

async function getJournalTitle() {
    const baseUrlPost = "http://127.0.0.1:5000/getJournalTitle";

    const inputJson = {
        date: document.getElementById("dateInput").value
    }
    const response = await fetch(baseUrlPost, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        }, 
        body: JSON.stringify(inputJson)
    }).then(function(response) {
        response.json().then(function(data) {
            document.getElementById("title").value = data;
        });
    });
}


async function saveJournalTitle() {
    const baseUrlPost = "http://127.0.0.1:5000/saveJournalTitle";

    const inputJson = {
        input: document.getElementById("journal-main").value, 
        title: document.getElementById("title").value,
        date: document.getElementById("dateInput").value
    }
    const response = await fetch(baseUrlPost, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(inputJson)
    }).then(function(response) {
        response.json().then(function(data) {
        });
    });
}

async function getCurrentUser() {
    const baseUrlPost = "http://127.0.0.1:5000/getCurrentUser";
    const response = await fetch(baseUrlPost, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    }).then(function(response) {
        response.json().then(function(data) {
            document.getElementById("currentUser").innerHTML = "Current User: " + data;
        });
    });
}

async function logout() {
    const baseUrlPost = "http://127.0.0.1:5000/logout";
    const response = await fetch(baseUrlPost, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    }).then(function(response) {
        response.json().then(function(data) {
            window.location.href = "http://127.0.0.1:5000/login";
        });
    });
}

function initJournals() {
    getJournalNames();
}

async function getJournalNames() {
    const baseUrlPost = "http://127.0.0.1:5000/getJournalNames";
    const response = await fetch(baseUrlPost, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    }).then(function(response) {
        response.json().then(function(data) {
            console.log(data);
            
            for (var i = 0; i < data.length; i++) {
                console.log(data[i]['title']);
                const para = document.createElement("p");
                para.innerHTML = data[i]['title'];
                document.getElementById("journals").appendChild(para);

                para.setAttribute(
                    'style',
                    'width: 100%; border: thin solid black; border-radius: 10px;text-align:center;',
                  );

                para.setAttribute("id", data[i]['date']);

                para.onclick = function () {
                    document.getElementById("dateInput").value = this.id;
                    console.log(this.id);
                    getJournalEntry();
                };

                para.onmouseout  = function () {
                    document.getElementById(this.id).class = "";
                };

                para.onmouseover = function () {
                    document.getElementById(this.id).class = "hover";
                };
            }


        });
    });
}


function initText() {
    document.getElementById("journal-main").innerHTML = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n";
    document.getElementById("dateInput").value = "2022-06-18";
    getJournalEntry();
    getJournalTitle();

    document.getElementById("journal-main").addEventListener("input", function(event) {
        saveJournalEntry();
    });

    document.getElementById("title").addEventListener("input", function(event) {
        saveJournalTitle();
    });

    document.getElementById("logout").addEventListener("click", function(event) {
        logout();
    });

    document.getElementById("dateInput").addEventListener("change", function(event) {
        getJournalEntry();
    });
    getCurrentUser();
}
