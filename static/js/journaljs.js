
async function getJournalEntry() {
    const baseUrlPost = "http://127.0.0.1:5000/getJournalEntry";
    const response = await fetch(baseUrlPost, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        }
    }).then(function(response) {
        response.json().then(function(data) {
            document.getElementById("journal-main").value = data;
        });
    });
}

async function saveJournalEntry() {
    const baseUrlPost = "http://127.0.0.1:5000/saveJournalEntry";

    const inputJson = {
        input: document.getElementById("journal-main").value
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

function initText() {
    document.getElementById("journal-main").innerHTML = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n";

    getJournalEntry();

    document.getElementById("journal-main").addEventListener("input", function(event) {
        saveJournalEntry();
    });
}


