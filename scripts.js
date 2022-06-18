var taskListOpen = false;
var journalListOpen = false;

document.getElementById("taskList").addEventListener("click", function(event) {
    taskListOpen = !taskListOpen;
    var taskList = document.getElementById("taskList");
    var taskListParent = taskList.parentElement;

    if (taskListOpen) {
        for (var counter = 0; counter < taskListParent.children.length; counter++) {
            var child = taskListParent.children[counter];
            console.log(child);
            if (child.classList.contains("subItem") && taskList != child) {
                child.classList.add("slide-bottom");
                child.style.display = "block";
            }
        }
    } else {
        for (var counter = 0; counter < taskListParent.children.length; counter++) {
            var child = taskListParent.children[counter];
            if (child.classList.contains("subItem")) {
                child.classList.remove("slide-bottom");
                child.style.display = "none";
            }
        }
    }
});

document.getElementById("journal").addEventListener("click", function(event) {
    journalListOpen = !journalListOpen;
    var journalList = document.getElementById("journal");
    var journalListParent = journalList.parentElement;

    if (journalListOpen) {
        for (var counter = 0; counter < journalListParent.children.length; counter++) {
            var child = journalListParent.children[counter];
            console.log(child);
            if (child.classList.contains("subItem") && journalList != child) {
                child.classList.add("slide-bottom");
                child.style.display = "block";
            }
        }
        document.getElementById("journalArrow").classList.add("rotate180");
    } else {
        for (var counter = 0; counter < journalListParent.children.length; counter++) {
            var child = journalListParent.children[counter];
            if (child.classList.contains("subItem")) {
                child.classList.remove("slide-bottom");
                child.style.display = "none";
            }
        }
        document.getElementById("journalArrow").classList.remove("rotate180");
    }
});
